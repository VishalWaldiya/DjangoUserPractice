from django.db import models

class ArticleFeed(models.Model):
    title = models.CharField(null=True,blank=False, max_length=50)
    # image = models.ImageField(upload_to='image/', blank=True, null=True)
    content = models.TextField(blank=False, max_length=5000)
    category = models.CharField(blank=False, max_length=500)

    class Meta:
        verbose_name = "ArticleFeed"
        verbose_name_plural = "ArticleFeeds"
