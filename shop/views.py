from django.shortcuts import get_object_or_404, render
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from shop.models import Category
Category.objects.all()
from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

# Predefined chatbot responses
CHATBOT_RESPONSES = {
    "1": "Option 1 selected: Chatbot says hello!",
    "2": "Option 2 selected: Chatbot provides helpful info.",
    "3": "Option 3 selected: Chatbot gives advice.",
    "4": "Option 4 selected: Chatbot shares a fun fact.",
    "5": "Option 5 selected: Chatbot tells a joke!",
    "hello": "Hello! How can I assist you today?",
    "help": "I'm here to help! Please ask me any questions.",
    "bye": "Goodbye! Have a great day!",
}

def chatbot_response(request):
    if request.method == "POST":
        selected_option = request.POST.get("option")
        response = CHATBOT_RESPONSES.get(selected_option.lower(), "I'm sorry, I didn't understand that.")
        return JsonResponse({"message": response})
    return JsonResponse({"error": "Invalid request"}, status=400)

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(
        request,
        'shop/product/list.html',
        {
            'category': category,
            'categories': categories,
            'products': products
        }
    )

def product_detail(request, id, slug):
    product = get_object_or_404(
        Product, id=id, slug=slug, available=True
    )
    cart_product_form = CartAddProductForm()
    return render(
        request,
        'shop/product/detail.html',
        {'product': product, 'cart_product_form': cart_product_form}
    )

# class SearchResultsView(TemplateView):
    template_name = 'search_results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')

        if query:
            # Search in Product fields
            product_results = Product.objects.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(category__name__icontains=query)
            )
            # Search in Category fields
            category_results = Category.objects.filter(
                Q(name__icontains=query)
            )
        else:
            product_results = Product.objects.none()
            category_results = Category.objects.none()

        # Add results to context
        context['query'] = query
        context['product_results'] = product_results
        context['category_results'] = category_results

        return context
class SearchResultsView(ListView):
    model = Product
    template_name = 'shop/search_results.html'  # Update if the path is different

    def get_queryset(self):
        query = self.request.GET.get('q')
        self.query = query  # To pass the query to the template

        # Use Q objects to filter by product name or category
        if query:
            return Product.objects.filter(
                Q(name__icontains=query) | Q(category__name__icontains=query)
            )
        else:
            return Product.objects.none()  # Return an empty queryset if no query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query  # Pass the search query to the template context
        return context


def category_products(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = category.products.all()  # Get products related to this category
    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'shop/product/category_products.html', context)

def category_products(request, category_id):
    # Retrieve the category using the category_id
    category = get_object_or_404(Category, id=category_id)
    # Get the products related to this category
    products = category.products.all()

    # Pass the category and products to the template
    return render(request, 'shop/product/category_products.html', {
        'category': category,
        'products': products
    })

def ocassion(request):
    categories = Category.objects.all()  # Ensure you retrieve categories
    return render(request, 'shop/ocassion.html', {'categories': categories})

def relation(request):
    categories = Category.objects.all()  # Ensure you are retrieving categories
    return render(request, 'shop/relation.html', {'categories': categories})

def coming_soon(request):
    return render(request, 'shop/coming_soon.html')

def city_page(request, city):
    template_mapping = {
        'new_york': 'shop/new_york.html',
        'los_angeles': 'shop/los_angeles.html',
        'chicago': 'shop/chicago.html',
        'houston': 'shop/houston.html',
        'miami': 'shop/miami.html',
    }
    template_name = template_mapping.get(city, 'shop/default_city.html')
    return render(request, template_name, {'city': city})


def privacy_policy(request):
    return render(request, 'shop/privacy-policy.html')

def refund_policy(request):
    return render(request, 'shop/refund_policy.html')

def shipping_policy(request):
    return render(request, 'shop/shipping_policy.html')

def terms_and_conditions(request):
    return render(request, 'shop/terms_and_conditions.html')

def wedding(request):
    return render(request, 'shop/wedding.html')

def reception(request):
    return render(request, 'shop/reception.html')

def birthday(request):
    return render(request, 'shop/birthday.html')

def festival(request):
    return render(request, 'shop/festival.html')

def christmas(request):
    return render(request, 'shop/christmas.html')

def ospicious(request):
    return render(request, 'shop/ospicious.html')

def contact(request):
    return render(request, 'shop/contact.html')

# def chatbot(request):
#     return render(request, 'shop/chatbot.html')

def reception(request):
    categories = Category.objects.all()  # Ensure this is correctly fetching categories
    return render(request, 'shop/reception.html', {'categories': categories})

from django.shortcuts import render

def chatbot(request):
    context = {
        "deepseek_api_key": "sk-220b8b1a649746da90ce97c0612f2986"  # Replace with actual API key
    }
    return render(request, "shop/chatbot.html", context)

# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json

# # Define a sample menu structure
# MENU_OPTIONS = {
#     "main": {"message": "Welcome! Choose an option:", "options": ["1. Order Food", "2. Contact Support"]},
#     "1": {"message": "Choose a dish:", "options": ["1. Pizza", "2. Burger", "3. Pasta"]},
#     "2": {"message": "Contact support at support@example.com", "options": []},
#     "1.1": {"message": "Pizza ordered! Would you like anything else?", "options": ["1. Yes", "2. No"]},
# }

# @csrf_exempt
# def chatbot_api(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         user_input = data.get("user_input", "main")
#         response = MENU_OPTIONS.get(user_input, {"message": "Invalid option, try again!", "options": []})
#         return JsonResponse(response)
#     return JsonResponse({"message": "Send a POST request with user_input."})
