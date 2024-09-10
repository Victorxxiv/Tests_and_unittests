# test_models.py
import pytest
from .models import BlogPost

@pytest.mark.django_db
def test_blog_post_creation():
    post = BlogPost.objects.create(title="My First Post", content="Hello, world!")
    assert post.title == "My First Post"
    assert post.content == "Hello, world!"