from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from ..tasks import send_password_reset_email_task

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    reset_password_url = "{}?token={}".format(
            instance.request.build_absolute_uri(reverse('password_reset:reset-password-confirm')),
            reset_password_token.key)

    send_password_reset_email_task.delay(
        user_email=reset_password_token.user.email,
        username=reset_password_token.user.username,
        reset_password_url=reset_password_url
    )
    
