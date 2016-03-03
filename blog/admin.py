from django.contrib import admin
from django.conf.urls import url
from django import forms
from . import models
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from nnscr.markdown import MarkdownWidget
from nnscr.admin import site


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = models.Post
        exclude = ("slug",)
        widgets = {
            "text": MarkdownWidget
        }


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm


class CommentAdmin(admin.ModelAdmin):
    list_display = ("author_name", "text_abbr", "date", "approved")


site.register(models.Post, PostAdmin)
site.register(models.Tag)
site.register(models.Comment, CommentAdmin)
site.add_context("index", "unapproved_comments", models.Comment.objects.filter(approved=False))


def comment_admin(approve):
    @require_http_methods(["POST"])
    def approve_comment(request, pk):
        comment = get_object_or_404(models.Comment, pk=pk)

        if approve:
            comment.approved = True
            comment.save()
        else:
            comment.delete()

        return HttpResponseRedirect(reverse("admin:index"))

    return approve_comment


site.extra_urls.append(url(r'^comment/(?P<pk>[0-9]+)/approve$', comment_admin(True), name="comment_approve"))
site.extra_urls.append(url(r'^comment/(?P<pk>[0-9]+)/delete$', comment_admin(False), name="comment_delete"))
