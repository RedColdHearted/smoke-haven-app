from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from django.db import models
from django.utils.translation import gettext_lazy as _

from imagekit import models as imagekitmodels
from imagekit.processors import ResizeToFill, Transpose

from apps.core.models import BaseModel


class User(
    BaseModel,
    AbstractBaseUser,
    PermissionsMixin,
):
    """Custom user model."""

    username = models.CharField(
        unique=True,
        verbose_name=_("Username"),
        max_length=30,
    )
    first_name = models.CharField(
        verbose_name=_("First name"),
        max_length=30,
        blank=True,
    )
    last_name = models.CharField(
        verbose_name=_("Last name"),
        max_length=30,
        blank=True,
    )
    email = models.EmailField(
        verbose_name=_("Email address"),
        max_length=254,
        unique=True,
    )
    is_active = models.BooleanField(
        verbose_name=_("Active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active.",
        ),
    )
    avatar = imagekitmodels.ProcessedImageField(
        verbose_name=_("Avatar"),
        blank=True,
        null=True,
        upload_to=settings.DEFAULT_MEDIA_PATH,
        max_length=512,
        processors=[Transpose()],
        options={
            "quality": 100,
        },
    )
    avatar_thumbnail = imagekitmodels.ImageSpecField(
        source="avatar",
        processors=[
            ResizeToFill(50, 50),
        ],
    )

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self) -> str:
        return self.username