from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from celery import shared_task

@shared_task
def send_password_reset_email_task(user_email, username, reset_password_url):
    title = settings.EMAIL_TITLE
    from_email = settings.DEFAULT_FROM_EMAIL

    context = {
        'subject': title,
        'username': username,
        'reset_password_url': reset_password_url,
    }

    email_html_message = render_to_string('email/user_reset_password.html', context)
    email_plaintext_message = render_to_string('email/user_reset_password.txt', context)

    msg = EmailMultiAlternatives(
        "Password Reset for {title}".format(title=title),
        email_plaintext_message,
        from_email,
        [user_email]
    )

    msg.attach_alternative(email_html_message, "text/html")
    msg.send()

    return f"Email sent to {user_email}"