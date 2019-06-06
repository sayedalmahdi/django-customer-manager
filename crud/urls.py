from django.urls import path

from .views import CustomerListView, CustomerCreateView, CustomerDetailsView, CustomerUpdateView, CustomerDeleteView

app_name = 'crud'
urlpatterns = [
    path('', CustomerListView.as_view(), name='customer-list'),
    path('create/', CustomerCreateView.as_view(), name='customer-create'),
    path('<int:id>/', CustomerDetailsView.as_view(), name='customer-details'),
    path('<int:id>/update/', CustomerUpdateView.as_view(), name='customer-update'),
    path('<int:id>/delete/', CustomerDeleteView.as_view(), name='customer-delete'),
]
