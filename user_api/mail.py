from django.core.mail import send_mail
from rest_framework.authtoken.models import Token

def send_activation_email(user):
    token = Token.objects.create(user=user)
    send_mail(
        'Verify your account',
        'Your account activation code: ' + token.key,
        'our@email.com',
        [user.email],
        fail_silently=False,
    )
