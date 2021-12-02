from django.db import models
# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()
    classname = models.CharField(max_length=80)

    #from https://stackpython.medium.com/how-to-start-django-project-with-a-database-postgresql-aaa1d74659d8  