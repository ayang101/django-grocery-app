from django.urls import path

from myapp.views import ItemCreateView, ItemDeleteView, ReceiptDeleteView
from . import views
from .views import (
    GroupListView,
    GroupCreateView,
    GroupDetailView,
    GroupDeleteView,

    ReceiptListView,
    ReceiptDetailView,
    ReceiptCreateView,
    ReceiptDeleteView,

    ItemListView,
    ItemDetailView,
    ItemCreateView,
    ItemUpdateView,
    ItemDeleteView
    )

urlpatterns = [
    path('', GroupListView.as_view(), name='groups'),
    path('create-group/', GroupCreateView.as_view(), name='create-group'),
    path('<int:pk>/', GroupDetailView.as_view(), name='group-detail'),
    path('<int:pk>/delete', GroupDeleteView.as_view(), name='group-delete'),

    path('receipts/all/', ReceiptListView.as_view(), name='receipts'),
    path('receipts/<int:pk>/', ReceiptDetailView.as_view(), name='receipt-detail'),
    path('receipts/add/', ReceiptCreateView.as_view(), name='add-receipt'),
    path('receipts/<int:pk>/delete/', ReceiptDeleteView.as_view(), name='delete-receipt'),

    path('items/all/', ItemListView.as_view(), name='items'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('items/add/', ItemCreateView.as_view(), name='add-item'),
    path('items/<int:pk>/delete/', ItemDeleteView.as_view(), name='delete-item'),

    # path('home/', name='home'),

    # path('receipts/<int:pk>/items/', ReceiptItemListView.as_view(), name='receipt-items')

]
