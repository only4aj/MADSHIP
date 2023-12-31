from django.contrib import admin
from django.urls import path
from MADSHIP_APP import views 

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.login, name = 'login'),
    # path('home/', views.home, name = "home"),
    # path("store/", views.store, name = "store"),
    # path("about/", views.about, name = "about"),
    # path("register/", views.register, name = "register"),
    # path("cart/", views.cart, name = "cart"),
    # # path("login/", views.login, name = "login"),
    # path("termsAndCondition/", views.term, name = "term"),
    # path("verification/", views.verification, name = "verification"),
    # path("items1/", views.items1, name = "items1"),
    # path("items2/", views.items2, name = "items2"),
    # path("items3/", views.items3, name = "items3"),
    # path("contact/", views.contact, name = "contact"),
    # path("items4/", views.items4, name = "items4"),
    # path("product/", views.product, name = "product"),
    # path("checkout/", views.checkout, name = "checkout"),
    # path("logout/", views.LogOut, name= "logout")
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('store/', views.store, name='store'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('cart/', views.cart, name='cart'),
    path('termsAndCondition/', views.term, name='term'),
    path('mens_fashion/', views.mens_fashion, name='items1'),
    path('electronics/', views.electronics, name='items2'),
    path('shoes/', views.shoes, name='items3'),
    path('contact/', views.contact, name='contact'),
    path('womens_fashion/', views.womens_fashion, name='items4'),
    path('product_view/', views.product_view, name='product'),
    path('checkout/', views.checkout, name='checkout'),
    path('logout/', views.LogOut, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)