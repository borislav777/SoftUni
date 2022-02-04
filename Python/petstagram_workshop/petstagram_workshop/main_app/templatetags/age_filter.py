import datetime

from django import template

register = template.Library()


@register.filter(name='year_to_now')
def year_to_now(pet):
    return datetime.datetime.now().year - pet.date_of_birth.year
