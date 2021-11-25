from django.db import models

class Camera(models.Model):
    cameraName = models.CharField(max_length=50)
    ipAddress = models.GenericIPAddressField
    def __str__(self):
        return self.cameraName

class Image(models.Model):
    imageName = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')

