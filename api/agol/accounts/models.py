from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.urls import reverse
from django.db import transaction

from customers.models import Customer


# class User(AbstractUser):
#     class Types(models.TextChoices):
#         OPERATIONS = "OPERATIONS", "OperationsUser"
#         CUSTOMER = "CUSTOMER", "CustomerUser"

#     base_type = Types.OPERATIONS

#     # What type of user are we?
#     type = models.CharField(
#         _("Type"), max_length=50, choices=Types.choices, default=Types.OPERATIONS
#     )
#     customer_id = models.ForeignKey(
#         Customer, on_delete=models.SET_NULL, blank=True, null=True)
#     # First Name and Last Name Do Not Cover Name Patterns
#     # Around the Globe.
#     name = models.CharField(_("Name of User"), blank=True, max_length=255)

#     # def get_absolute_url(self):
#     #     return reverse("users:detail", kwargs={"username": self.username})

#     # def save(self, *args, **kwargs):
#     #     if not self.id:
#     #         self.type = self.type
#     #     return super().save(*args, **kwargs)

    


# class OperationsManager(BaseUserManager):
#     def get_queryset(self):
#         return super(OperationsManager, self).get_queryset().filter(type='OPERATIONS')
    
#     USERNAME_FIELD = 'username'


# class OperationsUser(User):
#     base_type = User.Types.OPERATIONS
#     objects = OperationsManager()

#     class Meta:
#         proxy = True

#     # def whisper(self):
#     #     return "whisper"
        

# class CustomerManager(BaseUserManager): 

#     def get_queryset(self, *args, **kwargs):
#         # return CustomerUser.objects.all()
#         return super().get_queryset(*args, **kwargs).filter(type=User.Types.CUSTOMER)

#     def create(self, **kwargs):
#         kwargs.update({'type': 'CUSTOMER'})
#         return super(CustomerManager, self).create(**kwargs)

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['customer_id']

# class CustomerUser(User):
#     base_type = User.Types.CUSTOMER
#     objects = CustomerManager()

#     # @property
#     # def more(self):
#     #     return self.customermore

#     class Meta:
#         proxy = True



# # class OperationsMore(models.Model):
# #     user = models.OneToOneField(User, on_delete=models.CASCADE)
# #     gadgets = models.TextField()





# # class CustomerMore(models.Model):
# #     user = models.OneToOneField(User, on_delete=models.CASCADE)


# class CustomerAccount(models.Model):
#     user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
#     customer_id = models.ForeignKey(
#         Customer, on_delete=models.SET_NULL, blank=True, null=True)
#     location = models.CharField(max_length=20)

#     @transaction.atomic
#     def save(self, *args, **kwargs):
#         user = super().save()
#         print(self)        
#         self.save()
#         customer = Customer.objects.create(user=user)        
#         customer.save()
#         return user

# class OperationsAccount(models.Model):
#     user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
#     phone_number = models.CharField(max_length=20)
#     designation = models.CharField(max_length=20)

    
    


    # def accelerate(self):
    #     return "Go faster"

class UserManager(BaseUserManager):
    def create_user(self, email, name, customer_id, password=None):
        if not email:
            raise ValueError('Users must have an email address')

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