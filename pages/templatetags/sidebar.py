from django import template
from ..models import Page
register = template.Library()


@register.inclusion_tag("blog/sidebar_pages.html")
def sidebar_pages():
    return {"pages": Page.objects.all()}
