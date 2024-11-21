from django import template
from ..models import Country, State, City, Property, Reservation, PropertyPhoto, User
from django.utils.translation import gettext as _
import unicodedata

register = template.Library()

def normalize_text(text):
    """Normaliza un texto: elimina tildes y convierte 'ñ' a 'n'."""
    return unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf-8')

@register.simple_tag
def search_context():
    cities = City.objects.select_related('state__country').all()

    destination_list = [
        f"{city.name}, {city.state.country.name}"
        for city in cities
    ]

    guests_list = [
        f"{i} {str(_('search_guests_ph'))}"
        for i in range(1, 9)
    ]

    return {
        "destination": {
            "id":"destination",
            "name":"destination",
            "label": _("search_destination"), 
            "placeholder": _("search_destination_ph"), 
            "icon":"svg/search_icon.svg",
        },
        "date": {
            "id":"date",
            "name":"date",
            "label": _("search_date"), 
            "placeholder": _("search_date_ph"), 
            "icon":"svg/calendar_icon.svg",
        },
        "guests": {
            "id":"guests",
            "name":"guests",
            "label": _("search_guests"), 
            "placeholder": _("search_guests_ph"), 
            "icon":"svg/guests_icon.svg",
        },
        "guests_list": guests_list,
        "destination_list": destination_list,
    }

@register.simple_tag
def featured_context():
    properties = Property.objects.filter(status='available').order_by('-stars')[:3]
    return {
        "properties": [
            {
                "name": property.name,
                "location": f"{property.city.name}, {property.city.state.name} ,{property.city.state.country.name}",
                "photos": [f"img/{photo.photo}" for photo in property.photos.all()],
                "cost_per_night": property.cost_per_night,
                "stars": property.stars,
                "capacity": property.capacity,
                "beds": property.beds,
            }
            for property in properties
        ]
    }