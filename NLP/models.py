from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class NLP_MAPS(models.Model):
    id = models.IntegerField(primary_key=True)
    x = models.FloatField() 
    y = models.FloatField()
    Address = models.TextField()
    intensity = models.IntegerField()
    Remarks = models.CharField(max_length=50,default='Road Block',)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Address 

class Organisation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.CharField(max_length=100,default='NITK Rescue Team')
    def __str__(self):
        return self.organisation

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Organisation.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.organisation.save()