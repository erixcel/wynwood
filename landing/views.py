from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import translation
from django.utils.translation import gettext as _
from django.views.generic import TemplateView
from django.conf import settings

def change_i18n(request):
    lang_code = request.GET.get('language')
    if lang_code in dict(settings.LANGUAGES).keys():
        translation.activate(lang_code)
        response = redirect(request.META.get('HTTP_REFERER', '/'))
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
        return response
    else:
        return redirect(request.META.get('HTTP_REFERER', '/'))

def index(request):
    return render(request, 'index.html')