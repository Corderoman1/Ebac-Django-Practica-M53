from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from ecommerce import views


urlpatterns = [
    path("", views.product_model_list_view, name="Products"),
    path("products/<int:id>/", views.product_model_detail_view, name="ProductDetail"),
    path("products/create/", views.product_model_create_view, name="ProductCreate"),
    path("products/<int:product_id>/update/", views.product_model_update_view, name="ProductUpdate"),
    path("products/<int:product_id>/delete/", views.product_model_delete_view, name="ProductDelete"),
]