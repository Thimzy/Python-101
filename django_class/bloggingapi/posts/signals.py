import logging

from allauth.account.signals import user_logged_in
from django.dispatch import receiver

logger = logging.getLogger(__name__)


@receiver(user_logged_in)
def login_logger(request, user, **kwargs):
    logger.info("{} logged in with {}".format(user.email, request))