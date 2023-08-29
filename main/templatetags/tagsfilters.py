import os
from django import template
from config.settings import BASE_DIR


register = template.Library()


@register.filter()
def absolute_path(value):
    return f'/media/{value}'


@register.simple_tag
def abspth(value):
    return f'/media/{value}'
