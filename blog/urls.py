from django.conf.urls import include, url
from . import views

app_name = "blog"

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name="list"),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[^/]+)-(?P<pk>[\d+])$', views.PostDetailView.as_view(), name="detail"),
    url(r'^tag/(?P<name>[^/]+)$', views.TagDetailView.as_view(), name="tag_detail"),

    url(r'^post_comment', views.post_comment, name="comment_post"),

    url(r'^licensing$', views.licensing, name="licensing"),
    url(r'^contact$', views.contact, name="contact"),
]
