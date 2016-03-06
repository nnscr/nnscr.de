from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse


class Page(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    text = models.TextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def url(self):
        return reverse("pages:page", kwargs={"slug": self.slug})
