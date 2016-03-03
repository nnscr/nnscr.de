from blog.models import Tag
from django import template

register = template.Library()


@register.inclusion_tag("blog/sidebar_tags.html")
def sidebar_tags():
    return {"tags": Tag.objects.all()}
