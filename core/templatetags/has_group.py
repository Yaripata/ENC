from django import template
from ..models import Combustibles

register = template.Library() 

@register.filter(name='has_group') 
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists() 

@register.filter(name='has_code') 
def has_code(user, group_name):
    return Combustibles.objects.filter(codigo_combustible=group_name)