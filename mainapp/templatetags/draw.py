from django import template
from django.urls import reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from mainapp.models import MenuGroup, Logo
from django.http import HttpResponseServerError

register = template.Library()


def html(menu_items, menu_html):
    for item in menu_items:
        if item.dropdown is False:
            menu_html += format_html(
                '<li><a href="{}" class="{}">{}</a>',
                reverse("any", kwargs={"item": item.name}),
                item.classes,
                item.name,
            )
            if item.dropdown_links.all():
                menu_html += "<ul>"
                for link in item.dropdown_links.all():
                    menu_html += format_html(
                        "<li class='link'><a href='{}' class='{}'>{}</a>",
                        reverse("any2", kwargs={"item": item.name, "link": link.name}),
                        link.classes,
                        link.name,
                    )
                    ul_sub = False
                    for sublink in link.dropdown_links.all():
                        if sublink.dropdown is True:
                            if not ul_sub:
                                menu_html += "<ul>"
                                ul_sub = True
                            menu_html += format_html(
                                "<li class='link'><a href='{}' class='{}'>{}</a></li>",
                                reverse(
                                    "any3",
                                    kwargs={
                                        "item": item.name,
                                        "link": link.name,
                                        "sublink": sublink.name,
                                    },
                                ),
                                sublink.classes,
                                sublink.name,
                            )
                    if len(link.dropdown_links.all()) > 1:
                        menu_html += "</ul>"
                    menu_html += "</li>"
                menu_html += "</ul></li>"
    return menu_html


@register.simple_tag
def draw_menu(name):
    try:
        menu = MenuGroup.objects.prefetch_related("menu_items", "logo").get(name=name)
        logo = menu.logo.get()
    except (MenuGroup.DoesNotExist, Logo.DoesNotExist):
        return HttpResponseServerError()
    menu_items = menu.menu_items.all()
    menu_html = f'<div class="{menu.classes}">'
    menu_html += "<ul sdsd>"
    menu_html += (
        f'<li><img src="{logo.logo.url}" class="{logo.classes}" alt="logo"></li>'
    )

    menu_html = html(menu_items, menu_html)

    menu_html += "</ul></div>"
    return mark_safe(menu_html)
