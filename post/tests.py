from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text="just a test")
    
    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f"{post.text}"
        self.assertEqual(expected_object_name,"just a test")

class HomePageViewTest(TestCase):
    def setUp(self):
        post.objects.create(text="This is another test")
    
    def test_view_url_exists_at_proper_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
       
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response,"post_list.html")
    
    def test_page_content_contains_post_(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,"This is another test ")
