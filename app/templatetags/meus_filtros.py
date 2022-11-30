from django import template

register = template.Library()

# Filtro para inserir class no form
@register.filter(name='addclass')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})