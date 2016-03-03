from django.conf.urls import include, url
from . import views

app_name = "pages"

urlpatterns = [
    url(r'^(?P<slug>[^/]+)$', views.page, name="page"),
]
