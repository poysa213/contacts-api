from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, phone_number, password=None):
        if not email:
            raise ValueError('Users must have an phone number')

        if not phone_number:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            phone_number=phone_number
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password, username, phone_number):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            phone_number=phone_number
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    email = models.EmailField(blank=True, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)



    REQUIRED_FIELDS = ['phone_number']

    objects = UserManager()


   

