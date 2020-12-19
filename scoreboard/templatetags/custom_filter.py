from django import template

register = template.Library()

@register.filter(name='add')
def add(number,number1):
    return number + number1