from django import template
from kstory.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu.html')
def get_rate(url_path):
    tamil = MenuItem.objects.filter(parent__name="Tamil")
    return {"recs": tamil}
