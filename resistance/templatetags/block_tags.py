from datetime import datetime
from django import template

register = template.Library()


@register.simple_tag(takes_context=False)
def timestamp():
    dt = datetime.now()
    ts = dt.microsecond
    return str(ts)
