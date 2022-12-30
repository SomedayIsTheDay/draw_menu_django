from django import template
from mainapp.models import Menu
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag()
def draw_menu():
    return mark_safe(
        """
        <div class="header">
            <a href="#default" class="logo" style="color: red">CompanyLogo</a>
            <div class="header-right">
                <a class="active" href="#home">Home</a>
                <a href="#contact">Contact</a>
                <a href="#about">About</a>
            </div>
        </div>
        """
    )
