from django import forms
from .models import Group, Receipt, Item

ITEM_CATEGORIES = [
    ('', 'select'),
    ('vegetables', 'Vegetables'),
    ('dairy', 'Dairy'),
    ('grains', 'Grains'),
    ('meats', 'Meats'),
    ('fruits', 'Fruits'),
    ('drinks', 'Drinks'),
    ('frozen', 'Frozen'),
    ('baking', 'Baking'),
    ('snacks', 'Snacks'),
    ('condiments', 'Condiments'),
    ('canned goods', 'Canned goods'),
    ('other', 'Other')
]


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name',
                  'members']


class ReceiptForm(forms.ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'

    class Meta:
        model = Receipt
        fields = ['store',
                  'total_price',
                  'date_visited',
                  'items'
                  ]
        widgets = {
            'date_visited': forms.DateInput(attrs={
                'placeholder': 'YYYY-MM-DD',
                'required': 'required'}),
            'items': forms.CheckboxSelectMultiple()
        }


class ItemForm(forms.ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'

    class Meta:
        model = Item
        fields = ['name',
                  'quantity',
                  'price',
                  'category',
                  ]
        widgets = {
            'name': forms.TextInput(attrs={
                'style': 'width:200px;',
                'placeholder': 'Name',
                'required': 'required'
            }),
            'quantity': forms.NumberInput(attrs={
                'min': '0',
                'style': 'width:200px;',
                'placeholder': 'Quantity',
                'required': 'required'
            }),
            'price': forms.NumberInput(attrs={
                'min': '0',
                'style': 'width:200px;',
                'placeholder': 'Price',
                'required': 'required'
            }),
            'category': forms.Select(
                choices=ITEM_CATEGORIES
            )
        }
