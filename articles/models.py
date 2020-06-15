from django.db import models
# from account.models import User
# Create your models here.
# article name, article description, images, tags, category .

class Article(models.Model):
    """Model definition for Article."""

    UserInfo = models.ForeignKey('account.User', default=1 , on_delete=models.CASCADE)
    name = models.CharField(blank=False,max_length=100)
    description = models.TextField()
    tags = models.CharField(max_length=500)
    category = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='articleImage')

    class Meta:
        """Meta definition for Article."""

        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        """Unicode representation of Article."""
        return self.name

    def get_absolute_url(self):
        """Return absolute url for Article."""
        return ('')

    def clean_tags(self):
        return self.tags.split(',')
