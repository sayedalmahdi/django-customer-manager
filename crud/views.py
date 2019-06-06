# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .models import Customer
from .forms import CustomerForm


class CustomerListView(ListView):
    template_name = 'customers/customer_list.html'
    queryset = Customer.objects.all()


class CustomerCreateView(CreateView):
    template_name = 'customers/customer_create.html'
    form_class = CustomerForm
    queryset = Customer.objects.all()


class CustomerDetailsView(DetailView):
    template_name = 'customers/customer_details.html'
    queryset = Customer.objects.all()

    def get_object(self, queryset=None):
        return get_object_or_404(Customer, id=self.kwargs.get('id'))


class CustomerUpdateView(UpdateView):
    template_name = 'customers/customer_update.html'
    form_class = CustomerForm
    queryset = Customer.objects.all()

    def get_object(self, queryset=None):
        return get_object_or_404(Customer, id=self.kwargs.get('id'))


class CustomerDeleteView(DeleteView):
    template_name = 'customers/customer_delete.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Customer, id=self.kwargs.get('id'))

    def get_success_url(self):
        return reverse('crud:customer-list')


def about_page(request):
    return render(request, 'about.html')
