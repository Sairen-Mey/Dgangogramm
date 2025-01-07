from django.db import models


class User(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    bio = models.CharField(max_length=500)
    avatar = models.ImageField(max_length=100, upload_to="avatars/")

    class Meta:
        db_table = "users"


# class Post()