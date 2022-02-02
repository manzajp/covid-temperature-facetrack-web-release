from email.policy import default
from django.db import models
from login.models import User

class Camera(models.Model):
    cameraName = models.CharField(max_length=50)
    ipAddress = models.GenericIPAddressField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.cameraName

class Image(models.Model):
    imageName = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    temp = models.DecimalField(max_digits=5, decimal_places=1)
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE)

