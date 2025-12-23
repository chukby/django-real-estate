import logging
from django.db.models.signals import post_save 
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from apps.profiles.models import Profile
from real_estate.settings.base import AUTH_USER_MODEL

logger = logging.getLogger(__name__)   

@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
            logger.info(f'Profile created for user {instance.username}')
        except Exception as e:
            logger.error(f'Error creating profile for user {instance.username}: {e}')

@receiver(post_save, sender=AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
        logger.info(f'Profile saved for user {instance.username}')
    except Exception as e:
        logger.error(f'Error saving profile for user {instance.username}: {e}') 
 
