from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, \
    BaseUserManager


class UserProfileManager(BaseUserManager):
    """Custom Manager for User Profile Model"""

    def create_user(self, email, name, password=None):
        """create a new user profile"""
        if not email:
            raise ValueError("User must have a vaild email address")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password=password)
        user.save(using=self._db)

        return user


    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database modelfor users in the system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def get_full_name(self):
        """Retrieve full name of User"""
        return self.name

    def get_short_name(self):
        """Retrieve short name """
        return self.name

    def __str__(self):
        """Return String representation of our user"""
        return self.email