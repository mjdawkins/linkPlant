from django.db import models

# Create your models here.

class Profile(models.Model):
    #choices stored as tuples, with choice, uman readbale value for the choice
    BG_CHOICES = (
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('yellow', 'Yellow'),  
        )
    
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    bg_color = models.CharField(max_length=50, choices=BG_CHOICES)
    
    
    def __str__(self):
        return self.name
    
class Link(models.Model):
    text = models.CharField(max_length=100)
    url = models.URLField()
    # on_delete cascade when the profile is deleted it delete all related links
    # related_name within Profile lets you give a name to the reverse relation to the profile model
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="links")
    
    def __str__(self):
        return f" {self.text} | {self.url}"
    