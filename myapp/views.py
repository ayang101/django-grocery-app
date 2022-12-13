from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )
from django.views.generic.edit import ModelFormMixin

from .forms import GroupForm, ReceiptForm, ItemForm
from .models import Group, Membership, Receipt, Item, ReceiptItem


class GroupListView(ListView):
    template_name = 'myapp/group_create.html'
    model = Group

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = GroupForm()
        return context

    #def get_queryset(self):
        # Group.objects.filter


class GroupDetailView(DetailView):
    template_name = 'myapp/group_detail.html'
    model = Group
    context_object_name = 'group_detail'


class GroupCreateView(CreateView):
    template_name = 'myapp/group_create.html'
    form_class = GroupForm
    model = Group
    success_url = '/'

    def form_valid(self, form):
        # create a new group
        self.object = form.save(commit=False)
        self.object.save()
        # save each person and add to a list
        for person in form.cleaned_data['members']:
            membership = Membership()
            membership.group = self.object
            membership.person = person
            membership.save()

        return super(ModelFormMixin, self).form_valid(form)


class GroupDeleteView(DeleteView):
    template_name = 'myapp/group_confirm_delete.html'
    model = Group
    success_url = '/'


class ItemListView(ListView):
    template_name = 'myapp/item_create.html'
    model = Item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ItemForm()
        return context


class ReceiptListView(ListView):
    template_name = 'myapp/receipt_create.html'
    model = Receipt

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReceiptForm()
        return context


class ItemDetailView(DetailView):
    template_name = 'myapp/item_detail.html'
    model = Item
    context_object_name = 'item_detail'


class ReceiptDetailView(DetailView):
    template_name = 'myapp/receipt_detail.html'
    model = Receipt
    context_object_name = 'receipt_detail'


class ItemCreateView(CreateView):
    template_name = 'myapp/item_create.html'
    form_class = ItemForm
    model = Item
    success_url = '/items/all'


class ItemUpdateView(UpdateView):
    template_name = 'myapp/item_create.html'
    form_class = ItemForm
    model = Item
    success_url = '/items/all'


class ItemDeleteView(DeleteView):
    template_name = 'myapp/item_confirm_delete.html'
    model = Item
    success_url = '/items/all'


class ReceiptCreateView(CreateView):
    template_name = 'myapp/receipt_create.html'
    form_class = ReceiptForm
    model = Receipt
    success_url = '/receipts/all'

    def form_valid(self, form):
        # create a new receipt
        self.object = form.save(commit=False)
        self.object.save()
        # save each item and add to a list
        for item in form.cleaned_data['items']:
            receiptitem = ReceiptItem()
            receiptitem.receipt = self.object
            receiptitem.item = item
            receiptitem.save()

        return super(ModelFormMixin, self).form_valid(form)


class ReceiptUpdateView(UpdateView):
    template_name = 'myapp/receipt_create.html'
    form_class = ReceiptForm
    model = Receipt
    success_url = '/receipts/all'


class ReceiptDeleteView(DeleteView):
    template_name = 'myapp/receipt_confirm_delete.html'
    model = Receipt
    success_url = '/receipts/all'
