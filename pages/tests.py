from django.test import TestCase
from . import models


class PageTest(TestCase):
    def test_slug(self):
        page = models.Page()
        page.title = "Slug me"
        page.save()

        self.assertEqual(models.Page.objects.get(slug="slug-me"), page)

    def test_url(self):
        page = models.Page()
        page.slug = "slug-me"

        self.assertEqual("/pages/slug-me", page.url())
