from django.db import models

class User(models.Model):
    userName = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date created')
    def __str__(self):
        return self.userName
