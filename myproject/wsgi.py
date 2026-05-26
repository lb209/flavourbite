import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_wsgi_application()

# FIX: Vercel par khali database mein tables banane ke liye auto-migrate script
if 'VERCEL' in os.environ:
    from django.core.management import call_command
    try:
        print("Running automatic migrations on Vercel...")
        call_command('migrate', interactive=False)
        print("Migrations completed successfully!")
    except Exception as e:
        print(f"Migration error: {e}")