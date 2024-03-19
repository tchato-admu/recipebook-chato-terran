from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator


class Ingredient(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('recipe-detail', args = [self.name])


class Recipe(models.Model):
    name = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50, default = '')
    createdOn = models.DateTimeField(auto_now_add = True)
    updatedOn = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:recipe-detail', args = [self.pk])


class RecipeIngredient(models.Model):
    name = models.CharField(max_length = 50)
    quantity = models.IntegerField()
    measurement = models.CharField(max_length = 50, default = "pc/s")

    ingredient = models.ForeignKey(
        Ingredient, 
        on_delete = models.CASCADE,
        related_name = 'recipe'
    )

    recipe = models.ForeignKey(
        Recipe, 
        on_delete = models.CASCADE,
        related_name = 'ingredients'
    )

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    bio = models.CharField(max_length = 1000, validators = [MinLengthValidator(255)])