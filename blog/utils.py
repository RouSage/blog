from django.utils.text import slugify
from django.conf import settings


def get_unique_slug(model_instance, sluggable_field_name, slug_field_name):
    """
    Takes a model instance, sluggable field name (such as 'title') of that
    model as string, slug field name (such as 'slug') of the model as string;
    returns a unique slug as string.
    """
    slug = slugify(getattr(model_instance, sluggable_field_name))
    unique_slug = slug
    extension = 1
    ModelClass = model_instance.__class__

    while ModelClass._default_manager.filter(
        **{slug_field_name: unique_slug}
    ).exists():
        unique_slug = '{}-{}'.format(slug, extension)
        extension += 1
    return unique_slug


def switch_language(path: str, language: str):
    """Switches current language to the selected one

    Arguments:
        path {string} -- Path of the current page
        language {string} -- Language code
    """
    # Get the supported language codes
    lang_codes = [c for (c, name) in settings.LANGUAGES]

    # Validate the inputs
    if path == '':
        raise Exception('URL path for language switch is empty')
    elif path[0] != '/':
        raise Exception('URL path for language switch does not start with "/"')
    elif language not in lang_codes:
        raise Exception('%s is not a supported language code' % language)

    # Split the parts of the path
    parts = path.split('/')

    # Add or substitue the new language prefix
    if parts[1] in lang_codes:
        parts[1] = language
    else:
        parts[0] = '/' + language

    # Return the full new path
    return '/'.join(parts)
