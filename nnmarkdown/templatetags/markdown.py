from django import template
from django.utils.safestring import mark_safe
import markdown

register = template.Library()


@register.filter("markdown", is_safe=True)
def filter_markdown(inp, args=None):
    """
    Renders string to markdown

    :param inp: string
    :param args: None or "safe", which will escape suspicious HTML tags.
    :return: SafeString
    """
    safe = True

    if args == "safe":
        safe = False

    return mark_safe(markdown.markdown(inp, extensions=["fenced_code", "codehilite(linenums=yes)", "gfm"],
                                       safe_mode="escape" if safe else False,
                                       enable_arguments=not safe))
