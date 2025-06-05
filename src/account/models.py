from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomManager(models.Manager):
    def create_user(self, email, name, password, **kwargs):
        if not email:
            raise ValueError('Email is required')
        if not name:
            raise ValueError('Name is required')
        user = self.model(name=name, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, name, password, **kwargs):
        kwargs['is_staff'] = True
        kwargs['is_superuser'] = True
        return self.create_user(email, name, password, **kwargs)


class CustomUser(AbstractUser):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    email = models.EmailField(unique=True)
    objects = CustomManager()
