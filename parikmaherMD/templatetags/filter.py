from django import template

register = template.Library()


@register.filter(name='split')
def split(value, key):
    """
      Returns the value turned into a list.
    """
    return value.split(key)


@register.filter(name='opening')
def split_for_time(value, key):
    """
      Returns the value of hairdressing opening.
    """
    return value.split(key)[1]


@register.filter(name='closing')
def split_for_time(value, key):
    """
      Returns the value of hairdressing closing.
    """
    return value.split(key)[2]


@register.filter(name='to_str')
def split_for_time(value):
    """
      Returns the string value of local_time.
    """
    return str(value)
