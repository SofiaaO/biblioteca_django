# templatetags/form_tags.py

from django import template

register = template.Library()

@register.filter
def add_class(value, class_name):
    """Añade una clase a un campo de formulario"""
    if hasattr(value, 'as_widget'):  # Verifica que value sea un campo de formulario
        return value.as_widget(attrs={'class': class_name})
    return value  # Si no es un campo de formulario, retorna el valor original
