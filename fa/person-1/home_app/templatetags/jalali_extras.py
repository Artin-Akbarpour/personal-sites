# jalali_extras.py
from django import template
import jdatetime

register = template.Library()

@register.filter
def to_jalali(value):
    """تبدیل تاریخ میلادی به شمسی"""
    if not value:
        return ""
    try:
        # value باید datetime.date یا datetime.datetime باشد
        return jdatetime.date.fromgregorian(date=value).strftime("%-d %B %Y")
    except Exception:
        return ""
