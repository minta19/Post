from django.db import models

from django.db.models import CharField,TextField,DateField,ImageField,ForeignKey

# Create your models here.
class Post(models.Model):
    title=CharField(max_length=255)
    description=TextField()
    created_date=DateField(auto_now_add=True)
    image=ImageField(upload_to='media/')
    
    def __str__(self) -> str:
        return self.title
