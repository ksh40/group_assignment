from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class DonorManager(BaseUserManager):
    def create_user(self, name, amount, phone=None):
        if not name:
            raise ValueError("Incorrect username/Invalid name")
        user = self.model(

            name=name,
            amount=amount,
            phone=phone,
        )
        user.save(using=self._db)
        return user

class Donor(AbstractBaseUser):
    name = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    phone = models.CharField(max_length=15)

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['phone', 'amount']

    objects = DonorManager()

    def __str__(self):
        return self.name
