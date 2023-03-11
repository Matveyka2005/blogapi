from django.test import TestCase
from django.contrib.auth.models import User
from posts.models import Post


class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a User
        testuser1 = User.objects.create_user(
            username="testuser1",
            password="123abc"
        )
        testuser1.save()

        # Create a blog post
        post = Post.objects.create(
            author=testuser1,
            title="a title here",
            body="a body here",
        )
        post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f"{post.author}"
        title = f"{post.title}"
        body = f"{post.body}"
        self.assertEqual(author, "testuser1")
        self.assertEqual(title, "a title here")
        self.assertEqual(body, "a body here")

