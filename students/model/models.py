from django.db import models


class Students(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    profile_image = models.ImageField(upload_to='profile_images/')

    def __str__(self):
        return self.name
