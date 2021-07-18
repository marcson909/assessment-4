from django.test import TestCase
from .models import Category, Post
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta

class CategoryTestCase(TestCase):

    category = Category()

    def test_01_validate_category_name_presence(self):
        """validates presence of category_name"""
        try:
            self.category.full_clean()
        except ValidationError as e:
            self.assertTrue('This field cannot be blank.' in e.message_dict['name'])

class PostTestCase(TestCase):
    post = Post()

    def test_01_validate_post_title_presence(self):
        """validates presence of post_title"""
        try:
            self.post.full_clean()
        except ValidationError as e:
            self.assertTrue('This field cannot be blank.' in e.message_dict['title'])

    def test_02_validate_post_desc_prescence(self):
        "validates presence of post_description"
        try:
            self.post.full_clean()
        except ValidationError as e:
            self.assertTrue('This field cannot be blank.' in e.message_dict['description'])

    def test_03_validate_post_created_at(self):
        "validates post created date is not in future"
        bad_date = timezone.now() + timedelta(days=1)
        category = Category(name='Test')
        post = Post(created_at=bad_date, category=category)
        try:
            post.full_clean()
        except ValidationError as e:
            self.assertTrue("Can't create post in the future." in e.message_dict['created_at'])

    def test_04_validate_updated_after_created(self):
        """does not allow updated to be set before created"""
        c1 = Category(name='Test')
        c1.save()
        post = Post(title="t", description="t",created_at=timezone.now(), updated_at=timezone.now() - timedelta(days=1), category=c1)
        post.save()
        try:
            post.full_clean()
        except ValidationError as e:
            self.assertTrue("Can't update post before post was created." in e.message_dict['updated_at'])
