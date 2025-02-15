from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from Social.models import UserActivity
from django.contrib.auth.signals import user_login_failed
from django.dispatch import receiver
import logging

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    UserActivity.objects.create(user=user, action="Login")

@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    UserActivity.objects.create(user=user, action="Logout")

logger = logging.getLogger(__name__)

@receiver(user_login_failed)
def log_failed_login(sender, credentials, request, **kwargs):
    ip = request.META.get('REMOTE_ADDR', 'IP non disponibile')
    logger.warning(f"Tentativo di login fallito per username: {credentials.get('username', 'sconosciuto')}, IP: {ip}")