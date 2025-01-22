from django.apps import AppConfig

# 'AdminManagementConfig' class defines the configuration for the 'Admin_Management' app.
class AdminManagementConfig(AppConfig):
    name = 'Admin_Management'  # This sets the name of the app. Make sure this matches the name of the app folder.

    # The 'ready' method is called when the app is ready for use.
    def ready(self):
        # This imports the signals file to ensure that any signal handlers in 'signals.py' are registered
        # The import path should be adjusted based on your project structure
        import Admin_Management.signals  # Signals are imported to activate them as soon as the app starts.
