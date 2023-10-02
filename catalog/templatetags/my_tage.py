from django import template

register = template.Library()


@register.filter()
def product_media(value):
    if value:
        return f'/media/{value}'

    return '#'
