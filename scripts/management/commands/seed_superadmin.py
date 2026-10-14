from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os
from dotenv import load_dotenv

load_dotenv()


class Command(BaseCommand):
    help = "Create the default superadmin user"

    def handle(self, *args, **kwargs):
        User = get_user_model()

        email = os.getenv("ADMIN_EMAIL")
        password = os.getenv("ADMIN_PASSWORD")

        if User.objects.filter(email=email).exists():
            self.stdout.write(self.style.WARNING("Superadmin already exists."))
            return

        user = User.objects.create_superuser(
            first_name="superadmin",
            last_name="admin",
            phone_number="9876543210",
            user_type="ADMIN",
            dob="2000-12-12",
            email=email,
            password=password,
        )

        self.stdout.write(
            self.style.SUCCESS(f"Superadmin created successfully: {user.email}")
        )
