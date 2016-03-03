from django.contrib import admin
from . import models
from nnscr.admin import site


class PageAdmin(admin.ModelAdmin):
    fields = ["title", "text"]

site.register(models.Page, PageAdmin)
