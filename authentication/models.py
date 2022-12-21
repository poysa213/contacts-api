# from django.db import models
# from django.contrib.auth.models import AbstractUser, BaseUserManager
# from rest_framework import status
# from django.contrib import auth
# Create your views here.



# class UserManager(BaseUserManager):

#     use_in_migration = True

#     def create_user(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_active', True)
#         if not email:
#             raise ValueError('Email is Required')
#         user = self.model(email=self.normalize_email(email), **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff = True')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser = True')

#         return self.create_user(email, password, **extra_fields)


# class User(AbstractUser):
#     email = models.EmailField(unique=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ('username',)

#     objects = UserManager()

#     def __str__(self):
#         return self.email
    

