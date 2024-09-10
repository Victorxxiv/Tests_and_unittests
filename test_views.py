# test_views.py

import pytest
from django.urls import reverse
from .models import BlogPost

@pytest.mark.django_db
def test_blog_post_list_view(client):
    BlogPost.objects.create(title="My First Post", content="Hello, world!")
    response = client.get(reverse('blog:post_list'))
    assert response.status_code == 200
    assert "My First Post" in response.content.decode()