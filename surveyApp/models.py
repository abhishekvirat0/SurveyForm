from django.db import models

# Create your models here.


class Survey_Form(models.Model):
    name = models.CharField(blank=False, max_length=100)
    l_name = models.CharField(blank=False, max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)

    relation = models.CharField(max_length=100)
    employment = models.CharField(max_length=100)
    pregnancy = models.CharField(max_length=100, blank=True, default='No', null=True)
    diet = models.CharField(max_length=100)

    first_food = models.CharField(max_length=100)
    second_food = models.CharField(max_length=100)
    third_food = models.CharField(max_length=100)
    fourth_food = models.CharField(max_length=100)
    fifth_food = models.CharField(max_length=100)

    rating = models.IntegerField()
