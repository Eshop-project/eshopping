from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _

class AccountManagment(BaseUserManager):
    def create_user(self, email, username='None', first_name='None', last_name='None', password=None):
        if not email:
            raise ValueError(_('User must have a valid email address.'))

        user    = self.model(
                email = self.normalize_email(email),
                username = username,
                first_name = first_name,
                last_name = last_name,
                )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        user    = self.create_user(
                email = self.normalize_email(email),
                password = password,
                )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save()
        return user

class Account(AbstractBaseUser):
    email       = models.EmailField(verbose_name='email', max_length=50, unique=True)
    username    = models.CharField(max_length=35,)#, unique=True)
    first_name  = models.CharField(max_length=25)
    last_name   = models.CharField(max_length=35)
    # Required fields
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login  = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin    = models.BooleanField(default=False)
    is_active   = models.BooleanField(default=True)
    is_staff    = models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AccountManagment()

    def __str__(self):
        # Could add more information
        return self.email # + ', ' + self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
