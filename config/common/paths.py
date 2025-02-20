import pathlib
import typing
import uuid

# Build paths inside the project like this: BASE_DIR / "subdir"
CONFIG_DIR = pathlib.Path(__file__).resolve().parent.parent
BASE_DIR = CONFIG_DIR.parent


def _default_media_path(
    model_instance: typing.Any,
    filename: str,
) -> pathlib.Path:
    """Generate upload path for Django model instance.

    Generates upload path that contain instance's model app, model name,
    object's ID, salt and file name.

    """
    components = model_instance._meta.label_lower.split(".")
    components.append(str(model_instance.id))
    components.append(str(uuid.uuid4()))
    components.append(filename)
    return pathlib.Path(*components)


DEFAULT_MEDIA_PATH = _default_media_path