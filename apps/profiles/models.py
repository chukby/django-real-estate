from apps.common.models import TimeStampedUUIDModel 
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


User = get_user_model()

class Gender(models.TextChoices):
    MALE = "MALE", _("Male")
    FEMALE = "FEMALE", _("Female")
    OTHER = "OTHER", _("Other")

# Create your models here.
class Profile(TimeStampedUUIDModel):
    """
    Profile model to store additional information about users.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name=_("User")
    )
    gender = models.CharField(
        max_length=10,
        choices=Gender.choices,
        verbose_name=_("Gender"),
        default=Gender.OTHER
    )
    phone_number = PhoneNumberField(
        verbose_name=_("Phone Number"), 
        max_length=30,
        default="+2349035643421",  
        null=True,
        blank=True, 
        unique=True
    )
    about_me = models.TextField(blank=True, verbose_name=_("About Me"), default="Say something about yourself")
    license = models.CharField(max_length=100, verbose_name=_("License"), blank=True, null=True)
    profile_photo = models.ImageField(
        verbose_name=_("Profile Photo"),        
        default="/default_profile_photo.png"
    )
    country = CountryField(blank_label='(select country)',
                            verbose_name=_("Country"),
                            default='NG',
                            blank=False, 
                            null=False
    )
    city = models.CharField(max_length=100, verbose_name=_("City"), blank=False, null=False, default="Lagos")
    is_buyer = models.BooleanField(
        verbose_name=_("Is Buyer"), 
        default=False, 
        help_text=_("Are you looking to buy properties?")
    )
    is_seller = models.BooleanField(
        verbose_name=_("Is Seller"), 
        default=False, 
        help_text=_("Are you looking to sell properties?")
    )
    is_agent = models.BooleanField(
        verbose_name=_("Is Agent"), 
        default=False, 
        help_text=_("Are you an agent?")
    )
    top_agent = models.BooleanField(
        verbose_name=_("Top Agent"),
        default=False,
        help_text=_("Is this agent a top agent?")
    )
    rating = models.DecimalField(
        max_digits=4, 
        decimal_places=2, 
        verbose_name=_("Rating"), 
        null=True,
        blank=True,
        default=0.00
    )
    reviews_count = models.IntegerField(
        verbose_name=_("Number of Reviews"), 
        default=0,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.user.username}'s Profile"