from django.test import TestCase
from datetime import datetime

from ..models import Post, Category
from accounts.models import User,Profile

class TestPostModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="test@test.com",password="a/@1234567")
        self.profile = Profile.objects.create(
            user=self.user,
            first_name = "test_first_name",
            last_name = "test_last_name",
            description = "test description",
        )

    def test_create_post_with_valid_data(self):
        
        post = Post.objects.create(
            author = self.profile,
            title = "test",
            content = "description",
            status = True,
            category = None,
            published_date = datetime.now()
        )
        self.assertTrue(Post.objects.filter(pk=post.id).exists())
        self.assertEquals(post.title,"test")
