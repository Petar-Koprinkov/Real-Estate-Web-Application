from django import template

register = template.Library()


@register.filter
def placeholder(field_obj, placeholder_message):
    field_obj.field.widget.attrs.update({'placeholder': placeholder_message})
    return field_obj
