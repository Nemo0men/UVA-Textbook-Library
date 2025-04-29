from django import template

register = template.Library()

@register.filter(name='is_in_group')
def is_in_group(user, group_name):
    return user.groups.filter(name=group_name).exists()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def truncate_chars(value, max_length):
    if len(value) > max_length:
        return value[:max_length] + '...'
    return value