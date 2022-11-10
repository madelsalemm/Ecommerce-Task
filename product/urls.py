from django.urls import path , include
from . import views
from rest_framework.routers import DefaultRouter
from . import api
############################
router = DefaultRouter()
router.register('', api.ProductViewSet, basename='productViewSet')
############################
app_name = 'product'

urlpatterns = [
    path('',  views.product_list , name="product_list"),
    path('<int:id>',  views.product_details , name= 'product_details' ),
    ############################
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    ############################
    path('product/api/', include(router.urls) , name='postvs'),
]