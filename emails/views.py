from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from .forms import EmailForm
from django.contrib import messages
import imaplib
import email

from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from .forms import EmailForm
from .models import *

def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            recipient = form.cleaned_data['recipient']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Save the email to the database
            email_instance = Email_User.objects.create(
                user=request.user,
                subject=subject,
                sender=request.user.email,
                recipient=recipient,
                body=message,
                is_sent=True
            )

            try:
                send_mail(subject, message, request.user.email, [recipient])
                messages.success(request, 'Email sent successfully!')
            except BadHeaderError:
                messages.error(request, 'Invalid header found.')
            except Exception as e:
                messages.error(request, f"Error sending email: {e}")
            return redirect('sent')
    else:
        form = EmailForm()
    
    return render(request, 'send_email.html', {'form': form})


def fetch_emails(username, password):
    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')  # Gmail IMAP server
        mail.login(username, password)
        mail.select('inbox')

        result, data = mail.search(None, 'ALL')  # Fetch all emails
        email_ids = data[0].split()

        emails = []
        for e_id in email_ids:
            result, message_data = mail.fetch(e_id, '(RFC822)')
            raw_email = message_data[0][1]
            email_message = email.message_from_bytes(raw_email)

            emails.append({
                'subject': email_message['subject'],
                'from': email.utils.parseaddr(email_message['from'])[1],
                'to': email.utils.parseaddr(email_message['to'])[1] if email_message['to'] else 'N/A',
                'date': email_message['date'],
                'body': get_body(email_message),
            })

        return emails
    except Exception as e:
        return []


def get_body(email_message):
    if email_message.is_multipart():
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                return part.get_payload(decode=True).decode()
    else:
        return email_message.get_payload(decode=True).decode()

from django.shortcuts import render, redirect
from django.contrib import messages

def inbox(request):
    if request.method == 'POST':
        username = request.user.email
        password = request.POST.get('password')  # Handle securely
        
        if not password:
            messages.error(request, 'Password is required to fetch emails.')
            return redirect('inbox')
        
        emails = fetch_emails(username, password)
        
        if not emails:
            messages.error(request, 'Failed to retrieve emails. Please check your credentials or try again later.')
        
        return render(request, 'inbox.html', {'emails': emails})
    
    return render(request, 'login_to_inbox.html')

def sent(request):
    emails = Email_User.objects.filter(user=request.user).order_by('-date_sent')  # Fetch emails for the logged-in user
    return render(request, 'sent.html', {'emails': emails})
