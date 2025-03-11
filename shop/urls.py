from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('refund-policy/', views.refund_policy, name='refund_policy'),
    path('shipping-policy/', views.shipping_policy, name='shipping_policy'),
    path('terms-and-conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('wedding/', views.wedding, name='wedding'),
    path('reception/', views.reception, name='reception'),
    path('birthday/', views.birthday, name='birthday'),
    path('festival/', views.festival, name='festival'),
    path('christmas/', views.christmas, name='christmas'),
    path('ospicious/', views.ospicious, name='ospicious'),
    path('ocassion/', views.ocassion, name='ocassion'),
    path('relation/', views.relation, name='relation'),
    path('', views.product_list, name='product_list'),
    path('coming-soon/', views.coming_soon, name='coming_soon'),
    path("search/", views.SearchResultsView.as_view(), name="search_results"),
    path('city/<str:city>/', views.city_page, name='city_page'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('category/<int:category_id>/', views.category_products, name='category_products'),
    path('chatbot/', views.chatbot, name='chatbot'),  # Chatbot UI page
    path('chatbot-response/', views.chatbot_response, name='chatbot_response'),  # API for chatbot replies
]
