from django import template

register = template.Library()

@register.simple_tag
def valuelookup(object, property):
    obj = object.__dict__.get(property)
    if 'datetime' in str(type(obj)):
        return str(obj)[:10]
    if not obj:
        try:
            obj = eval(F'object.{property}.__str__()')
        except Exception:
            obj = None
    return str(obj)
