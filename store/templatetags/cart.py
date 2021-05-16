from django import template

register = template.Library()

@register.filter(name="is_in_cart")
def is_in_cart(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False

@register.filter(name="product_count")
def product_count(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart[id]
    return 0