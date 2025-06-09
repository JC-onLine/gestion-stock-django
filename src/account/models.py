from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


class CustomManager(BaseUserManager):
    def create_user(self, email, username, password, **kwargs):
        if not email:
            raise ValueError('Email is required')
        if not username:
            raise ValueError('Name is required')
        user = self.model(username=username, email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password, **kwargs):
        kwargs['is_staff'] = True
        kwargs['is_superuser'] = True
        return self.create_user(username, email, password, **kwargs)


class CustomUser(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    email = models.EmailField(unique=True)
    objects = CustomManager()
