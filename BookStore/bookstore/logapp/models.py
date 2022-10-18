# from django.db import models
# class User(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     first_name = models.CharField(max_length=50, default='')
#     last_name = models.CharField(max_length=50, default='')
#     username = models.CharField(max_length=50, unique=True)
#     email = models.EmailField(max_length=100, unique=True)
#     phonenumber = models.BigIntegerField(default=0, unique=True)
#     hname = models.CharField(max_length=50)
#     country = models.CharField(max_length=50)
#     state = models.CharField(max_length=50)
#     city = models.CharField(max_length=50)
#     pincode = models.IntegerField(default=0)
#     password = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.email
#
#
#
#
# #Login Table
# class log_user(models.Model):
#      username = models.CharField(max_length=50,default='')
#      email= models.CharField(max_length=200,primary_key=True,unique=True)
#      password = models.CharField(max_length=100)


from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
import datetime


class MyAccountManager(BaseUserManager):
    def create_user(self, first_name,last_name,username,email,phonenumber,hname,country,state,city,pincode,password=None):
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            phonenumber=phonenumber,
            hname=hname,
            country=country,
            state=state,
            city=city,
            pincode=pincode,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, username, password, email,**extra_fields):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,**extra_fields

        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phonenumber = models.BigIntegerField(default=0, unique=True)
    hname = models.CharField(max_length=50)
    country = models.CharField(max_length=50 )
    state = models.CharField(max_length=50 )
    city = models.CharField(max_length=50 )
    pincode = models.IntegerField(default=0)

    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name','phonenumber','hname','country','state','city','pincode']
    # object=MyAccount()
    objects = MyAccountManager()
    # objects = models.Manager()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True


