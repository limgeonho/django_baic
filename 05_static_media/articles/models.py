from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # upload_to='images/' => images아래에 모을 것임!!!
    image = models.ImageField(blank=True, upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
