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

@register.filter(name="price_total")
def price_total(product, cart):
    return product.price * product_count(product, cart)

@register.filter(name="order_total")
def order_total(products, cart):
    sum = 0
    for product in products:
        sum = sum + price_total(product,cart)
    return sum

    