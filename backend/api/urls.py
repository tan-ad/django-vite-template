from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.ItemListCreate.as_view(), name='item-list-create'),
    path('items/<int:pk>/', views.ItemRetrieveUpdateDestroy.as_view(), name='item-detail'),
    # Add your API endpoint paths here
 ]
