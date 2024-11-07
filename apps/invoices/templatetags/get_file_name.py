import pathlib
from django import template

from .. import models

register = template.Library()


@register.filter
def get_file_name(document: models.Document) -> str:
    """Return string of document's file name."""
    return pathlib.Path(document.file.url).name