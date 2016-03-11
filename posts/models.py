from django.db import models
# from django.contrib.auth.models import User
# from django.utils.text import slugify
# from django.utils import timezone #make sure to set the timezone 

# Create your models here.

class WCard(models.Model):
    content = models.CharField(max_length=4000)
    show = models.BooleanField(default=True)

    # this is a custom save method
    def save(self, *args, **kwargs):
        super(WCard, self).save(*args, **kwargs)

    # this create a dictionary from an object to use with ajax
    def to_json(self):
        return {
            "content": self.content,
            "show": self.show,
        }


class BCard(models.Model):
    content = models.CharField(max_length=4000)
    show = models.BooleanField(default=True)

    # this is a custom save method
    def save(self, *args, **kwargs):
        super(BCard, self).save(*args, **kwargs)

    # this create a dictionary from an object to use with ajax
    def to_json(self):
        return {
            "content": self.content,
            "show": self.show,
        }



        
