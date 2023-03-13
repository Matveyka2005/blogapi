from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    title = models.CharField(
        max_length=50,
        default="Заголовок"
    )

    body = models.TextField(
        default="Содержание"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        verbose_name_plural = "Посты"
        verbose_name = "Пост"
        ordering = ["-uploaded_at"]


