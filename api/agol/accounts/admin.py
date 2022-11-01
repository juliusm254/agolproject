# from django.contrib import admin
# # from .models import User, OperationsUser, CustomerUser
# from django.contrib.auth.admin import UserAdmin

# from .forms import CustomUserCreationForm, CustomUserChangeForm
# # Register your models here.
# @admin.register(User)
# class RequestDemoAdmin(admin.ModelAdmin):
#   list_display = ['username','name', 'email', 'type', 'customer_id']

# from .models import User, CustomerAccount

# admin.site.register(User)
# admin.site.register(CustomerAccount)


# class CustomerUserInline(admin.StackedInline):
#   model = User
#   can_delete: False


# # admin.register(OperationsUser, UserAdmin)
# class OperationsUserAdmin(UserAdmin):
  
#   fieldsets=(
#     *UserAdmin.fieldsets, (
#       'Additional Info', {'fields':(
#         'type',
#       )}
#     )
#   )
# # class OperationsUserAdmin(UserAdmin):
# #   pass
# class CustomerUserAdmin(UserAdmin):
#   inlines = (CustomerUserInline,)
#   add_form = CustomUserCreationForm
#   form = CustomUserChangeForm
#   model = CustomerUser

#   # fieldsets=(
#   #   *UserAdmin.fieldsets, (
#   #     'Additional Info', {'fields':(
#   #       'type','customer_id',
#   #     )}
#   #   )
#   # )
# admin.site.register(OperationsUser, OperationsUserAdmin)
# admin.site.register(CustomerUser, CustomerUserAdmin)

from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from accounts.models import User


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email','type' )

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password','is_active', 'type')


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'type')
    # list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        # ('Personal info', {'fields': ('date_of_birth',)}),
        ('Permissions', {'fields': ('type',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2','type', 'customer_id'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)