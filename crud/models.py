from django.db import models
from django.shortcuts import redirect
from django.urls import reverse


# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(max_length=80)
    phone = models.CharField(max_length=80)
    address = models.CharField(max_length=80)
    city = models.CharField(max_length=80)
    state = models.CharField(max_length=80)

    def get_absolute_url(self):
        return reverse("crud:customer-details", kwargs={"id": self.id})

    def get_update_url(self):
        return reverse("crud:customer-update", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("crud:customer-delete", kwargs={"id": self.id})
