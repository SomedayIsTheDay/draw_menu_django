import re
from django import template
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from mainapp.models import MenuGroup
from django.http import HttpResponseServerError

register = template.Library()


@register.simple_tag
def draw_menu(name):
    try:
        menu_group = MenuGroup.objects.prefetch_related("menu_items").get(name=name)
    except MenuGroup.DoesNotExist:
        return HttpResponseServerError()
    styles = [
        re.sub(r"\r\n|\s\s+", "", style) for style in menu_group.styles.split(",")
    ]

    menu = {"styles": styles}
    return menu
