from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _
from typing import Any, Dict, Optional, TypeVar
from django.db import models

T = TypeVar("T", bound=models.Model)


class CustomUserManager(BaseUserManager):
    """
    Custom user manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def email_validator(self, email: str) -> bool:
        """
        Validate the email format.
        """
        try:
            validate_email(email)
            return True
        except ValidationError:
            raise ValueError(_("The Email is not valid, please provide a valid email address."))   

    def create_user(
            self, 
            username: str, 
            first_name: str, 
            last_name: str, 
            email: Optional[str], 
            password: Optional[str] = None, 
            **extra_fields: Any
        ) -> T:
        """
        Create and save a User with the given email and password and other details.
        """
        if not username:
            raise ValueError(_("Please provide a Username"))
        if not first_name:
            raise ValueError(_("Please provide a First Name"))
        if not last_name:
            raise ValueError(_("Please provide a Last Name"))        

        if email:     
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Base User Account: An Email must be provided"))
        
        user = self.model(
            username=username, 
            first_name=first_name,
            last_name=last_name,
            email=email,
            **extra_fields
        )

        user.set_password(password)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        user.save(using=self._db)
        return user

    def create_superuser(
            self, 
            username: str, 
            first_name: str,
            last_name: str, 
            email: Optional[str], 
            password: Optional[str] = None, 
            **extra_fields: Any
            ) -> T:
        """
        Create and save a SuperUser with the given email and password and other fields.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superusers must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superusers must have is_superuser=True."))

        if not password:
            raise ValueError(_("Superusers must have a password."))
    
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Admin Account: An Email must be provided")) 
        

        user = self.create_user(username, first_name, last_name, email, password, **extra_fields)
        user.save(using=self._db)
        return user