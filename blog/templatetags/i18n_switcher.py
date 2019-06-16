from django import template
from django.template.defaultfilters import stringfilter
from blog.utils import switch_language


register = template.Library()


@register.filter(name='switch_i18n_prefix')
@stringfilter
def switch_i18n_prefix(path, language):
    return switch_language(path, language)


@register.filter(name='switch_i18n')
def switch_i18n(request, language):
    return switch_language(request.get_full_path(), language)
