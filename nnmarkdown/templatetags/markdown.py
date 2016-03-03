from django import template
from django.utils.safestring import mark_safe
import markdown


register = template.Library()


@register.filter("markdown", is_safe=True)
def filter_markdown(inp):
    return mark_safe(markdown.markdown(inp, extensions=["gfm"]))


