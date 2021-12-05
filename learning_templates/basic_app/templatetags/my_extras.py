from django import template

register = template.Library()

@register.filter(name='cut')


def cut(value, arg):
    # This cuts all values of "arg" from the string!
    return value.replace(arg,'')

# register.filter('cut',cut)
# Instead of "register.filter(), we can use "@register.filter(name='cut')"