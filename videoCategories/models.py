from django.db import models
from embed_video.fields import EmbedVideoField


class Categories(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Catgimages/', height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return '{}'.format(self.name)


class Video(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50, default="Unknown")
    video = EmbedVideoField(default=None)
    slug = models.SlugField(max_length=40, null=False)
    thumbnail = models.ImageField(upload_to='thumbnails/', default=None)

    def __str__(self):
        return ' Title - {} || Category - {} '.format(self.title, self.category)
