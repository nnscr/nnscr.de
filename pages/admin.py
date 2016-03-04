from django.contrib import admin
from django import forms
from . import models
from nnmarkdown.form import MarkdownWidget
from nnscr.admin import site


class PageAdminForm(forms.ModelForm):
    class Meta:
        model = models.Page
        exclude = ("slug",)
        widgets = {
            "text": MarkdownWidget
        }


class PageAdmin(admin.ModelAdmin):
    form = PageAdminForm


site.register(models.Page, PageAdmin)
