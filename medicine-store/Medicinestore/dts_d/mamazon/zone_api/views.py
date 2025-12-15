from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# temporary in-memory list
products = [
    {"name": "iPhone 15", "price": 120000, "category": "Electronics"},
    {"name": "Nike Air Max", "price": 8500, "category": "Footwear"},
    {"name": "Thalapathy T-Shirt", "price": 499, "category": "Clothing"},
]

@api_view(['GET','POST'])
def product_list(request):
    if request.method == 'GET':
        return Response(products)

    elif request.method == 'POST':
        new_product = request.data
        products.append(new_product)
        return Response(new_product, status=status.HTTP_201_CREATED)