from django.db import models
import uuid


# Create your models here.
class TimeStampedUUIDModel(models.Model):
    """
    An abstract base class model that provides self-updating
    'created' and 'modified' fields along with a UUID primary key.
    """
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True