from django import template
from mainapp.models import MenuGroup
from django.http import HttpResponseServerError

register = template.Library()


@register.simple_tag
def draw_menu(name):
    try:
        menu_group = MenuGroup.objects.prefetch_related("menu_items", "logo").get(
            name=name
        )
    except MenuGroup.DoesNotExist:
        return HttpResponseServerError()

    logo = menu_group.logo.get()
    menu_items = menu_group.menu_items.all()

    menu = {
        "logo": {
            "image": logo.image.url,
            "styles": logo.styles,
        },
        "items": [],
        "styles": menu_group.styles,
    }

    for item in menu_items:
        menu["items"].append(
            {
                "text": item.text,
                "url": item.url,
                "styles": item.styles.split(", "),
            }
        )

    return menu


# @register.simple_tag
# def menu(name):
#     menu_group = MenuGroup.objects.prefetch_related("items", "menu_logo").get(
#         name=name
#     )  # makes only one query to the database
#     logo = menu_group.menu_logo.get()
#     menu_items = menu_group.items.all()
#
#     logo_styles = logo.styles
#     menu_html = f"<div style='{menu_group.styles}'>"
#     menu_html += f"<img src='{logo.image.url}' style='{logo_styles}'>"
#     for item in menu_items:
#         item_styles = item.styles
#         menu_html += f"<a href='{item.url}' style='{item_styles}'>{item.text}</a>"
#     menu_html += "</div>"
#     return mark_safe(menu_html)
