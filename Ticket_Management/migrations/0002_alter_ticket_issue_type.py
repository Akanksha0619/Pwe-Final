# Generated by Django 5.0.2 on 2025-01-01 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket_Management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='issue_type',
            field=models.CharField(choices=[('Furnished Rooms', 'Furnished Rooms'), ('Wi-Fi Connectivity', 'Wi-Fi Connectivity'), ('Clean Drinking Water', 'Clean Drinking Water'), ('Washing Machine', 'Washing Machine')], max_length=50),
        ),
    ]
