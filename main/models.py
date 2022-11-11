from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=125)
    desc = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    category = models.ForeignKey(
        to="Category",
        on_delete=models.SET_NULL,
        null=True,
        related_name='books'
    )


class Category(models.Model):
    title = models.CharField(max_length=125, primary_key=True)
