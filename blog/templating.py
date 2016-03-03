from django import template
from django.utils.safestring import mark_safe
from .models import Tag
import markdown


register = template.Library()


@register.filter("markdown", is_safe=True)
def filter_markdown(inp):
    return mark_safe(markdown.markdown(inp, extensions=["gfm"]))


@register.inclusion_tag("blog/sidebar_tags.html")
def sidebar_tags():
    return {"tags": Tag.objects.all()}


