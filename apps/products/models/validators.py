import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_inn(value):
    """Validate inn to ensure it`s correct."""
    if len(value) not in (10, 12):
        raise ValidationError(
            _("INN digits amount should be between 10 and 12."),
        )
    if not value.isdigit():
        raise ValidationError(_("INN should contain digits only."))
    if value.startswith("0"):
        raise ValidationError(_("INN can't starts with 0."))

def validate_bik(value):
    """Validate bik to ensure it`s correct."""
    if len(value) != 9:
        raise ValidationError(_("BIK should contains 9 symbols."))
    if not value.isdigit():
        raise ValidationError(_("BIK should contain digits only."))
    if value[:2] != "04":
        raise ValidationError(_("BIK russian should start with `04`."))

def validate_russian_phone_number(value):
    """Validate russian phone number to ensure it`s correct."""
    value = re.sub(r'[ \-\(\)]', '', value)

    if not re.fullmatch(r'^(\+7|8)\d+$', value):
        raise ValidationError(_("Phone number should start with `+7` or `8`."))
