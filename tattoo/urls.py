from django.urls import path

from .views import testview, ProductDetailView

urlpatterns = [
    path('', testview, name='base'),
    path('products/<str:ct_model>/<str:slug>', ProductDetailView.as_view(), name='product_detail')
]
