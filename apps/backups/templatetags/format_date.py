import datetime

from django import template
from django.utils.translation import gettext_lazy as _

register = template.Library()


@register.filter
def format_date(date: datetime.date) -> str:
    current_date = datetime.datetime.now().date()
    if date == datetime.datetime.now().date():
        return _("Today")
    if date == current_date - datetime.timedelta(days=1):
        return _("Yesterday")
    return date