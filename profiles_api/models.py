from django.db import models
from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin,
                                        BaseUserManager)


class UserProfileManager(BaseUserManager):
    """
    Manager for user profiles.
    """
    def create_user(self, email, name, password=None):
        """
        Creates a new user profile
        :param email: str in the format abc@abc.com
        :param name: Full name of the user
        :param password: Str to be saved as Hash object
        :return: created user
        """
        try:
            email = self.normalize_email(email)
            user = self.model(email=email, name=name)
            user.set_password(password)
            # This saves the password as hash object
            user.save(using=self._db)
            # Since there can be many dbs in our app, the
            # best practice is to save the user in current db.
            return user
        except Exception as e:
            raise

    def create_superuser(self, email, name, password):
        """
        This will be used to craete the super user from the CLI.
        :param email: str in the format abc@abc.com
        :param name: Full name of the user
        :param password: Str to be saved as Hash object
        :return: created super user
        """
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    DB Model for users in system. Later to configure it add this to
    settings.py so that django knows to use this class instead of
    the default model it already has.
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email


class ProfileFeedItem(models.Model):
    """
    Status updates, it uses foreign key to
    connect with other models.
    """
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status_text
