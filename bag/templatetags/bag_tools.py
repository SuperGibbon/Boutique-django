from django import template


register = template.Library()


@register.filter(names='cal_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
