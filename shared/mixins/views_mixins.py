from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import gettext_lazy as _

from apps.account.tokens import account_activation_token
from apps.cart.models import Cart, CartItem, Order


def send_activate_message(user, request) -> None:
    """send message for new user with activate linc"""
    to_email = user.email
    current_site = get_current_site(request)
    mail_subject = _('Activating your account')
    message = render_to_string(
        'registration/msg.jinja2',
        {
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        }
    )
    send_mail(
        mail_subject,
        from_email=settings.EMAIL_HOST_USER,
        message=_('link to confirm email and complete registration'),
        recipient_list=[to_email],
        html_message=message,
    )


def get_cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart
