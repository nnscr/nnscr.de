from django import forms
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from django.forms.utils import flatatt


class MarkdownWidget(forms.Textarea):
    def render(self, name, value, attrs=None):
        value = value or ""
        final_attrs = self.build_attrs(attrs, name=name)
        
        return mark_safe(render_to_string("widget/markdown.html", {"attrs": flatatt(final_attrs), "value": value}))


class MarkdownFormField(forms.CharField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.widget = MarkdownWidget()

