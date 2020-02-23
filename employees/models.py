from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    department = models.CharField(max_length= 10 ,null= True, blank=True)
    designation = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self):
        return self.user.username






@receiver(post_save, sender = User)
def user_is_created(sender, instance,created, **kwargs):
    if created:
        Profile.objects.create(user = instance)
    else:
        instance.profile.save()




