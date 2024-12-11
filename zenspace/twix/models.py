from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.


class Twix(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    photo = models.ImageField(upload_to='twix_photos/', blank=True, null=True)
    text = models.TextField(max_length=240)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User,related_name="twix_like" ,blank=True)
    
    def number_of_likes(self):
        return self.likes.count()
        

    def __str__(self):
        return f'{self.user.username} - {self.text[:10]}'

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , null=True, blank=True)
    twix = models.ForeignKey(Twix , related_name="comments" , on_delete=models.CASCADE,)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.text[:20]}"






class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    follows = models.ManyToManyField("self", related_name="followed_by", symmetrical=False, blank=True)
    date_modified = models.DateTimeField(auto_now=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to="photos/", default='images/icon.png') 
    profile_bio = models.CharField(null=True, blank=True, max_length=500)
    email = models.EmailField(null=True, blank=True, max_length=100)
    facebook_link = models.URLField(max_length=200, null=True, blank=True)
    instagram_link = models.URLField(max_length=200, null=True, blank=True)
    linkedin_link = models.URLField(max_length=200, null=True, blank=True)
    

    def __str__(self):
        return f'{self.user.username}'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'profile'):
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
