from django.db import models
from django.contrib.auth.models import User


GENDER_CHOICES = (
   ('male', 'Male'),
   ('female', 'Female')
)
RELATIONAL_STATUS = (
   ('singale', 'Singale'),
   ('marrid', 'Marrid')
)
class Profile(models.Model):
    nick_name = models.CharField(max_length=20)
    hobby = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='image')
    status = models.CharField(max_length=30)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=128)
    relationship_status = models.CharField(choices=RELATIONAL_STATUS, max_length=128)
    phone = models.IntegerField()
    user = models.ForeignKey(User, on_delete="CASCADE", null=True)

    def __str__(self):
        return self.nick_name

class Message(models.Model):
    message = models.TextField(max_length=100)
