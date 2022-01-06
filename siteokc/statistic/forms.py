from django.contrib.admin.widgets import AdminDateWidget
from django import forms
from .models import *


class StatisticForms(forms.ModelForm):
    class Meta:
        model = Statistic
        fields = ['date', 'number_of_calls', 'subdivisions']
        widgets = {
            'date': AdminDateWidget(attrs={'placeholder': 'Оберіть дату'}),
            'number_of_calls': forms.NumberInput(attrs={'class': 'form-control'}),
            'subdivisions': forms.Select(attrs={'class': 'form-control', 'placeholder': 'help'})
        }


