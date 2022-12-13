from django import forms
from .models import Group, Receipt, Item


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name',
                  'members']


class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ['store',
                  'total_price',
                  'date_visited',
                  'items'
                  ]
        widgets = {
            'date_visited': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD',
                                                   'required': 'required'}),
            'items': forms.CheckboxSelectMultiple()
        }


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        """exclude = ['receipts']"""
        fields = ['name',
                  'quantity',
                  'price',
                  'category',
                  ]
