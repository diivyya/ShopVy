from django.shortcuts import render
from store.models.product import Product
from store.models.category import Category

def index(request):
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_category_id(categoryID)
    else:
        products = Product.get_all_products()
    data = {}
    data['products'] = products
    data['categories'] = categories
    print('you are: ',request.session.get('email'))
    return render(request, 'index.html', data)
