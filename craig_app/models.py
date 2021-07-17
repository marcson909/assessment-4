from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as text



# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self) -> str:
        return f"ID: {self.id} Name: {self.name}"

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')

    def __str__(self) -> str:
        return f"""
        ID: {self.id} 
        Title: {self.title}
        Description: {self.description}
        Created: {self.created_at}
        """
    
    def datepublished(self):
        return self.created_at.strftime('%m/%d')

