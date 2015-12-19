from django.db import models
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from ckeditor.fields import RichTextField

class Series(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Series, self).save(*args, **kwargs)

    def get_absolute_url(self):
        pass

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    body = RichTextField()
    posted = models.DateField(auto_now_add=True)
    series = models.ForeignKey(Series)

    def __unicode__(self):
        return str(self.series) + ": " + str(self.title)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = self.series.slug + "-" + slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        unique_together = ('series', 'slug')