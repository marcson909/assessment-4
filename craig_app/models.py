from django.utils import timezone
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as text

def validate_category_name_presence(name):
    if len(name) == 0:
        raise ValidationError(text(
            'This field cannot be blank.'
        ))

def validate_post_title_presence(title):
    if len(title) == 0:
        raise ValidationError(text(
            'This field cannot be blank.'
        ))

def validate_post_description_presence(description):
    if len(description) == 0:
        raise ValidationError(text(
            'This field cannot be blank.'
        ))
def validate_created(created_at):
    if created_at > timezone.now():
        raise ValidationError(text("Can't create post in the future."))


class Category(models.Model):
    name = models.CharField(max_length=200, validators=[validate_category_name_presence])
    
    #self referencing foreignkey allows Category to have its own subcategories recursively
    #example: Jobs category can have Tech as a child
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self) -> str:
        return f"ID: {self.id} Name: {self.name}"

class Post(models.Model):
    title = models.CharField(max_length=200, validators=[validate_post_title_presence])
    description = models.CharField(max_length=1000, validators=[validate_post_description_presence])

    #automatically sets time when post is created
    created_at = models.DateTimeField(auto_now_add=True, validators=[validate_created])

    #is null until post is updated and then is auto populated with time
    updated_at = models.DateTimeField(auto_now=True)
    
    #FK for Category relationship
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')

    def __str__(self) -> str:
        return f"""
        ID: {self.id} 
        Title: {self.title}
        Description: {self.description}
        Created: {self.created_at}
        """
    
    #function for category detail page that formats the date to the left of the post title
    def datepublished(self):
        return self.created_at.strftime('%m/%d')

    #override clean function for validator testing
    def clean(self):
        super().clean()
        if (self.updated_at is not None) and (self.updated_at < self.created_at):
            raise ValidationError(
                {'updated_at': "Can't update post before post was created."})

