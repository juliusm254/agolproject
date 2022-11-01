from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.urls import reverse
from django.db import transaction

from customers.models import Customer

class UserManager(BaseUserManager):
    def create_user(self, email, name, customer_id, password=None):
        if not email:
            raise ValueError('Users must have an email address')

    # def accelerate(self):
    #     return "Go faster"
        email = self.normalize_email(email)
        email = email.lower()

        user = self.model(
            email= email,
            customer_id = customer_id,
            name=name
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_operatons_user(self, email, name, password=None):
        user = self.create_user(email, name, password)

        user.type = 'OPERATIONS'
        user.save(using=self._db)

        return user

    def create_customer_user(self, email,customer_id, name, password=None):
        user = self.create_user(email, name,customer_id, password)

        user.type = 'CUSTOMER'
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password=None):
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user



class User(AbstractBaseUser, PermissionsMixin):
    OPERATIONS = 'OPERATIONS'
    CUSTOMER = 'CUSTOMER'
    ADMIN = 'ADMIN'

    TYPE = (
        (OPERATIONS, 'Operations'),       
        (CUSTOMER, 'Customer'),
        (ADMIN, 'Admin'),
     )

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    customer_id = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, blank=True, null=True)
    type = models.CharField(max_length=25, choices=TYPE)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','type',]

    def __str__(self):
        return self.email 