import re
from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import translation
from django.utils.translation import gettext as _
from django.views.generic import TemplateView
from django.conf import settings
from django.utils.text import slugify

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


def redirect_external(request):
    destination = request.GET.get('destination', '')
    date = request.GET.get('date', '')
    guests = request.GET.get('guests', '')

    destination_parsed = slugify(destination, allow_unicode=False)

    guests_parsed = re.sub(r'\D', '', guests)
    guests_parsed = guests_parsed if guests_parsed else "1"

    if " - " in date:
        date_start, date_end = date.split(" - ")
        date_start = re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\3-\2-\1', date_start.strip())
        date_end = re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\3-\2-\1', date_end.strip())
    else:
        date_start = ""
        date_end = ""

    url_external = f"https://wynwood-house.com/madrid-espana/?guests={guests_parsed}&check_in={date_start}&check_out={date_end}&city={destination_parsed}"
    
    return redirect(url_external)
