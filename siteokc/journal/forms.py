from django.contrib.admin.widgets import AdminTimeWidget, AdminSplitDateTime
from django.forms import Select
from .models import *
from django import forms


class JournalFormsEdit(forms.Form):
    date_of_receipt_message = forms.SplitDateTimeField(widget=
                                                       AdminSplitDateTime(attrs={'placeholder': 'Оберіть дату та час'}),
                                                       label='Отримання (передача) повідомлення')
    region = forms.ModelChoiceField(queryset=Region.objects.all(),
                                    label='Район',
                                    empty_label='Оберіть район',
                                    widget=Select(attrs={'class': 'form-control'}))

    city = forms.ModelChoiceField(queryset=City.objects.all(),
                                  label='Територіальна громада',
                                  empty_label='Оберіть територіальну громаду',
                                  widget=Select(attrs={'class': 'form-control'}))
    town = forms.ModelChoiceField(queryset=Town.objects.all(),
                                  label='Населений пункт',
                                  empty_label='Оберіть населений пункт',
                                  widget=Select(attrs={'class': 'form-control'}))

    information = forms.CharField(max_length=2000,
                                  widget=forms.Textarea(attrs={'class': 'form-control',
                                                               'placeholder': 'Інформація про обстановку на місці події'}),
                                  label='Інформація про подію')
    subdivisions = forms.CharField(max_length=2000,
                                   widget=forms.Textarea(attrs={'class': 'form-control',
                                                                'placeholder': 'Підрозділи (відділення), що виїхали на місце події'}),
                                   label='Підрозділ')
    quantity_peoples = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                          'placeholder': 'Кількість особового складу'}),
                                          label='Кількість о.с')
    quantity_technics = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                           'placeholder': 'Кількість одиниць техніки'}),
                                           label='Кількість од.тех.')
    departure_date = forms.TimeField(widget=AdminTimeWidget(), label='Час виїзду',
                                     required=False)

    time_of_arrival_to_the_place = forms.TimeField(widget=AdminTimeWidget(), label='Час прибуття до місця',
                                                   required=False)

    barrel_feed_time = forms.TimeField(widget=AdminTimeWidget(), label='Час подачі першого ствола на гасіння',
                                       required=False)

    area = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}),
                            label='Площа пожежі(м2)', required=False)
    localization_time = forms.TimeField(widget=AdminTimeWidget(), label='Час локалізації', required=False)

    area2 = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}),
                             label='Площа пожежі(м2)', required=False)

    liquidation_time = forms.TimeField(widget=AdminTimeWidget(), label='Час ліквідації', required=False)
    liquidation = forms.BooleanField(widget=forms.CheckboxInput(), label='Ліквідовано', required=False)

    quantity_rescued = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                          label='Кількість врятованих')
    quantity_rescued_kids = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                               label='Дітей')

    quantity_victims = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                          label='Кількість постраждалих')
    quantity_victims_kids = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                               label='Дітей')

    quantity_dead = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                       label='Кількість загиблих')
    quantity_dead_kids = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                            label='Дітей')

    quantity_ammunition = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                             label='Кількість знищених боеприпасів')

    violated_conditions = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                             label='Порушено умови життєдіяльності осіб')

    quantity_objects = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                          label="Кількість замінованих об'єктів")

    time_return_to_location = forms.TimeField(widget=AdminTimeWidget(),
                                              label='час повернення до місця розташування',
                                              required=False)

    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      label='Категорія події',
                                      empty_label='Оберіть категорію',
                                      widget=Select(attrs={'class': 'form-control'}))

    type_of_fire = forms.ModelChoiceField(queryset=FireType.objects.all(),
                                          label='Тип події',
                                          empty_label='Оберіть тип',
                                          widget=Select(attrs={'class': 'form-control'}))

    subtype = forms.ModelChoiceField(queryset=Subtype.objects.all(),
                                     required=False,
                                     label='Підтип',
                                     empty_label='Оберіть підтип',
                                     widget=Select(attrs={'class': 'form-control'}))


class JournalFormsAdd(forms.Form):
    date_of_receipt_message = forms.SplitDateTimeField(widget=
                                                       AdminSplitDateTime(attrs={'placeholder': 'Оберіть дату та час'}),
                                                       label='Отримання (передача) повідомлення')
    region = forms.ModelChoiceField(queryset=Region.objects.all(),
                                    label='Район',
                                    empty_label='Оберіть район',
                                    widget=Select(attrs={'class': 'form-control'}))

    city = forms.ModelChoiceField(queryset=City.objects.all(),
                                  label='Територіальна громада',
                                  empty_label='Оберіть територіальну громаду',
                                  widget=Select(attrs={'class': 'form-control'}))
    town = forms.ModelChoiceField(queryset=Town.objects.all(),
                                  label='Населений пункт',
                                  empty_label='Оберіть населений пункт',
                                  widget=Select(attrs={'class': 'form-control'}))

    information = forms.CharField(max_length=2000,
                                  widget=forms.Textarea(attrs={'class': 'form-control',
                                                               'placeholder': 'Інформація про обстановку на місці події'}),
                                  label='Інформація про подію')
    subdivisions = forms.CharField(max_length=2000,
                                   widget=forms.Textarea(attrs={'class': 'form-control',
                                                                'placeholder': 'Підрозділи (відділення), що виїхали на місце події'}),
                                   label='Підрозділ')
    quantity_peoples = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                          'placeholder': 'Кількість особового складу'}),
                                          label='Кількість о.с')
    quantity_technics = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                           'placeholder': 'Кількість одиниць техніки'}),
                                           label='Кількість од.тех.')

    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      label='Категорія',
                                      empty_label='Оберіть категорію',
                                      widget=Select(attrs={'class': 'form-control'}))

    type_of_fire = forms.ModelChoiceField(queryset=FireType.objects.all(),
                                          label='Тип',
                                          empty_label='Оберіть тип',
                                          widget=Select(attrs={'class': 'form-control'}))

    subtype = forms.ModelChoiceField(queryset=Subtype.objects.all(),
                                     label='Підтип',
                                     empty_label='Оберіть підтип',
                                     required=False,
                                     widget=Select(attrs={'class': 'form-control'}))


class NoFireFormsEdit(forms.Form):
    date_of_receipt_message = forms.SplitDateTimeField(widget=AdminSplitDateTime(),
                                                       label='Отримання (передача) повідомлення')
    information = forms.CharField(max_length=2000,
                                  widget=forms.Textarea(attrs={'class': 'form-control'}),
                                  label='Інформація про подію')
    subdivisions = forms.CharField(max_length=2000,
                                   widget=forms.Textarea(attrs={'class': 'form-control'}),
                                   label='Підрозділ')
    departure_date = forms.TimeField(widget=AdminTimeWidget(), label='час виїзду',
                                     required=False)
    time_of_arrival_to_the_place = forms.TimeField(widget=AdminTimeWidget(), label='час прибуття до місця',
                                                   required=False)
    time_return_to_location = forms.TimeField(widget=AdminTimeWidget(),
                                              label='час повернення до місця розташування',
                                              required=False)


class NoFireFormsAdd(forms.Form):
    date_of_receipt_message = forms.SplitDateTimeField(widget=AdminSplitDateTime(attrs={'placeholder': 'Оберіть дату та час'}),
                                                       label='Отримання (передача) повідомлення')
    information = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                               'placeholder': 'Інформація про обстановку на місці події'}),
                                  label='Інформація про подію')
    subdivisions = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                                'placeholder': 'Підрозділи (відділення), що виїхали на місце події'}),
                                   label='Підрозділ')
    departure_date = forms.TimeField(widget=AdminTimeWidget(), label='Час виїзду', required=False, initial='00:00')
    time_of_arrival_to_the_place = forms.TimeField(widget=AdminTimeWidget(),
                                                   label='Час прибуття до місця',
                                                   required=False,
                                                   initial='00:00')
    time_return_to_location = forms.TimeField(widget=AdminTimeWidget(),
                                              label='Час повернення до місця розташування',
                                              required=False,
                                              initial='00:00')


class DepartureStatisticsForm(forms.Form):
    start_datetime = forms.SplitDateTimeField(label="З якої дати",
                                              widget=AdminSplitDateTime(attrs={'placeholder': 'Оберіть з якої дати та часу'}))
    end_datetime = forms.SplitDateTimeField(label="По яку дату",
                                            widget=AdminSplitDateTime(attrs={'placeholder': 'Оберіть з якої дати та часу'}))


class OperativeJournalDateRangeForm(forms.Form):
    start_datetime = forms.SplitDateTimeField(label="З якої дати",
                                              widget=AdminSplitDateTime(attrs={'placeholder': 'Оберіть з якої дати та часу'}))
    end_datetime = forms.SplitDateTimeField(label="По яку дату",
                                            widget=AdminSplitDateTime(attrs={'placeholder': 'Оберіть по яку дату та час'}))
