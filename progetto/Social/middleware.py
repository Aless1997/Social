import logging
from django.utils.timezone import now

logger = logging.getLogger(__name__)
logging.basicConfig(filename='login_records.log', level=logging.INFO)

class LoginLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated and request.path == "/accounts/login/":
            ip = request.META.get("REMOTE_ADDR", "")
            log_message = f"Utente: {request.user.username}, Data: {now()}, IP: {ip}"
            logger.info(log_message)

        return response
