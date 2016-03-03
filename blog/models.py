from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return "#" + self.name

    def url(self):
        return reverse("blog:tag_detail", kwargs={
            "name": self.name
        })


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    text = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="posts")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def url(self):
        return reverse("blog:detail", kwargs={
            "slug": self.slug,
            "year": str(self.date.year),
            "month": str(self.date.month).zfill(2)
        })

    def approved_comments(self):
        return self.comment_set.filter(approved=True).order_by("-id")


class Comment(models.Model):
    author_name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return "[%s] %s" % (self.author_name, self.text_abbr())

    def text_abbr(self):
        return self.text[0:20]

    text_abbr.short_description = "Text"

