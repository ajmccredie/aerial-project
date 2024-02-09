from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.http import HttpRequest

# Define the class-based view
class BasketView(View):
    def get(self, request, *args, **kwargs):
        """ A view that renders the bag contents page """
        return render(request, 'basket/basket.html')


class AddToBasketView(View):
    def post(self, request: HttpRequest, item_id: str):
        """ Add a quantity of the specified product to the shopping basket """
        
        quantity = int(request.POST.get('quantity'))
        redirect_url = reverse('view_basket') 
        basket = request.session.get('basket', {})

        weight = 400
        if 'weight' in request.POST:
            weight = request.POST('size')

        if item_id in list(basket.keys()):
            basket[item_id] += quantity
        else:
            basket[item_id] = quantity

        request.session['basket'] = basket
        print(request.POST)
        request.session['basket'] = basket
        request.session.modified = True  # Ensure the session is marked as modified so it gets saved
        print("Updated session basket:", request.session['basket'])

        return redirect(redirect_url)
