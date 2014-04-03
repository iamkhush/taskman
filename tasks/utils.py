from django.db.models.signals import post_save
from django.contrib.auth.models import User

from views import add_acton_to_log


post_save.connect(add_acton_to_log, sender=User)