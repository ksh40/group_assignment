from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class DonorManager(BaseUserManager):
    def create_user(self, email, name, phone, age, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            phone=phone,
            age=age,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

class Donor(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone', 'age']

    objects = DonorManager()

    def __str__(self):
        return self.name
