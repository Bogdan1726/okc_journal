from datetime import datetime, timedelta
from babel.dates import format_datetime
from django.contrib import messages
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.http import HttpResponseNotFound
from django.views.generic import ListView
from .forms import *
from django.shortcuts import render, redirect
from .models import *
from django.utils import timezone


# Create your views here.

# def dinamic_journal(request):
#     print('ok')
#     queryset = Journal.objects.filter(
#         date_of_receipt_message__range=[
#             f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
#             f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59']
#     )
#     context = {
#         'journal': queryset
#     }
#     return render(request, 'journal/index.html', context)

class OperativeJournal(ListView):
    """
    Home page
    """
    model = Journal
    template_name = 'journal/index.html'
    context_object_name = 'journal'
    type_of_fire = FireType.objects.all()

    def get_context_data(self, **kwargs):
        context = super(OperativeJournal, self).get_context_data(**kwargs)
        context['title'] = 'Оперативні виїзди'
        context['type'] = self.type_of_fire
        context['form_add'] = JournalFormsAdd()
        context['form_date_range'] = OperativeJournalDateRangeForm()
        context['page1'] = format_datetime(datetime.today() - timedelta(days=1), "dd.MM")
        context['page2'] = format_datetime(datetime.today() - timedelta(days=2), "dd.MM")
        context['page3'] = format_datetime(datetime.today() - timedelta(days=3), "dd.MM")
        return context

    def get_queryset(self):
        return Journal.objects.filter(
            date_of_receipt_message__range=[f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                                            f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59']).order_by(
            '-date_of_receipt_message')

    def render_to_response(self, context, **response_kwargs):
        if self.request.user.is_authenticated:
            return super(OperativeJournal, self).render_to_response(context, **response_kwargs)
        else:
            messages.warning(self.request, 'Схоже ви намагаєтеся зайти Не Авторизувавшись')
            return redirect('login')



class OperativeJournal1(ListView):
    """
    journal page 1
    """
    model = Journal
    template_name = 'journal/page1.html'
    context_object_name = 'journal'
    type_of_fire = FireType.objects.all()

    def get_context_data(self, **kwargs):
        context = super(OperativeJournal1, self).get_context_data(**kwargs)
        context['title'] = 'Оперативні виїзди'
        context['type'] = self.type_of_fire
        context['form_add'] = JournalFormsAdd()
        context['form_date_range'] = OperativeJournalDateRangeForm()
        context['page1'] = format_datetime(datetime.today() - timedelta(days=1), "dd.MM")
        context['page2'] = format_datetime(datetime.today() - timedelta(days=2), "dd.MM")
        context['page3'] = format_datetime(datetime.today() - timedelta(days=3), "dd.MM")
        return context

    def get_queryset(self):
        return Journal.objects.filter(
            date_of_receipt_message__range=[f'{format_datetime(datetime.today() - timedelta(days=1), "Y-MM-dd")} 00:00',
                                            f'{format_datetime(datetime.today() - timedelta(days=1), "Y-MM-dd")} 23:59']).order_by(
            '-date_of_receipt_message')

    def render_to_response(self, context, **response_kwargs):
        if self.request.user.is_authenticated:
            return super(OperativeJournal1, self).render_to_response(context, **response_kwargs)
        else:
            messages.warning(self.request, 'Схоже ви намагаєтеся зайти Не Авторизувавшись')
            return redirect('login')


class OperativeJournal2(ListView):
    """
    journal page 2
    """
    model = Journal
    template_name = 'journal/page2.html'
    context_object_name = 'journal'
    type_of_fire = FireType.objects.all()

    def get_context_data(self, **kwargs):
        context = super(OperativeJournal2, self).get_context_data(**kwargs)
        context['title'] = 'Оперативні виїзди'
        context['type'] = self.type_of_fire
        context['form_add'] = JournalFormsAdd()
        context['form_date_range'] = OperativeJournalDateRangeForm()
        context['page1'] = format_datetime(datetime.today() - timedelta(days=1), "dd.MM")
        context['page2'] = format_datetime(datetime.today() - timedelta(days=2), "dd.MM")
        context['page3'] = format_datetime(datetime.today() - timedelta(days=3), "dd.MM")

        return context

    def get_queryset(self):
        return Journal.objects.filter(
            date_of_receipt_message__range=[f'{format_datetime(datetime.today() - timedelta(days=2), "Y-MM-dd")} 00:00',
                                            f'{format_datetime(datetime.today() - timedelta(days=2), "Y-MM-dd")} 23:59']).order_by(
            '-date_of_receipt_message')

    def render_to_response(self, context, **response_kwargs):
        if self.request.user.is_authenticated:
            return super(OperativeJournal2, self).render_to_response(context, **response_kwargs)
        else:
            messages.warning(self.request, 'Схоже ви намагаєтеся зайти Не Авторизувавшись')
            return redirect('login')


class OperativeJournal3(ListView):
    """
    journal page 3
    """
    model = Journal
    template_name = 'journal/page3.html'
    context_object_name = 'journal'
    type_of_fire = FireType.objects.all()

    def get_context_data(self, **kwargs):
        context = super(OperativeJournal3, self).get_context_data(**kwargs)
        context['title'] = 'Оперативні виїзди'
        context['type'] = self.type_of_fire
        context['form_add'] = JournalFormsAdd()
        context['form_date_range'] = OperativeJournalDateRangeForm()
        context['page1'] = format_datetime(datetime.today() - timedelta(days=1), "dd.MM")
        context['page2'] = format_datetime(datetime.today() - timedelta(days=2), "dd.MM")
        context['page3'] = format_datetime(datetime.today() - timedelta(days=3), "dd.MM")
        return context

    def get_queryset(self):
        return Journal.objects.filter(
            date_of_receipt_message__range=[f'{format_datetime(datetime.today() - timedelta(days=3), "Y-MM-dd")} 00:00',
                                            f'{format_datetime(datetime.today() - timedelta(days=3), "Y-MM-dd")} 23:59']).order_by(
            '-date_of_receipt_message')

    def render_to_response(self, context, **response_kwargs):
        if self.request.user.is_authenticated:
            return super(OperativeJournal3, self).render_to_response(context, **response_kwargs)
        else:
            messages.warning(self.request, 'Схоже ви намагаєтеся зайти Не Авторизувавшись')
            return redirect('login')


def filter_date_range(request):
    if request.method == 'POST':
        form = OperativeJournalDateRangeForm(request.POST)
        if form.is_valid():
            start_datetime = format_datetime(form.cleaned_data['start_datetime'], "Y-MM-dd H:mm")
            end_datetime = format_datetime(form.cleaned_data['end_datetime'], "Y-MM-dd H:mm")
            context = {
                'title': 'Оперативні виїзди',
                'page1': format_datetime(datetime.today() - timedelta(days=1), "dd.MM"),
                'page2': format_datetime(datetime.today() - timedelta(days=2), "dd.MM"),
                'page3': format_datetime(datetime.today() - timedelta(days=3), "dd.MM"),
                'start_datetime': format_datetime(form.cleaned_data['start_datetime'],
                                                  "EEEE  d MMMM Y року H:mm", locale='uk_UA'),
                'end_datetime': format_datetime(form.cleaned_data['end_datetime'],
                                                "EEEE  d MMMM Y року H:mm", locale='uk_UA'),
                'journal': Journal.objects.filter(date_of_receipt_message__range=[start_datetime, end_datetime]),
                'form_date_range': OperativeJournalDateRangeForm()
            }

            return render(request, 'journal/filter_date_range.html', context)
        else:
            return redirect('journal')


def add_journal(request):
    if request.method == 'POST':
        form = JournalFormsAdd(request.POST)
        if form.is_valid():
            Journal.objects.create(**form.cleaned_data,
                                   quantity_departure=Journal.objects.filter(
                                       date_of_receipt_message__range=[
                                           f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                                           f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59']).count() + 1,
                                   add_user=f'{request.user.first_name}\n'
                                            f'{request.user.last_name}')
            messages.success(request, f'Запис додано користувачем: {request.user.username}')
            return redirect('journal')
        else:
            messages.warning(request, 'Помилка при передачі інформації')
            return redirect('journal')

    else:
        messages.warning(request, 'Помилка при передачі інформації')
        return redirect('journal')


def edit_journal(request, id):
    if request.user.groups.filter(name="Окц").exists() or \
            Journal.objects.filter(id=id,
                                   add_user=f'{request.user.first_name}\n'
                                            f'{request.user.last_name}').exists():
        try:
            journal = Journal.objects.get(id=id)
            queryset = {'date_of_receipt_message': journal.date_of_receipt_message,
                        'information': journal.information,
                        'region': journal.region,
                        'city': journal.city,
                        'town': journal.town,
                        'subdivisions': journal.subdivisions,
                        'quantity_peoples': journal.quantity_peoples,
                        'quantity_technics': journal.quantity_technics,
                        'departure_date': journal.departure_date,
                        'time_of_arrival_to_the_place': journal.time_of_arrival_to_the_place,
                        'barrel_feed_time': journal.barrel_feed_time,
                        'area': journal.area,
                        'liquidation': journal.liquidation,
                        'localization_time': journal.localization_time,
                        'quantity_rescued': journal.quantity_rescued,
                        'quantity_victims': journal.quantity_victims,
                        'quantity_dead': journal.quantity_dead,
                        'quantity_rescued_kids': journal.quantity_rescued_kids,
                        'quantity_victims_kids': journal.quantity_victims_kids,
                        'quantity_dead_kids': journal.quantity_dead_kids,
                        'quantity_ammunition': journal.quantity_ammunition,
                        'violated_conditions': journal.violated_conditions,
                        'quantity_objects': journal.quantity_objects,
                        'area2': journal.area2,
                        'liquidation_time': journal.liquidation_time,
                        'time_return_to_location': journal.time_return_to_location,
                        'type_of_fire': journal.type_of_fire,
                        'category': journal.category,
                        'subtype': journal.subtype}
            form = JournalFormsEdit(initial=queryset)
            if request.method == 'POST':
                form = JournalFormsEdit(request.POST, initial=queryset)
                if form.is_valid():
                    Journal.objects.filter(id=id).update(**form.cleaned_data,
                                                         edit_user=f'{request.user.first_name}\n'
                                                                   f'{request.user.last_name}')
                    messages.success(request, f'Запис відредактованно користувачем: {request.user.username}')
                    return redirect('journal')

                else:
                    messages.warning(request, 'Помилка при передачі інформації!')
                    return redirect('journal')
            context = {
                'form': form,
                'title': 'Редагування запису',
                'queryset': journal

            }
            return render(request, 'journal/edit.html', context)

        except Journal.DoesNotExist:
            return HttpResponseNotFound('<h2>Запису не існує</h2>')
    else:
        messages.warning(request, 'Редагування чужих записів Заборонено!')
        return redirect('journal')


def load_cities_town(request):
    values = request.GET.get('values')
    try:
        towns = Town.objects.filter(city_id=values)
    except:
        raise ValueError()
    return render(request, 'journal/town_dropdown_list_option.html', {'towns': towns})


def load_cities(request):
    country_id = request.GET.get('country')
    try:
        cities = City.objects.filter(region_id=country_id)
    except:
        raise ValueError()
    return render(request, 'journal/city_dropdown_list_options.html', {'cities': cities})


def load_subtype(request):
    type = request.GET.get('values')
    try:
        sybtype = Subtype.objects.filter(type_id=type)
    except:
        raise ValueError()
    return render(request, 'journal/subtype_dropdown_list_options.html', {'subtype': sybtype})


def del_journal(request, id):
    if request.user.groups.filter(name="Окц").exists():
        try:
            journal = Journal.objects.get(id=id)
            if request.method == 'POST':
                journal.delete()
                messages.success(request, f'Запис видалено із таблиці корыстувачем: {request.user.username}')
                return redirect('journal')

        except Journal.DoesNotExist:
            return HttpResponseNotFound('<h2>Запису не існує</h2>')
    else:
        messages.warning(request, 'У вас не має прав для видалення записів!')
        return redirect('journal')


# No Fire

class JournalNotFire(ListView):
    model = NoFire
    template_name = 'journal/non_fire.html'
    context_object_name = 'no_fire'

    def get_context_data(self, **kwargs):
        context = super(JournalNotFire, self).get_context_data(**kwargs)
        context['title'] = "Не пов'язані з пожежею"
        context['form_add_no_fire'] = NoFireFormsAdd()
        context['page1'] = datetime.today() - timedelta(days=1)
        context['page2'] = datetime.today() - timedelta(days=2)
        context['page3'] = datetime.today() - timedelta(days=3)
        return context

    def get_queryset(self):
        return NoFire.objects.filter(
            date_of_receipt_message__range=[f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                                            f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59']).order_by(
            '-date_of_receipt_message')

    def render_to_response(self, context, **response_kwargs):
        if self.request.user.is_authenticated:
            return super(JournalNotFire, self).render_to_response(context, **response_kwargs)
        else:
            messages.warning(self.request, 'Схоже ви намагаєтеся зайти Не Авторизувавшись')
            return redirect('login')


class JournalNotFire1(ListView):
    """
    page 1
    """
    model = NoFire
    template_name = 'journal/non_fire_page1.html'
    context_object_name = 'no_fire'

    def get_context_data(self, **kwargs):
        context = super(JournalNotFire1, self).get_context_data(**kwargs)
        context['title'] = "Не пов'язані з пожежею"
        context['form_add_no_fire'] = NoFireFormsAdd()
        context['page1'] = datetime.today() - timedelta(days=1)
        context['page2'] = datetime.today() - timedelta(days=2)
        context['page3'] = datetime.today() - timedelta(days=3)
        return context

    def get_queryset(self):
        return NoFire.objects.filter(
            date_of_receipt_message__range=[f'{format_datetime(datetime.today() - timedelta(days=1), "Y-MM-dd")} 00:00',
                                            f'{format_datetime(datetime.today() - timedelta(days=1), "Y-MM-dd")} 23:59']).order_by(
            '-date_of_receipt_message')

    def render_to_response(self, context, **response_kwargs):
        if self.request.user.is_authenticated:
            return super(JournalNotFire1, self).render_to_response(context, **response_kwargs)
        else:
            messages.warning(self.request, 'Схоже ви намагаєтеся зайти Не Авторизувавшись')
            return redirect('login')


class JournalNotFire2(ListView):
    """
    page 2
    """
    model = NoFire
    template_name = 'journal/non_fire_page2.html'
    context_object_name = 'no_fire'

    def get_context_data(self, **kwargs):
        context = super(JournalNotFire2, self).get_context_data(**kwargs)
        context['title'] = "Не пов'язані з пожежею"
        context['form_add_no_fire'] = NoFireFormsAdd()
        context['page1'] = datetime.today() - timedelta(days=1)
        context['page2'] = datetime.today() - timedelta(days=2)
        context['page3'] = datetime.today() - timedelta(days=3)
        return context

    def get_queryset(self):
        return NoFire.objects.filter(
            date_of_receipt_message__range=[f'{format_datetime(datetime.today() - timedelta(days=2), "Y-MM-dd")} 00:00',
                                            f'{format_datetime(datetime.today() - timedelta(days=2), "Y-MM-dd")} 23:59']).order_by(
            '-date_of_receipt_message')

    def render_to_response(self, context, **response_kwargs):
        if self.request.user.is_authenticated:
            return super(JournalNotFire2, self).render_to_response(context, **response_kwargs)
        else:
            messages.warning(self.request, 'Схоже ви намагаєтеся зайти Не Авторизувавшись')
            return redirect('login')


class JournalNotFire3(ListView):
    """
    page 3
    """
    model = NoFire
    template_name = 'journal/non_fire_page3.html'
    context_object_name = 'no_fire'

    def get_context_data(self, **kwargs):
        context = super(JournalNotFire3, self).get_context_data(**kwargs)
        context['title'] = "Не пов'язані з пожежею"
        context['form_add_no_fire'] = NoFireFormsAdd()
        context['page1'] = datetime.today() - timedelta(days=1)
        context['page2'] = datetime.today() - timedelta(days=2)
        context['page3'] = datetime.today() - timedelta(days=3)
        return context

    def get_queryset(self):
        return NoFire.objects.filter(
            date_of_receipt_message__range=[f'{format_datetime(datetime.today() - timedelta(days=3), "Y-MM-dd")} 00:00',
                                            f'{format_datetime(datetime.today() - timedelta(days=3), "Y-MM-dd")} 23:59']).order_by(
            '-date_of_receipt_message')

    def render_to_response(self, context, **response_kwargs):
        if self.request.user.is_authenticated:
            return super(JournalNotFire3, self).render_to_response(context, **response_kwargs)
        else:
            messages.warning(self.request, 'Схоже ви намагаєтеся зайти Не Авторизувавшись')
            return redirect('login')


def add_no_fire(request):
    if request.method == 'POST':
        form_add_no_fire = NoFireFormsAdd(request.POST)
        if form_add_no_fire.is_valid():
            NoFire.objects.create(**form_add_no_fire.cleaned_data,
                                  quantity_departure=NoFire.objects.filter(
                                      date_of_receipt_message__range=[
                                          f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                                          f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59']).count() + 1,
                                  add_user=f'{request.user.first_name}\n'
                                           f'{request.user.last_name}')
            messages.success(request, f'Запис додано корыстувачем: {request.user.username}')
            return redirect('non_fire')
        else:
            messages.warning(request, 'Помилка при передачі інформації')
            return redirect('non_fire')


def edit_non_fire(request, id):
    try:
        no_fire = NoFire.objects.get(id=id)
        if request.user.groups.filter(name="Окц").exists() or \
                NoFire.objects.filter(id=id,
                                      add_user=f'{request.user.first_name}\n'
                                               f'{request.user.last_name}').exists():
            queryset = {'date_of_receipt_message': no_fire.date_of_receipt_message,
                        'information': no_fire.information,
                        'subdivisions': no_fire.subdivisions,
                        'departure_date': no_fire.departure_date,
                        'time_of_arrival_to_the_place': no_fire.time_of_arrival_to_the_place,
                        'time_return_to_location': no_fire.time_return_to_location,
                        }
            form = NoFireFormsEdit(initial=queryset)
            if request.method == 'POST':
                form = NoFireFormsEdit(request.POST, initial=queryset)
                if form.is_valid():
                    NoFire.objects.filter(id=id).update(**form.cleaned_data,
                                                        edit_user=f'{request.user.first_name}\n'
                                                                  f'{request.user.last_name}')

                    messages.success(request, f'Запис відредактованно корыстувачем: {request.user.username}')
                    return redirect('non_fire')

                else:
                    messages.warning(request, 'Помилка при передачі інформації')
                    return redirect('non_fire')

            context = {
                'form': form,
                'title': 'Редагування запису'
            }
            return render(request, 'journal/edit_non_fire.html', context)
        else:
            messages.warning(request, 'Редагування чужих записів Заборонено!')
            return redirect('non_fire')

    except NoFire.DoesNotExist:
        messages.warning(request, 'Такого запису не існує')
        return redirect('non_fire')


def del_non_fire(request, id):
    if request.user.groups.filter(name="Окц").exists():
        try:
            no_fire = NoFire.objects.get(id=id)
            if request.method == 'POST':
                no_fire.delete()
                messages.success(request, f'Запис видалено із таблиці корыстувачем: {request.user.username}')
                return redirect('non_fire')

        except Journal.DoesNotExist:
            return HttpResponseNotFound('<h2>Запису не існує</h2>')
    else:
        messages.warning(request, 'У вас не має прав для видалення записів')
        return redirect('non_fire')


class StatisticJournal(ListView):
    """
    Statistics journal by type and category
    Page 1
    """
    model = Journal
    template_name = 'journal/statistic_journal.html'
    context_object_name = 'statistic_journal'

    def get_context_data(self, **kwargs):
        """
        Rendering template statistic_journal_page1.html
        """
        datetime_range = [f"{format_datetime(datetime.today(), 'Y-MM-dd')} 00:00",
                          f"{format_datetime(datetime.today(), 'Y-MM-dd')} 06:00"]
        datetime_range2 = [f"{format_datetime(datetime.today(), 'Y-MM-dd')} 06:00",
                           f"{format_datetime(datetime.today(), 'Y-MM-dd')} 23:59"]
        datetime_range3 = [f"{format_datetime(datetime.today(), 'Y-MM-dd')} 00:00",
                           f"{format_datetime(datetime.today(), 'Y-MM-dd')} 23:59"]
        context = super(StatisticJournal, self).get_context_data(**kwargs)
        context['title'] = 'Статистика викликів'
        context['page1'] = datetime.today() - timedelta(days=1)
        context['page2'] = datetime.today() - timedelta(days=2)
        context['page3'] = datetime.today() - timedelta(days=3)
        context['form'] = DepartureStatisticsForm()
        context['departures'] = self.model.objects.filter(date_of_receipt_message__range=datetime_range,
                                                          category_id=25).count() + \
                                self.model.objects.filter(date_of_receipt_message__range=datetime_range,
                                                          category_id=26).count() + \
                                self.model.objects.filter(date_of_receipt_message__range=datetime_range,
                                                          category_id=28).count()

        context['departures2'] = self.model.objects.filter(date_of_receipt_message__range=datetime_range2,
                                                           category_id=25).count() + \
                                 self.model.objects.filter(date_of_receipt_message__range=datetime_range2,
                                                           category_id=26).count() + \
                                 self.model.objects.filter(date_of_receipt_message__range=datetime_range2,
                                                           category_id=28).count()

        context['departures3'] = self.model.objects.filter(date_of_receipt_message__range=datetime_range3,
                                                           category_id=25).count() + \
                                 self.model.objects.filter(date_of_receipt_message__range=datetime_range3,
                                                           category_id=26).count() + \
                                 self.model.objects.filter(date_of_receipt_message__range=datetime_range3,
                                                           category_id=28).count()

        context['events'] = self.model.objects.filter(date_of_receipt_message__range=datetime_range,
                                                      category_id=25).count() + \
                            self.model.objects.filter(date_of_receipt_message__range=datetime_range,
                                                      category_id=27).count()

        context['events2'] = self.model.objects.filter(date_of_receipt_message__range=datetime_range2,
                                                       category_id=25).count() + \
                             self.model.objects.filter(date_of_receipt_message__range=datetime_range2,
                                                       category_id=27).count()

        context['events3'] = self.model.objects.filter(date_of_receipt_message__range=datetime_range3,
                                                       category_id=25).count() + \
                             self.model.objects.filter(date_of_receipt_message__range=datetime_range3,
                                                       category_id=27).count()

        context['ns'] = self.model.objects.filter(date_of_receipt_message__range=datetime_range,
                                                  category_id=28).count() + \
                        self.model.objects.filter(date_of_receipt_message__range=datetime_range,
                                                  category_id=29).count()

        context['ns2'] = self.model.objects.filter(date_of_receipt_message__range=datetime_range2,
                                                   category_id=28).count() + \
                         self.model.objects.filter(date_of_receipt_message__range=datetime_range2,
                                                   category_id=29).count()

        context['ns3'] = self.model.objects.filter(date_of_receipt_message__range=datetime_range3,
                                                   category_id=28).count() + \
                         self.model.objects.filter(date_of_receipt_message__range=datetime_range3,
                                                   category_id=29).count()

        context['people_rescued'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['children_rescued'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['people_injured'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['children_injured'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['people_died'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['children_died'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['quantity_peoples'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_peoples'), 0))

        context['quantity_peoples2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2).aggregate(
            sum=Coalesce(Sum('quantity_peoples'), 0))

        context['quantity_peoples3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3).aggregate(
            sum=Coalesce(Sum('quantity_peoples'), 0))

        context['quantity_technics'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_technics'), 0))

        context['quantity_technics2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2).aggregate(
            sum=Coalesce(Sum('quantity_technics'), 0))

        context['quantity_technics3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3).aggregate(
            sum=Coalesce(Sum('quantity_technics'), 0))

        context['fire'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                type_of_fire_id=8).count()

        context['fire2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                type_of_fire_id=8).count()

        context['fire3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                type_of_fire_id=8).count()

        context['dwelling'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=1).count()

        context['dwelling2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=1).count()

        context['dwelling3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=1).count()

        context['notdwelling'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=2).count()

        context['notdwelling2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=2).count()

        context['notdwelling3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=2).count()

        context['object'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=3).count()

        context['object2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=3).count()

        context['object3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=3).count()

        context['min_oborony'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=4).count()

        context['min_oborony2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=4).count()

        context['min_oborony3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=4).count()

        context['ukr_zaliz'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=5).count()

        context['ukr_zaliz2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=5).count()

        context['ukr_zaliz3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=5).count()

        context['lis'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=7).count()

        context['lis2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=7).count()

        context['lis3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=7).count()

        context['count_lis'] = \
            sum([item.area2 for item in
                 self.model.objects.filter(
                     date_of_receipt_message__range=datetime_range3,
                     subtype=7)])

        context['trava'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=8).count()

        context['trava2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=8).count()

        context['trava3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=8).count()

        context['count_trava'] = \
            sum([item.area2 for item in
                 self.model.objects.filter(
                     date_of_receipt_message__range=datetime_range3,
                     subtype=8)])

        context['smitya'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=9).count()

        context['smitya2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=9).count()

        context['smitya3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=9).count()

        context['count_smitya'] = \
            sum([item.area2 for item in
                 self.model.objects.filter(
                     date_of_receipt_message__range=datetime_range3,
                     subtype=9)])

        context['selo'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=10).count()

        context['selo2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=10).count()

        context['selo3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=10).count()

        context['count_selo'] = \
            sum([item.area2 for item in
                 self.model.objects.filter(
                     date_of_receipt_message__range=datetime_range3,
                     subtype=10)])

        context['torf'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=11).count()

        context['torf2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=11).count()

        context['torf3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=11).count()

        context['count_torf'] = \
            sum([item.area2 for item in
                 self.model.objects.filter(
                     date_of_receipt_message__range=datetime_range3,
                     subtype=11)])

        context['ecosystems'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=7).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=8).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=9).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=10).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=11).count()

        context['ecosystems2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=7).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=8).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=9).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=10).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=11).count()

        context['ecosystems3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=7).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=8).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=9).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=10).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=11).count()

        context['count_ecosystems'] = \
            sum(
                [
                    sum(
                        [item.area2 for item in
                         self.model.objects.filter(
                             date_of_receipt_message__range=datetime_range3,
                             subtype=7)]),
                    sum(
                        [item.area2 for item in
                         self.model.objects.filter(
                             date_of_receipt_message__range=datetime_range3,
                             subtype=8)]),

                    sum(
                        [item.area2 for item in
                         self.model.objects.filter(
                             date_of_receipt_message__range=datetime_range3,
                             subtype=9)]),
                    sum(
                        [item.area2 for item in
                         self.model.objects.filter(
                             date_of_receipt_message__range=datetime_range3,
                             subtype=10)]),
                    sum(
                        [item.area2 for item in
                         self.model.objects.filter(
                             date_of_receipt_message__range=datetime_range3,
                             subtype=11)])
                ]

            )

        context['avto'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=13).count()

        context['avto2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=13).count()

        context['avto3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=13).count()

        context['zalizn'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=14).count()

        context['zalizn2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=14).count()

        context['zalizn3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=14).count()

        context['avia'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=15).count()

        context['avia2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=15).count()

        context['avia3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=15).count()

        context['transports'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=13).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=14).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=15).count()

        context['transports2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=13).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=14).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=15).count()

        context['transports3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=13).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=14).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=15).count()

        context['people_rescued_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued2_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued3_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['children_rescued_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued2_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued3_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['people_injured_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured2_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured3_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['children_injured_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured2_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured3_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['people_died_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died2_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died3_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['children_died_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died2_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died3_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['dopomoga'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                type_of_fire_id=12).count()

        context['dopomoga2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                type_of_fire_id=12).count()

        context['dopomoga3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                type_of_fire_id=12).count()

        context['dtp'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=19).count()

        context['dtp2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=19).count()

        context['dtp3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=19).count()

        context['dtp_podiya'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=20).count()

        context['dtp_podiya2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=20).count()

        context['dtp_podiya3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=20).count()

        context['dopomoga_nas'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=21).count()

        context['dopomoga_nas2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=21).count()

        context['dopomoga_nas3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=21).count()

        context['dopomoga102'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=22).count()

        context['dopomoga102_2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=22).count()

        context['dopomoga102_3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=22).count()

        context['dopomoga103'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=23).count()

        context['dopomoga103_2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=23).count()

        context['dopomoga103_3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=23).count()

        context['dopomoga104'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=24).count()

        context['dopomoga104_2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=24).count()

        context['dopomoga104_3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=24).count()

        context['podiya_na_vodi'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=25).count()

        context['podiya_na_vodi2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=25).count()

        context['podiya_na_vodi3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=25).count()

        context['podiya_inshi'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=26).count()

        context['podiya_inshi2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=26).count()

        context['podiya_inshi3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=26).count()

        context['parnokopitni'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=27).count()

        context['parnokopitni2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=27).count()

        context['parnokopitni3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=27).count()

        context['dog'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=28).count()

        context['dog2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=28).count()

        context['dog3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=28).count()

        context['cat'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=29).count()

        context['cat2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=29).count()

        context['cat3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=29).count()

        context['plazuni'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=30).count()

        context['plazuni2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=30).count()

        context['plazuni3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=30).count()

        context['tvar_inshi'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=31).count()

        context['tvar_inshi2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=31).count()

        context['tvar_inshi3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=31).count()

        context['zag_tvar'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=27).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=28).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=29).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=30).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=31).count()

        context['zag_tvar2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=27).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=28).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=29).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=30).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=31).count()

        context['zag_tvar3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=27).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=28).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=29).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=30).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=31).count()

        context['san_obrobka'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=37).count()

        context['san_obrobka2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=37).count()

        context['san_obrobka3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=37).count()

        context['opendoors'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=38).count()

        context['opendoors2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=38).count()

        context['opendoors3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=38).count()

        context['opencar'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=39).count()

        context['opencar2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=39).count()

        context['opencar3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=39).count()

        context['people_rescued_dopomoga'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=12).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued2_dopomoga'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=12).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued3_dopomoga'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=12).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['children_rescued_dopomoga'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=12).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued2_dopomoga'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=12).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued3_dopomoga'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=12).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['people_rescued_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued2_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued3_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['children_rescued_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued2_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued3_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['people_injured_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured2_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured3_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['children_injured_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured2_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured3_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['people_died_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died2_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died3_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['children_died_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died2_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died3_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['people_rescued_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued2_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued3_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['children_rescued_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued2_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued3_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['people_injured_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured2_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured3_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['children_injured_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured2_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured3_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['people_died_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died2_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died3_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['children_died_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died2_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died3_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['people_rescued_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued2_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued3_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['children_rescued_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued2_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued3_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['people_injured_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured2_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured3_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['children_injured_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured2_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured3_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['people_died_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died2_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died3_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['children_died_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died2_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died3_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['vnp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            type_of_fire_id=13).count()

        context['vnp2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            type_of_fire_id=13).count()

        context['vnp3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            type_of_fire_id=13).count()

        context['quantity_vnp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=13).aggregate(
            sum=Coalesce(Sum('quantity_ammunition'), 0))

        context['quantity_vnp2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=13).aggregate(
            sum=Coalesce(Sum('quantity_ammunition'), 0))

        context['quantity_vnp3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=13).aggregate(
            sum=Coalesce(Sum('quantity_ammunition'), 0))

        context['hibniy_viklik'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            type_of_fire_id=9).count()

        context['hibniy_viklik2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            type_of_fire_id=9).count()

        context['hibniy_viklik3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            type_of_fire_id=9).count()

        context['aps'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            type_of_fire_id=10).count()

        context['aps2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            type_of_fire_id=10).count()

        context['aps3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            type_of_fire_id=10).count()

        context['ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            type_of_fire_id=14).count()

        context['ns2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            type_of_fire_id=14).count()

        context['ns3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            type_of_fire_id=14).count()

        context['tehno_haracter'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            subtype=32).count()

        context['tehno_haracter2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            subtype=32).count()

        context['tehno_haracter3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            subtype=32).count()

        context['prirodnogo_haracter'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            subtype=33).count()

        context['prirodnogo_haracter2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            subtype=33).count()

        context['prirodnogo_haracter3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            subtype=33).count()

        context['social_haracter'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            subtype=34).count()

        context['social_haracter2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            subtype=34).count()

        context['social_haracter3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            subtype=34).count()

        context['voen_haracter'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            subtype=35).count()

        context['voen_haracter2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            subtype=35).count()

        context['voen_haracter3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            subtype=35).count()

        context['quantity_umovi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('violated_conditions'), 0))

        context['quantity_umovi2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('violated_conditions'), 0))

        context['quantity_umovi3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('violated_conditions'), 0))

        context['people_rescued_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued2_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued3_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['children_rescued_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued2_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued3_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['people_injured_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured2_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured3_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['children_injured_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured2_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured3_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['people_died_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died2_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died3_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['children_died_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died2_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died3_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['zaminuvanya'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            type_of_fire_id=15).count()

        context['zaminuvanya2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            type_of_fire_id=15).count()

        context['zaminuvanya3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            type_of_fire_id=15).count()

        context['zaminuvanya_object'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=15).aggregate(
            sum=Coalesce(Sum('quantity_objects'), 0))

        context['zaminuvanya2_object'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=15).aggregate(
            sum=Coalesce(Sum('quantity_objects'), 0))

        context['zaminuvanya3_object'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=15).aggregate(
            sum=Coalesce(Sum('quantity_objects'), 0))

        context['inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            type_of_fire_id=11).count()

        context['inshi2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            type_of_fire_id=11).count()

        context['inshi3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            type_of_fire_id=11).count()

        context['kz'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            subtype=16).count()

        context['kz2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            subtype=16).count()

        context['kz3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            subtype=16).count()

        context['prigoranya_izhi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            subtype=17).count()

        context['prigoranya_izhi2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            subtype=17).count()

        context['prigoranya_izhi3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            subtype=17).count()

        context['info_ne_pidt'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            subtype=18).count()

        context['info_ne_pidt2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            subtype=18).count()

        context['info_ne_pidt3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            subtype=18).count()

        return context

    def render_to_response(self, context, **response_kwargs):
        """
        check on the authenticated user
        """
        if self.request.user.is_authenticated:
            return super(StatisticJournal, self).render_to_response(context, **response_kwargs)
        else:
            messages.warning(self.request, 'Схоже ви намагаєтеся зайти Не Авторизувавшись')
            return redirect('login')


def filter(request):
    """
    The function returns call statistics from the log according to the time interval
    """
    if request.method == 'POST':
        form = DepartureStatisticsForm(request.POST)
        if form.is_valid():

            datetime_range = [f"{format_datetime(form.cleaned_data['start_datetime'], 'Y-MM-dd H:mm')}",
                              f"{format_datetime(form.cleaned_data['end_datetime'], 'Y-MM-dd H:mm')}"]
            context = {
                'title': 'Статистика викликів',
                'page1': datetime.today() - timedelta(days=1),
                'page2': datetime.today() - timedelta(days=2),
                'page3': datetime.today() - timedelta(days=3),
                'form': DepartureStatisticsForm(),
                'start_datetime': format_datetime(form.cleaned_data['start_datetime'],
                                                  "EEEE  d MMMM Y року H:mm", locale='uk_UA'),
                'end_datetime': format_datetime(form.cleaned_data['end_datetime'],
                                                "EEEE  d MMMM Y року H:mm", locale='uk_UA'),

                'departures': Journal.objects.filter(date_of_receipt_message__range=datetime_range,
                                                     category_id=25).count() + \
                              Journal.objects.filter(date_of_receipt_message__range=datetime_range,
                                                     category_id=26).count() + \
                              Journal.objects.filter(date_of_receipt_message__range=datetime_range,
                                                     category_id=28).count(),

                'events': Journal.objects.filter(date_of_receipt_message__range=datetime_range,
                                                 category_id=25).count() + \
                          Journal.objects.filter(date_of_receipt_message__range=datetime_range,
                                                 category_id=27).count(),

                'ns': Journal.objects.filter(date_of_receipt_message__range=datetime_range,
                                             category_id=28).count() + \
                      Journal.objects.filter(date_of_receipt_message__range=datetime_range,
                                             category_id=29).count(),

                'people_rescued': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range).aggregate(
                    sum=Coalesce(Sum('quantity_rescued'), 0)),

                'children_rescued': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range).aggregate(
                    sum=Coalesce(Sum('quantity_rescued_kids'), 0)),

                'people_injured': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range).aggregate(
                    sum=Coalesce(Sum('quantity_victims'), 0)),

                'children_injured': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range).aggregate(
                    sum=Coalesce(Sum('quantity_victims_kids'), 0)),

                'people_died': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range).aggregate(
                    sum=Coalesce(Sum('quantity_dead'), 0)),

                'children_died': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range).aggregate(
                    sum=Coalesce(Sum('quantity_dead_kids'), 0)),

                'quantity_peoples': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range).aggregate(
                    sum=Coalesce(Sum('quantity_peoples'), 0)),

                'quantity_technics': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range).aggregate(
                    sum=Coalesce(Sum('quantity_technics'), 0)),

                'fire': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    type_of_fire_id=8).count(),

                'dwelling': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    subtype=1).count(),

                'notdwelling': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    subtype=2).count(),

                'object': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    subtype=3).count(),

                'min_oborony': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    subtype=4).count(),

                'ukr_zaliz': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    subtype=5).count(),

                'lis': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    subtype=7).count(),

                'count_lis': sum([item.area2 for item in
                                  Journal.objects.filter(
                                      date_of_receipt_message__range=datetime_range,
                                      subtype=7)]),

                'trava': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    subtype=8).count(),

                'count_trava': sum([item.area2 for item in
                                    Journal.objects.filter(
                                        date_of_receipt_message__range=datetime_range,
                                        subtype=8)]),

                'smitya': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    subtype=9).count(),

                'count_smitya': sum([item.area2 for item in
                                     Journal.objects.filter(
                                         date_of_receipt_message__range=datetime_range,
                                         subtype=9)]),

                'selo':
                    Journal.objects.filter(
                        date_of_receipt_message__range=datetime_range,
                        subtype=10).count(),

                'count_selo': sum([item.area2 for item in
                                   Journal.objects.filter(
                                       date_of_receipt_message__range=datetime_range,
                                       subtype=10)]),

                'torf': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    subtype=11).count(),

                'count_torf': sum([item.area2 for item in
                                   Journal.objects.filter(
                                       date_of_receipt_message__range=datetime_range,
                                       subtype=11)]),

                'ecosystems':
                    Journal.objects.filter(
                        date_of_receipt_message__range=datetime_range,
                        subtype=7).count() + \
                    Journal.objects.filter(
                        date_of_receipt_message__range=datetime_range,
                        subtype=8).count() + \
                    Journal.objects.filter(
                        date_of_receipt_message__range=datetime_range,
                        subtype=9).count() + \
                    Journal.objects.filter(
                        date_of_receipt_message__range=datetime_range,
                        subtype=10).count() + \
                    Journal.objects.filter(
                        date_of_receipt_message__range=datetime_range,
                        subtype=11).count(),

                'count_ecosystems': sum([
                    sum(
                        [item.area2 for item in
                         Journal.objects.filter(
                             date_of_receipt_message__range=datetime_range,
                             subtype=7)]),
                    sum(
                        [item.area2 for item in
                         Journal.objects.filter(
                             date_of_receipt_message__range=datetime_range,
                             subtype=8)]),

                    sum(
                        [item.area2 for item in
                         Journal.objects.filter(
                             date_of_receipt_message__range=datetime_range,
                             subtype=9)]),
                    sum(
                        [item.area2 for item in
                         Journal.objects.filter(
                             date_of_receipt_message__range=datetime_range,
                             subtype=10)]),
                    sum(
                        [item.area2 for item in
                         Journal.objects.filter(
                             date_of_receipt_message__range=datetime_range,
                             subtype=11)])
                ]

                ),

                'avto': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    subtype=13).count(),

                'zalizn': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    subtype=14).count(),

                'avia': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    subtype=15).count(),

                'transports': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    subtype=13).count() + \
                              Journal.objects.filter(
                                  date_of_receipt_message__range=datetime_range,
                                  subtype=14).count() + \
                              Journal.objects.filter(
                                  date_of_receipt_message__range=datetime_range,
                                  subtype=15).count(),

                'people_rescued_fire': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range, type_of_fire_id=8).aggregate(
                    sum=Coalesce(Sum('quantity_rescued'), 0)),

                'children_rescued_fire': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range, type_of_fire_id=8).aggregate(
                    sum=Coalesce(Sum('quantity_rescued_kids'), 0)),

                'people_injured_fire': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range, type_of_fire_id=8).aggregate(
                    sum=Coalesce(Sum('quantity_victims'), 0)),

                'children_injured_fire': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range, type_of_fire_id=8).aggregate(
                    sum=Coalesce(Sum('quantity_victims_kids'), 0)),

                'people_died_fire': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range, type_of_fire_id=8).aggregate(
                    sum=Coalesce(Sum('quantity_dead'), 0)),

                'children_died_fire': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range, type_of_fire_id=8).aggregate(
                    sum=Coalesce(Sum('quantity_dead_kids'), 0)),

                'dopomoga': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    type_of_fire_id=12).count(),

                'dtp': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    subtype=19).count(),

                'dtp_podiya': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    subtype=20).count(),

                'dopomoga_nas': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    subtype=21).count(),

                'dopomoga102': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    subtype=22).count(),

                'dopomoga103': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    subtype=23).count(),

                'dopomoga104': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    subtype=24).count(),

                'podiya_na_vodi': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    subtype=25).count(),

                'podiya_inshi': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    subtype=26).count(),

                'parnokopitni': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    subtype=27).count(),

                'dog': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    subtype=28).count(),

                'cat': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    subtype=29).count(),

                'plazuni': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    subtype=30).count(),

                'tvar_inshi': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    subtype=31).count(),

                'zag_tvar':
                    Journal.objects.filter(
                        date_of_receipt_message__range=datetime_range,
                        subtype=27).count() + \
                    Journal.objects.filter(
                        date_of_receipt_message__range=datetime_range,
                        subtype=28).count() + \
                    Journal.objects.filter(
                        date_of_receipt_message__range=datetime_range,
                        subtype=29).count() + \
                    Journal.objects.filter(
                        date_of_receipt_message__range=datetime_range,
                        subtype=30).count() + \
                    Journal.objects.filter(
                        date_of_receipt_message__range=datetime_range,
                        subtype=31).count(),

                'san_obrobka':
                    Journal.objects.filter(
                        date_of_receipt_message__range=datetime_range,
                        subtype=37).count(),

                'opendoors':
                    Journal.objects.filter(
                        date_of_receipt_message__range=datetime_range,
                        subtype=38).count(),

                'opencar':
                    Journal.objects.filter(
                        date_of_receipt_message__range=datetime_range,
                        subtype=39).count(),

                'people_rescued_dopomoga': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range, type_of_fire_id=12).aggregate(
                    sum=Coalesce(Sum('quantity_rescued'), 0)),

                'children_rescued_dopomoga': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range, type_of_fire_id=12).aggregate(
                    sum=Coalesce(Sum('quantity_rescued_kids'), 0)),

                'people_rescued_dtp': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range, subtype=20).aggregate(
                    sum=Coalesce(Sum('quantity_rescued'), 0)),

                'children_rescued_dtp': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range, subtype=20).aggregate(
                    sum=Coalesce(Sum('quantity_rescued_kids'), 0)),

                'people_injured_dtp': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range, subtype=20).aggregate(
                    sum=Coalesce(Sum('quantity_victims'), 0)),

                'children_injured_dtp': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range, subtype=20).aggregate(
                    sum=Coalesce(Sum('quantity_victims_kids'), 0)),

                'people_died_dtp': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range, subtype=20).aggregate(
                    sum=Coalesce(Sum('quantity_dead'), 0)),

                'children_died_dtp': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range, subtype=20).aggregate(
                    sum=Coalesce(Sum('quantity_dead_kids'), 0)),

                'people_rescued_voda': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range, subtype=25).aggregate(
                    sum=Coalesce(Sum('quantity_rescued'), 0)),

                'children_rescued_voda': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range, subtype=25).aggregate(
                    sum=Coalesce(Sum('quantity_rescued_kids'), 0)),

                'people_injured_voda': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range, subtype=25).aggregate(
                    sum=Coalesce(Sum('quantity_victims'), 0)),

                'children_injured_voda': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range, subtype=25).aggregate(
                    sum=Coalesce(Sum('quantity_victims_kids'), 0)),

                'people_died_voda': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range, subtype=25).aggregate(
                    sum=Coalesce(Sum('quantity_dead'), 0)),

                'children_died_voda': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range, subtype=25).aggregate(
                    sum=Coalesce(Sum('quantity_dead_kids'), 0)),

                'people_rescued_inshi': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range, subtype=26).aggregate(
                    sum=Coalesce(Sum('quantity_rescued'), 0)),

                'children_rescued_inshi': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range, subtype=26).aggregate(
                    sum=Coalesce(Sum('quantity_rescued_kids'), 0)),

                'people_injured_inshi': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range, subtype=26).aggregate(
                    sum=Coalesce(Sum('quantity_victims'), 0)),

                'children_injured_inshi': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range, subtype=26).aggregate(
                    sum=Coalesce(Sum('quantity_victims_kids'), 0)),

                'people_died_inshi': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range, subtype=26).aggregate(
                    sum=Coalesce(Sum('quantity_dead'), 0)),

                'children_died_inshi': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range, subtype=26).aggregate(
                    sum=Coalesce(Sum('quantity_dead_kids'), 0)),

                'vnp': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    type_of_fire_id=13).count(),

                'quantity_vnp': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range, type_of_fire_id=13).aggregate(
                    sum=Coalesce(Sum('quantity_ammunition'), 0)),

                'hibniy_viklik': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    type_of_fire_id=9).count(),

                'aps': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    type_of_fire_id=10).count(),

                'ns': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    type_of_fire_id=14).count(),

                'tehno_haracter': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    subtype=32).count(),

                'prirodnogo_haracter': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    subtype=33).count(),

                'social_haracter': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    subtype=34).count(),

                'voen_haracter': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    subtype=35).count(),

                'quantity_umovi': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range, type_of_fire_id=14).aggregate(
                    sum=Coalesce(Sum('violated_conditions'), 0)),

                'people_rescued_ns': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range, type_of_fire_id=14).aggregate(
                    sum=Coalesce(Sum('quantity_rescued'), 0)),

                'children_rescued_ns': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range, type_of_fire_id=14).aggregate(
                    sum=Coalesce(Sum('quantity_rescued_kids'), 0)),

                'people_injured_ns': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range, type_of_fire_id=14).aggregate(
                    sum=Coalesce(Sum('quantity_victims'), 0)),

                'children_injured_ns': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range, type_of_fire_id=14).aggregate(
                    sum=Coalesce(Sum('quantity_victims_kids'), 0)),

                'people_died_ns': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range, type_of_fire_id=14).aggregate(
                    sum=Coalesce(Sum('quantity_dead'), 0)),

                'children_died_ns': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range, type_of_fire_id=14).aggregate(
                    sum=Coalesce(Sum('quantity_dead_kids'), 0)),

                'zaminuvanya': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    type_of_fire_id=15).count(),

                'zaminuvanya_object': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range, type_of_fire_id=15).aggregate(
                    sum=Coalesce(Sum('quantity_objects'), 0)),

                'inshi': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    type_of_fire_id=11).count(),

                'kz': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    subtype=16).count(),

                'prigoranya_izhi': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    subtype=17).count(),

                'info_ne_pidt': Journal.objects.filter(
                    date_of_receipt_message__range=datetime_range,
                    subtype=18).count()
            }

            messages.success(request, 'Статистика викликів підрахована за вашим запитом')
            return render(request, 'journal/filter.html', context)
        else:
            messages.warning(request, f'Невірний формат дати або часу')
            return redirect('statistic_journal')


class StatisticJournal1(ListView):
    """
    Statistics journal by type and category
    Page 1
    """
    model = Journal
    template_name = 'journal/statistic_journal_page1.html'
    context_object_name = 'statistic_journal'

    def get_context_data(self, **kwargs):
        """
        Rendering template statistic_journal_page1.html
        """
        datetime_range = [f"{format_datetime(datetime.today() - timedelta(days=1), 'Y-MM-dd')} 00:00",
                          f"{format_datetime(datetime.today() - timedelta(days=1), 'Y-MM-dd')} 06:00"]
        datetime_range2 = [f"{format_datetime(datetime.today() - timedelta(days=1), 'Y-MM-dd')} 06:00",
                           f"{format_datetime(datetime.today() - timedelta(days=1), 'Y-MM-dd')} 23:59"]
        datetime_range3 = [f"{format_datetime(datetime.today() - timedelta(days=1), 'Y-MM-dd')} 00:00",
                           f"{format_datetime(datetime.today() - timedelta(days=1), 'Y-MM-dd')} 23:59"]
        context = super(StatisticJournal1, self).get_context_data(**kwargs)
        context['title'] = 'Статистика викликів'
        context['page1'] = datetime.today() - timedelta(days=1)
        context['page2'] = datetime.today() - timedelta(days=2)
        context['page3'] = datetime.today() - timedelta(days=3)
        context['form'] = DepartureStatisticsForm()
        context['departures'] = self.model.objects.filter(date_of_receipt_message__range=datetime_range,
                                                          category_id=25).count() + \
                                self.model.objects.filter(date_of_receipt_message__range=datetime_range,
                                                          category_id=26).count() + \
                                self.model.objects.filter(date_of_receipt_message__range=datetime_range,
                                                          category_id=28).count()

        context['departures2'] = self.model.objects.filter(date_of_receipt_message__range=datetime_range2,
                                                           category_id=25).count() + \
                                 self.model.objects.filter(date_of_receipt_message__range=datetime_range2,
                                                           category_id=26).count() + \
                                 self.model.objects.filter(date_of_receipt_message__range=datetime_range2,
                                                           category_id=28).count()

        context['departures3'] = self.model.objects.filter(date_of_receipt_message__range=datetime_range3,
                                                           category_id=25).count() + \
                                 self.model.objects.filter(date_of_receipt_message__range=datetime_range3,
                                                           category_id=26).count() + \
                                 self.model.objects.filter(date_of_receipt_message__range=datetime_range3,
                                                           category_id=28).count()

        context['events'] = self.model.objects.filter(date_of_receipt_message__range=datetime_range,
                                                      category_id=25).count() + \
                            self.model.objects.filter(date_of_receipt_message__range=datetime_range,
                                                      category_id=27).count()

        context['events2'] = self.model.objects.filter(date_of_receipt_message__range=datetime_range2,
                                                       category_id=25).count() + \
                             self.model.objects.filter(date_of_receipt_message__range=datetime_range2,
                                                       category_id=27).count()

        context['events3'] = self.model.objects.filter(date_of_receipt_message__range=datetime_range3,
                                                       category_id=25).count() + \
                             self.model.objects.filter(date_of_receipt_message__range=datetime_range3,
                                                       category_id=27).count()

        context['ns'] = self.model.objects.filter(date_of_receipt_message__range=datetime_range,
                                                  category_id=28).count() + \
                        self.model.objects.filter(date_of_receipt_message__range=datetime_range,
                                                  category_id=29).count()

        context['ns2'] = self.model.objects.filter(date_of_receipt_message__range=datetime_range2,
                                                   category_id=28).count() + \
                         self.model.objects.filter(date_of_receipt_message__range=datetime_range2,
                                                   category_id=29).count()

        context['ns3'] = self.model.objects.filter(date_of_receipt_message__range=datetime_range3,
                                                   category_id=28).count() + \
                         self.model.objects.filter(date_of_receipt_message__range=datetime_range3,
                                                   category_id=29).count()

        context['people_rescued'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['children_rescued'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['people_injured'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['children_injured'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['people_died'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['children_died'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['quantity_peoples'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_peoples'), 0))

        context['quantity_peoples2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2).aggregate(
            sum=Coalesce(Sum('quantity_peoples'), 0))

        context['quantity_peoples3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3).aggregate(
            sum=Coalesce(Sum('quantity_peoples'), 0))

        context['quantity_technics'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_technics'), 0))

        context['quantity_technics2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2).aggregate(
            sum=Coalesce(Sum('quantity_technics'), 0))

        context['quantity_technics3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3).aggregate(
            sum=Coalesce(Sum('quantity_technics'), 0))

        context['fire'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                type_of_fire_id=8).count()

        context['fire2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                type_of_fire_id=8).count()

        context['fire3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                type_of_fire_id=8).count()

        context['dwelling'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=1).count()

        context['dwelling2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=1).count()

        context['dwelling3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=1).count()

        context['notdwelling'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=2).count()

        context['notdwelling2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=2).count()

        context['notdwelling3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=2).count()

        context['object'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=3).count()

        context['object2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=3).count()

        context['object3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=3).count()

        context['min_oborony'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=4).count()

        context['min_oborony2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=4).count()

        context['min_oborony3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=4).count()

        context['ukr_zaliz'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=5).count()

        context['ukr_zaliz2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=5).count()

        context['ukr_zaliz3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=5).count()

        context['lis'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=7).count()

        context['lis2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=7).count()

        context['lis3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=7).count()

        context['count_lis'] = \
            sum([item.area2 for item in
                 self.model.objects.filter(
                     date_of_receipt_message__range=datetime_range3,
                     subtype=7)])

        context['trava'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=8).count()

        context['trava2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=8).count()

        context['trava3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=8).count()

        context['count_trava'] = \
            sum([item.area2 for item in
                 self.model.objects.filter(
                     date_of_receipt_message__range=datetime_range3,
                     subtype=8)])

        context['smitya'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=9).count()

        context['smitya2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=9).count()

        context['smitya3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=9).count()

        context['count_smitya'] = \
            sum([item.area2 for item in
                 self.model.objects.filter(
                     date_of_receipt_message__range=datetime_range3,
                     subtype=9)])

        context['selo'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=10).count()

        context['selo2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=10).count()

        context['selo3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=10).count()

        context['count_selo'] = \
            sum([item.area2 for item in
                 self.model.objects.filter(
                     date_of_receipt_message__range=datetime_range3,
                     subtype=10)])

        context['torf'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=11).count()

        context['torf2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=11).count()

        context['torf3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=11).count()

        context['count_torf'] = \
            sum([item.area2 for item in
                 self.model.objects.filter(
                     date_of_receipt_message__range=datetime_range3,
                     subtype=11)])

        context['ecosystems'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=7).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=8).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=9).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=10).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=11).count()

        context['ecosystems2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=7).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=8).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=9).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=10).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=11).count()

        context['ecosystems3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=7).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=8).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=9).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=10).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=11).count()

        context['count_ecosystems'] = \
            sum(
                [
                    sum(
                        [item.area2 for item in
                         self.model.objects.filter(
                             date_of_receipt_message__range=datetime_range3,
                             subtype=7)]),
                    sum(
                        [item.area2 for item in
                         self.model.objects.filter(
                             date_of_receipt_message__range=datetime_range3,
                             subtype=8)]),

                    sum(
                        [item.area2 for item in
                         self.model.objects.filter(
                             date_of_receipt_message__range=datetime_range3,
                             subtype=9)]),
                    sum(
                        [item.area2 for item in
                         self.model.objects.filter(
                             date_of_receipt_message__range=datetime_range3,
                             subtype=10)]),
                    sum(
                        [item.area2 for item in
                         self.model.objects.filter(
                             date_of_receipt_message__range=datetime_range3,
                             subtype=11)])
                ]

            )

        context['avto'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=13).count()

        context['avto2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=13).count()

        context['avto3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=13).count()

        context['zalizn'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=14).count()

        context['zalizn2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=14).count()

        context['zalizn3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=14).count()

        context['avia'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=15).count()

        context['avia2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=15).count()

        context['avia3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=15).count()

        context['transports'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=13).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=14).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=15).count()

        context['transports2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=13).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=14).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=15).count()

        context['transports3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=13).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=14).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=15).count()

        context['people_rescued_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued2_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued3_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['children_rescued_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued2_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued3_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['people_injured_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured2_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured3_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['children_injured_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured2_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured3_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['people_died_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died2_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died3_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['children_died_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died2_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died3_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['dopomoga'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                type_of_fire_id=12).count()

        context['dopomoga2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                type_of_fire_id=12).count()

        context['dopomoga3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                type_of_fire_id=12).count()

        context['dtp'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=19).count()

        context['dtp2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=19).count()

        context['dtp3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=19).count()

        context['dtp_podiya'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=20).count()

        context['dtp_podiya2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=20).count()

        context['dtp_podiya3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=20).count()

        context['dopomoga_nas'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=21).count()

        context['dopomoga_nas2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=21).count()

        context['dopomoga_nas3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=21).count()

        context['dopomoga102'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=22).count()

        context['dopomoga102_2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=22).count()

        context['dopomoga102_3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=22).count()

        context['dopomoga103'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=23).count()

        context['dopomoga103_2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=23).count()

        context['dopomoga103_3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=23).count()

        context['dopomoga104'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=24).count()

        context['dopomoga104_2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=24).count()

        context['dopomoga104_3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=24).count()

        context['podiya_na_vodi'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=25).count()

        context['podiya_na_vodi2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=25).count()

        context['podiya_na_vodi3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=25).count()

        context['podiya_inshi'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=26).count()

        context['podiya_inshi2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=26).count()

        context['podiya_inshi3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=26).count()

        context['parnokopitni'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=27).count()

        context['parnokopitni2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=27).count()

        context['parnokopitni3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=27).count()

        context['dog'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=28).count()

        context['dog2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=28).count()

        context['dog3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=28).count()

        context['cat'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=29).count()

        context['cat2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=29).count()

        context['cat3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=29).count()

        context['plazuni'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=30).count()

        context['plazuni2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=30).count()

        context['plazuni3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=30).count()

        context['tvar_inshi'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=31).count()

        context['tvar_inshi2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=31).count()

        context['tvar_inshi3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=31).count()

        context['zag_tvar'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=27).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=28).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=29).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=30).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=31).count()

        context['zag_tvar2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=27).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=28).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=29).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=30).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=31).count()

        context['zag_tvar3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=27).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=28).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=29).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=30).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=31).count()

        context['san_obrobka'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=37).count()

        context['san_obrobka2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=37).count()

        context['san_obrobka3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=37).count()

        context['opendoors'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=38).count()

        context['opendoors2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=38).count()

        context['opendoors3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=38).count()

        context['opencar'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=39).count()

        context['opencar2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=39).count()

        context['opencar3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=39).count()

        context['people_rescued_dopomoga'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=12).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued2_dopomoga'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=12).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued3_dopomoga'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=12).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['children_rescued_dopomoga'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=12).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued2_dopomoga'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=12).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued3_dopomoga'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=12).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['people_rescued_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued2_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued3_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['children_rescued_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued2_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued3_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['people_injured_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured2_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured3_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['children_injured_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured2_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured3_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['people_died_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died2_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died3_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['children_died_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died2_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died3_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['people_rescued_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued2_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued3_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['children_rescued_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued2_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued3_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['people_injured_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured2_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured3_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['children_injured_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured2_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured3_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['people_died_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died2_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died3_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['children_died_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died2_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died3_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['people_rescued_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued2_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued3_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['children_rescued_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued2_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued3_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['people_injured_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured2_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured3_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['children_injured_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured2_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured3_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['people_died_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died2_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died3_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['children_died_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died2_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died3_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['vnp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            type_of_fire_id=13).count()

        context['vnp2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            type_of_fire_id=13).count()

        context['vnp3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            type_of_fire_id=13).count()

        context['quantity_vnp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=13).aggregate(
            sum=Coalesce(Sum('quantity_ammunition'), 0))

        context['quantity_vnp2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=13).aggregate(
            sum=Coalesce(Sum('quantity_ammunition'), 0))

        context['quantity_vnp3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=13).aggregate(
            sum=Coalesce(Sum('quantity_ammunition'), 0))

        context['hibniy_viklik'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            type_of_fire_id=9).count()

        context['hibniy_viklik2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            type_of_fire_id=9).count()

        context['hibniy_viklik3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            type_of_fire_id=9).count()

        context['aps'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            type_of_fire_id=10).count()

        context['aps2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            type_of_fire_id=10).count()

        context['aps3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            type_of_fire_id=10).count()

        context['ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            type_of_fire_id=14).count()

        context['ns2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            type_of_fire_id=14).count()

        context['ns3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            type_of_fire_id=14).count()

        context['tehno_haracter'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            subtype=32).count()

        context['tehno_haracter2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            subtype=32).count()

        context['tehno_haracter3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            subtype=32).count()

        context['prirodnogo_haracter'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            subtype=33).count()

        context['prirodnogo_haracter2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            subtype=33).count()

        context['prirodnogo_haracter3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            subtype=33).count()

        context['social_haracter'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            subtype=34).count()

        context['social_haracter2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            subtype=34).count()

        context['social_haracter3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            subtype=34).count()

        context['voen_haracter'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            subtype=35).count()

        context['voen_haracter2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            subtype=35).count()

        context['voen_haracter3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            subtype=35).count()

        context['quantity_umovi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('violated_conditions'), 0))

        context['quantity_umovi2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('violated_conditions'), 0))

        context['quantity_umovi3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('violated_conditions'), 0))

        context['people_rescued_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued2_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued3_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['children_rescued_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued2_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued3_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['people_injured_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured2_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured3_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['children_injured_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured2_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured3_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['people_died_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died2_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died3_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['children_died_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died2_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died3_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['zaminuvanya'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            type_of_fire_id=15).count()

        context['zaminuvanya2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            type_of_fire_id=15).count()

        context['zaminuvanya3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            type_of_fire_id=15).count()

        context['zaminuvanya_object'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=15).aggregate(
            sum=Coalesce(Sum('quantity_objects'), 0))

        context['zaminuvanya2_object'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=15).aggregate(
            sum=Coalesce(Sum('quantity_objects'), 0))

        context['zaminuvanya3_object'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=15).aggregate(
            sum=Coalesce(Sum('quantity_objects'), 0))

        context['inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            type_of_fire_id=11).count()

        context['inshi2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            type_of_fire_id=11).count()

        context['inshi3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            type_of_fire_id=11).count()

        context['kz'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            subtype=16).count()

        context['kz2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            subtype=16).count()

        context['kz3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            subtype=16).count()

        context['prigoranya_izhi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            subtype=17).count()

        context['prigoranya_izhi2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            subtype=17).count()

        context['prigoranya_izhi3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            subtype=17).count()

        context['info_ne_pidt'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            subtype=18).count()

        context['info_ne_pidt2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            subtype=18).count()

        context['info_ne_pidt3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            subtype=18).count()

        return context

    def render_to_response(self, context, **response_kwargs):
        """
        check on the authenticated user
        """
        if self.request.user.is_authenticated:
            return super(StatisticJournal1, self).render_to_response(context, **response_kwargs)
        else:
            messages.warning(self.request, 'Схоже ви намагаєтеся зайти Не Авторизувавшись')
            return redirect('login')


class StatisticJournal2(ListView):
    """
    Statistics journal by type and category
    Page 2
    """
    model = Journal
    template_name = 'journal/statistic_journal_page2.html'
    context_object_name = 'statistic_journal'

    def get_context_data(self, **kwargs):
        """
        Rendering template statistic_journal_page1.html
        """
        datetime_range = [f"{format_datetime(datetime.today() - timedelta(days=2), 'Y-MM-dd')} 00:00",
                          f"{format_datetime(datetime.today() - timedelta(days=2), 'Y-MM-dd')} 06:00"]
        datetime_range2 = [f"{format_datetime(datetime.today() - timedelta(days=2), 'Y-MM-dd')} 06:00",
                           f"{format_datetime(datetime.today() - timedelta(days=2), 'Y-MM-dd')} 23:59"]
        datetime_range3 = [f"{format_datetime(datetime.today() - timedelta(days=2), 'Y-MM-dd')} 00:00",
                           f"{format_datetime(datetime.today() - timedelta(days=2), 'Y-MM-dd')} 23:59"]
        context = super(StatisticJournal2, self).get_context_data(**kwargs)
        context['title'] = 'Статистика викликів'
        context['page1'] = datetime.today() - timedelta(days=1)
        context['page2'] = datetime.today() - timedelta(days=2)
        context['page3'] = datetime.today() - timedelta(days=3)
        context['form'] = DepartureStatisticsForm()
        context['departures'] = self.model.objects.filter(date_of_receipt_message__range=datetime_range,
                                                          category_id=25).count() + \
                                self.model.objects.filter(date_of_receipt_message__range=datetime_range,
                                                          category_id=26).count() + \
                                self.model.objects.filter(date_of_receipt_message__range=datetime_range,
                                                          category_id=28).count()

        context['departures2'] = self.model.objects.filter(date_of_receipt_message__range=datetime_range2,
                                                           category_id=25).count() + \
                                 self.model.objects.filter(date_of_receipt_message__range=datetime_range2,
                                                           category_id=26).count() + \
                                 self.model.objects.filter(date_of_receipt_message__range=datetime_range2,
                                                           category_id=28).count()

        context['departures3'] = self.model.objects.filter(date_of_receipt_message__range=datetime_range3,
                                                           category_id=25).count() + \
                                 self.model.objects.filter(date_of_receipt_message__range=datetime_range3,
                                                           category_id=26).count() + \
                                 self.model.objects.filter(date_of_receipt_message__range=datetime_range3,
                                                           category_id=28).count()

        context['events'] = self.model.objects.filter(date_of_receipt_message__range=datetime_range,
                                                      category_id=25).count() + \
                            self.model.objects.filter(date_of_receipt_message__range=datetime_range,
                                                      category_id=27).count()

        context['events2'] = self.model.objects.filter(date_of_receipt_message__range=datetime_range2,
                                                       category_id=25).count() + \
                             self.model.objects.filter(date_of_receipt_message__range=datetime_range2,
                                                       category_id=27).count()

        context['events3'] = self.model.objects.filter(date_of_receipt_message__range=datetime_range3,
                                                       category_id=25).count() + \
                             self.model.objects.filter(date_of_receipt_message__range=datetime_range3,
                                                       category_id=27).count()

        context['ns'] = self.model.objects.filter(date_of_receipt_message__range=datetime_range,
                                                  category_id=28).count() + \
                        self.model.objects.filter(date_of_receipt_message__range=datetime_range,
                                                  category_id=29).count()

        context['ns2'] = self.model.objects.filter(date_of_receipt_message__range=datetime_range2,
                                                   category_id=28).count() + \
                         self.model.objects.filter(date_of_receipt_message__range=datetime_range2,
                                                   category_id=29).count()

        context['ns3'] = self.model.objects.filter(date_of_receipt_message__range=datetime_range3,
                                                   category_id=28).count() + \
                         self.model.objects.filter(date_of_receipt_message__range=datetime_range3,
                                                   category_id=29).count()

        context['people_rescued'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['children_rescued'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['people_injured'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['children_injured'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['people_died'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['children_died'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['quantity_peoples'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_peoples'), 0))

        context['quantity_peoples2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2).aggregate(
            sum=Coalesce(Sum('quantity_peoples'), 0))

        context['quantity_peoples3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3).aggregate(
            sum=Coalesce(Sum('quantity_peoples'), 0))

        context['quantity_technics'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_technics'), 0))

        context['quantity_technics2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2).aggregate(
            sum=Coalesce(Sum('quantity_technics'), 0))

        context['quantity_technics3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3).aggregate(
            sum=Coalesce(Sum('quantity_technics'), 0))

        context['fire'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                type_of_fire_id=8).count()

        context['fire2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                type_of_fire_id=8).count()

        context['fire3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                type_of_fire_id=8).count()

        context['dwelling'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=1).count()

        context['dwelling2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=1).count()

        context['dwelling3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=1).count()

        context['notdwelling'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=2).count()

        context['notdwelling2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=2).count()

        context['notdwelling3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=2).count()

        context['object'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=3).count()

        context['object2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=3).count()

        context['object3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=3).count()

        context['min_oborony'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=4).count()

        context['min_oborony2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=4).count()

        context['min_oborony3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=4).count()

        context['ukr_zaliz'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=5).count()

        context['ukr_zaliz2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=5).count()

        context['ukr_zaliz3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=5).count()

        context['lis'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=7).count()

        context['lis2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=7).count()

        context['lis3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=7).count()

        context['count_lis'] = \
            sum([item.area2 for item in
                 self.model.objects.filter(
                     date_of_receipt_message__range=datetime_range3,
                     subtype=7)])

        context['trava'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=8).count()

        context['trava2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=8).count()

        context['trava3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=8).count()

        context['count_trava'] = \
            sum([item.area2 for item in
                 self.model.objects.filter(
                     date_of_receipt_message__range=datetime_range3,
                     subtype=8)])

        context['smitya'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=9).count()

        context['smitya2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=9).count()

        context['smitya3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=9).count()

        context['count_smitya'] = \
            sum([item.area2 for item in
                 self.model.objects.filter(
                     date_of_receipt_message__range=datetime_range3,
                     subtype=9)])

        context['selo'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=10).count()

        context['selo2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=10).count()

        context['selo3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=10).count()

        context['count_selo'] = \
            sum([item.area2 for item in
                 self.model.objects.filter(
                     date_of_receipt_message__range=datetime_range3,
                     subtype=10)])

        context['torf'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=11).count()

        context['torf2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=11).count()

        context['torf3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=11).count()

        context['count_torf'] = \
            sum([item.area2 for item in
                 self.model.objects.filter(
                     date_of_receipt_message__range=datetime_range3,
                     subtype=11)])

        context['ecosystems'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=7).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=8).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=9).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=10).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=11).count()

        context['ecosystems2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=7).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=8).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=9).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=10).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=11).count()

        context['ecosystems3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=7).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=8).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=9).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=10).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=11).count()

        context['count_ecosystems'] = \
            sum(
                [
                    sum(
                        [item.area2 for item in
                         self.model.objects.filter(
                             date_of_receipt_message__range=datetime_range3,
                             subtype=7)]),
                    sum(
                        [item.area2 for item in
                         self.model.objects.filter(
                             date_of_receipt_message__range=datetime_range3,
                             subtype=8)]),

                    sum(
                        [item.area2 for item in
                         self.model.objects.filter(
                             date_of_receipt_message__range=datetime_range3,
                             subtype=9)]),
                    sum(
                        [item.area2 for item in
                         self.model.objects.filter(
                             date_of_receipt_message__range=datetime_range3,
                             subtype=10)]),
                    sum(
                        [item.area2 for item in
                         self.model.objects.filter(
                             date_of_receipt_message__range=datetime_range3,
                             subtype=11)])
                ]

            )

        context['avto'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=13).count()

        context['avto2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=13).count()

        context['avto3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=13).count()

        context['zalizn'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=14).count()

        context['zalizn2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=14).count()

        context['zalizn3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=14).count()

        context['avia'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=15).count()

        context['avia2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=15).count()

        context['avia3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=15).count()

        context['transports'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=13).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=14).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=15).count()

        context['transports2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=13).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=14).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=15).count()

        context['transports3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=13).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=14).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=15).count()

        context['people_rescued_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued2_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued3_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['children_rescued_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued2_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued3_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['people_injured_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured2_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured3_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['children_injured_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured2_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured3_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['people_died_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died2_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died3_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['children_died_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died2_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died3_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['dopomoga'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                type_of_fire_id=12).count()

        context['dopomoga2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                type_of_fire_id=12).count()

        context['dopomoga3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                type_of_fire_id=12).count()

        context['dtp'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=19).count()

        context['dtp2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=19).count()

        context['dtp3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=19).count()

        context['dtp_podiya'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=20).count()

        context['dtp_podiya2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=20).count()

        context['dtp_podiya3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=20).count()

        context['dopomoga_nas'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=21).count()

        context['dopomoga_nas2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=21).count()

        context['dopomoga_nas3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=21).count()

        context['dopomoga102'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=22).count()

        context['dopomoga102_2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=22).count()

        context['dopomoga102_3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=22).count()

        context['dopomoga103'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=23).count()

        context['dopomoga103_2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=23).count()

        context['dopomoga103_3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=23).count()

        context['dopomoga104'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=24).count()

        context['dopomoga104_2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=24).count()

        context['dopomoga104_3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=24).count()

        context['podiya_na_vodi'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=25).count()

        context['podiya_na_vodi2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=25).count()

        context['podiya_na_vodi3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=25).count()

        context['podiya_inshi'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=26).count()

        context['podiya_inshi2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=26).count()

        context['podiya_inshi3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=26).count()

        context['parnokopitni'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=27).count()

        context['parnokopitni2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=27).count()

        context['parnokopitni3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=27).count()

        context['dog'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=28).count()

        context['dog2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=28).count()

        context['dog3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=28).count()

        context['cat'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=29).count()

        context['cat2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=29).count()

        context['cat3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=29).count()

        context['plazuni'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=30).count()

        context['plazuni2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=30).count()

        context['plazuni3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=30).count()

        context['tvar_inshi'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=31).count()

        context['tvar_inshi2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=31).count()

        context['tvar_inshi3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=31).count()

        context['zag_tvar'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=27).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=28).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=29).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=30).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=31).count()

        context['zag_tvar2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=27).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=28).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=29).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=30).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=31).count()

        context['zag_tvar3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=27).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=28).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=29).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=30).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=31).count()

        context['san_obrobka'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=37).count()

        context['san_obrobka2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=37).count()

        context['san_obrobka3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=37).count()

        context['opendoors'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=38).count()

        context['opendoors2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=38).count()

        context['opendoors3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=38).count()

        context['opencar'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=39).count()

        context['opencar2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=39).count()

        context['opencar3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=39).count()

        context['people_rescued_dopomoga'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=12).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued2_dopomoga'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=12).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued3_dopomoga'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=12).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['children_rescued_dopomoga'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=12).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued2_dopomoga'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=12).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued3_dopomoga'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=12).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['people_rescued_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued2_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued3_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['children_rescued_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued2_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued3_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['people_injured_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured2_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured3_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['children_injured_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured2_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured3_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['people_died_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died2_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died3_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['children_died_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died2_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died3_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['people_rescued_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued2_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued3_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['children_rescued_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued2_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued3_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['people_injured_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured2_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured3_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['children_injured_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured2_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured3_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['people_died_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died2_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died3_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['children_died_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died2_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died3_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['people_rescued_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued2_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued3_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['children_rescued_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued2_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued3_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['people_injured_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured2_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured3_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['children_injured_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured2_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured3_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['people_died_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died2_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died3_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['children_died_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died2_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died3_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['vnp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            type_of_fire_id=13).count()

        context['vnp2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            type_of_fire_id=13).count()

        context['vnp3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            type_of_fire_id=13).count()

        context['quantity_vnp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=13).aggregate(
            sum=Coalesce(Sum('quantity_ammunition'), 0))

        context['quantity_vnp2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=13).aggregate(
            sum=Coalesce(Sum('quantity_ammunition'), 0))

        context['quantity_vnp3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=13).aggregate(
            sum=Coalesce(Sum('quantity_ammunition'), 0))

        context['hibniy_viklik'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            type_of_fire_id=9).count()

        context['hibniy_viklik2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            type_of_fire_id=9).count()

        context['hibniy_viklik3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            type_of_fire_id=9).count()

        context['aps'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            type_of_fire_id=10).count()

        context['aps2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            type_of_fire_id=10).count()

        context['aps3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            type_of_fire_id=10).count()

        context['ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            type_of_fire_id=14).count()

        context['ns2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            type_of_fire_id=14).count()

        context['ns3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            type_of_fire_id=14).count()

        context['tehno_haracter'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            subtype=32).count()

        context['tehno_haracter2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            subtype=32).count()

        context['tehno_haracter3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            subtype=32).count()

        context['prirodnogo_haracter'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            subtype=33).count()

        context['prirodnogo_haracter2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            subtype=33).count()

        context['prirodnogo_haracter3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            subtype=33).count()

        context['social_haracter'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            subtype=34).count()

        context['social_haracter2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            subtype=34).count()

        context['social_haracter3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            subtype=34).count()

        context['voen_haracter'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            subtype=35).count()

        context['voen_haracter2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            subtype=35).count()

        context['voen_haracter3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            subtype=35).count()

        context['quantity_umovi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('violated_conditions'), 0))

        context['quantity_umovi2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('violated_conditions'), 0))

        context['quantity_umovi3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('violated_conditions'), 0))

        context['people_rescued_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued2_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued3_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['children_rescued_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued2_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued3_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['people_injured_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured2_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured3_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['children_injured_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured2_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured3_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['people_died_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died2_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died3_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['children_died_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died2_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died3_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['zaminuvanya'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            type_of_fire_id=15).count()

        context['zaminuvanya2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            type_of_fire_id=15).count()

        context['zaminuvanya3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            type_of_fire_id=15).count()

        context['zaminuvanya_object'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=15).aggregate(
            sum=Coalesce(Sum('quantity_objects'), 0))

        context['zaminuvanya2_object'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=15).aggregate(
            sum=Coalesce(Sum('quantity_objects'), 0))

        context['zaminuvanya3_object'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=15).aggregate(
            sum=Coalesce(Sum('quantity_objects'), 0))

        context['inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            type_of_fire_id=11).count()

        context['inshi2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            type_of_fire_id=11).count()

        context['inshi3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            type_of_fire_id=11).count()

        context['kz'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            subtype=16).count()

        context['kz2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            subtype=16).count()

        context['kz3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            subtype=16).count()

        context['prigoranya_izhi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            subtype=17).count()

        context['prigoranya_izhi2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            subtype=17).count()

        context['prigoranya_izhi3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            subtype=17).count()

        context['info_ne_pidt'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            subtype=18).count()

        context['info_ne_pidt2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            subtype=18).count()

        context['info_ne_pidt3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            subtype=18).count()

        return context

    def render_to_response(self, context, **response_kwargs):
        """
        check on the authenticated user
        """
        if self.request.user.is_authenticated:
            return super(StatisticJournal2, self).render_to_response(context, **response_kwargs)
        else:
            messages.warning(self.request, 'Схоже ви намагаєтеся зайти Не Авторизувавшись')
            return redirect('login')


class StatisticJournal3(ListView):
    """
    Statistics journal by type and category
    Page 3
    """
    model = Journal
    template_name = 'journal/statistic_journal_page3.html'
    context_object_name = 'statistic_journal'

    def get_context_data(self, **kwargs):
        """
        Rendering template statistic_journal_page1.html
        """
        datetime_range = [f"{format_datetime(datetime.today() - timedelta(days=3), 'Y-MM-dd')} 00:00",
                          f"{format_datetime(datetime.today() - timedelta(days=3), 'Y-MM-dd')} 06:00"]
        datetime_range2 = [f"{format_datetime(datetime.today() - timedelta(days=3), 'Y-MM-dd')} 06:00",
                           f"{format_datetime(datetime.today() - timedelta(days=3), 'Y-MM-dd')} 23:59"]
        datetime_range3 = [f"{format_datetime(datetime.today() - timedelta(days=3), 'Y-MM-dd')} 00:00",
                           f"{format_datetime(datetime.today() - timedelta(days=3), 'Y-MM-dd')} 23:59"]
        context = super(StatisticJournal3, self).get_context_data(**kwargs)
        context['title'] = 'Статистика викликів'
        context['page1'] = datetime.today() - timedelta(days=1)
        context['page2'] = datetime.today() - timedelta(days=2)
        context['page3'] = datetime.today() - timedelta(days=3)
        context['form'] = DepartureStatisticsForm()
        context['departures'] = self.model.objects.filter(date_of_receipt_message__range=datetime_range,
                                                          category_id=25).count() + \
                                self.model.objects.filter(date_of_receipt_message__range=datetime_range,
                                                          category_id=26).count() + \
                                self.model.objects.filter(date_of_receipt_message__range=datetime_range,
                                                          category_id=28).count()

        context['departures2'] = self.model.objects.filter(date_of_receipt_message__range=datetime_range2,
                                                           category_id=25).count() + \
                                 self.model.objects.filter(date_of_receipt_message__range=datetime_range2,
                                                           category_id=26).count() + \
                                 self.model.objects.filter(date_of_receipt_message__range=datetime_range2,
                                                           category_id=28).count()

        context['departures3'] = self.model.objects.filter(date_of_receipt_message__range=datetime_range3,
                                                           category_id=25).count() + \
                                 self.model.objects.filter(date_of_receipt_message__range=datetime_range3,
                                                           category_id=26).count() + \
                                 self.model.objects.filter(date_of_receipt_message__range=datetime_range3,
                                                           category_id=28).count()

        context['events'] = self.model.objects.filter(date_of_receipt_message__range=datetime_range,
                                                      category_id=25).count() + \
                            self.model.objects.filter(date_of_receipt_message__range=datetime_range,
                                                      category_id=27).count()

        context['events2'] = self.model.objects.filter(date_of_receipt_message__range=datetime_range2,
                                                       category_id=25).count() + \
                             self.model.objects.filter(date_of_receipt_message__range=datetime_range2,
                                                       category_id=27).count()

        context['events3'] = self.model.objects.filter(date_of_receipt_message__range=datetime_range3,
                                                       category_id=25).count() + \
                             self.model.objects.filter(date_of_receipt_message__range=datetime_range3,
                                                       category_id=27).count()

        context['ns'] = self.model.objects.filter(date_of_receipt_message__range=datetime_range,
                                                  category_id=28).count() + \
                        self.model.objects.filter(date_of_receipt_message__range=datetime_range,
                                                  category_id=29).count()

        context['ns2'] = self.model.objects.filter(date_of_receipt_message__range=datetime_range2,
                                                   category_id=28).count() + \
                         self.model.objects.filter(date_of_receipt_message__range=datetime_range2,
                                                   category_id=29).count()

        context['ns3'] = self.model.objects.filter(date_of_receipt_message__range=datetime_range3,
                                                   category_id=28).count() + \
                         self.model.objects.filter(date_of_receipt_message__range=datetime_range3,
                                                   category_id=29).count()

        context['people_rescued'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['children_rescued'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['people_injured'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['children_injured'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['people_died'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['children_died'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['quantity_peoples'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_peoples'), 0))

        context['quantity_peoples2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2).aggregate(
            sum=Coalesce(Sum('quantity_peoples'), 0))

        context['quantity_peoples3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3).aggregate(
            sum=Coalesce(Sum('quantity_peoples'), 0))

        context['quantity_technics'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_technics'), 0))

        context['quantity_technics2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2).aggregate(
            sum=Coalesce(Sum('quantity_technics'), 0))

        context['quantity_technics3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3).aggregate(
            sum=Coalesce(Sum('quantity_technics'), 0))

        context['fire'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                type_of_fire_id=8).count()

        context['fire2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                type_of_fire_id=8).count()

        context['fire3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                type_of_fire_id=8).count()

        context['dwelling'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=1).count()

        context['dwelling2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=1).count()

        context['dwelling3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=1).count()

        context['notdwelling'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=2).count()

        context['notdwelling2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=2).count()

        context['notdwelling3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=2).count()

        context['object'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=3).count()

        context['object2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=3).count()

        context['object3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=3).count()

        context['min_oborony'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=4).count()

        context['min_oborony2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=4).count()

        context['min_oborony3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=4).count()

        context['ukr_zaliz'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=5).count()

        context['ukr_zaliz2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=5).count()

        context['ukr_zaliz3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=5).count()

        context['lis'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=7).count()

        context['lis2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=7).count()

        context['lis3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=7).count()

        context['count_lis'] = \
            sum([item.area2 for item in
                 self.model.objects.filter(
                     date_of_receipt_message__range=datetime_range3,
                     subtype=7)])

        context['trava'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=8).count()

        context['trava2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=8).count()

        context['trava3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=8).count()

        context['count_trava'] = \
            sum([item.area2 for item in
                 self.model.objects.filter(
                     date_of_receipt_message__range=datetime_range3,
                     subtype=8)])

        context['smitya'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=9).count()

        context['smitya2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=9).count()

        context['smitya3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=9).count()

        context['count_smitya'] = \
            sum([item.area2 for item in
                 self.model.objects.filter(
                     date_of_receipt_message__range=datetime_range3,
                     subtype=9)])

        context['selo'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=10).count()

        context['selo2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=10).count()

        context['selo3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=10).count()

        context['count_selo'] = \
            sum([item.area2 for item in
                 self.model.objects.filter(
                     date_of_receipt_message__range=datetime_range3,
                     subtype=10)])

        context['torf'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=11).count()

        context['torf2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=11).count()

        context['torf3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=11).count()

        context['count_torf'] = \
            sum([item.area2 for item in
                 self.model.objects.filter(
                     date_of_receipt_message__range=datetime_range3,
                     subtype=11)])

        context['ecosystems'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=7).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=8).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=9).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=10).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=11).count()

        context['ecosystems2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=7).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=8).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=9).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=10).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=11).count()

        context['ecosystems3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=7).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=8).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=9).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=10).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=11).count()

        context['count_ecosystems'] = \
            sum(
                [
                    sum(
                        [item.area2 for item in
                         self.model.objects.filter(
                             date_of_receipt_message__range=datetime_range3,
                             subtype=7)]),
                    sum(
                        [item.area2 for item in
                         self.model.objects.filter(
                             date_of_receipt_message__range=datetime_range3,
                             subtype=8)]),

                    sum(
                        [item.area2 for item in
                         self.model.objects.filter(
                             date_of_receipt_message__range=datetime_range3,
                             subtype=9)]),
                    sum(
                        [item.area2 for item in
                         self.model.objects.filter(
                             date_of_receipt_message__range=datetime_range3,
                             subtype=10)]),
                    sum(
                        [item.area2 for item in
                         self.model.objects.filter(
                             date_of_receipt_message__range=datetime_range3,
                             subtype=11)])
                ]

            )

        context['avto'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=13).count()

        context['avto2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=13).count()

        context['avto3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=13).count()

        context['zalizn'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=14).count()

        context['zalizn2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=14).count()

        context['zalizn3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=14).count()

        context['avia'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=15).count()

        context['avia2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=15).count()

        context['avia3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=15).count()

        context['transports'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=13).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=14).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=15).count()

        context['transports2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=13).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=14).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=15).count()

        context['transports3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=13).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=14).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=15).count()

        context['people_rescued_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued2_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued3_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['children_rescued_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued2_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued3_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['people_injured_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured2_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured3_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['children_injured_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured2_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured3_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['people_died_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died2_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died3_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['children_died_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died2_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died3_fire'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=8).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['dopomoga'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                type_of_fire_id=12).count()

        context['dopomoga2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                type_of_fire_id=12).count()

        context['dopomoga3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                type_of_fire_id=12).count()

        context['dtp'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=19).count()

        context['dtp2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=19).count()

        context['dtp3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=19).count()

        context['dtp_podiya'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=20).count()

        context['dtp_podiya2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=20).count()

        context['dtp_podiya3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=20).count()

        context['dopomoga_nas'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=21).count()

        context['dopomoga_nas2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=21).count()

        context['dopomoga_nas3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=21).count()

        context['dopomoga102'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=22).count()

        context['dopomoga102_2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=22).count()

        context['dopomoga102_3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=22).count()

        context['dopomoga103'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=23).count()

        context['dopomoga103_2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=23).count()

        context['dopomoga103_3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=23).count()

        context['dopomoga104'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=24).count()

        context['dopomoga104_2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=24).count()

        context['dopomoga104_3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=24).count()

        context['podiya_na_vodi'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=25).count()

        context['podiya_na_vodi2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=25).count()

        context['podiya_na_vodi3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=25).count()

        context['podiya_inshi'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=26).count()

        context['podiya_inshi2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=26).count()

        context['podiya_inshi3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=26).count()

        context['parnokopitni'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=27).count()

        context['parnokopitni2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=27).count()

        context['parnokopitni3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=27).count()

        context['dog'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=28).count()

        context['dog2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=28).count()

        context['dog3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=28).count()

        context['cat'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=29).count()

        context['cat2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=29).count()

        context['cat3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=29).count()

        context['plazuni'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=30).count()

        context['plazuni2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=30).count()

        context['plazuni3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=30).count()

        context['tvar_inshi'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=31).count()

        context['tvar_inshi2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=31).count()

        context['tvar_inshi3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=31).count()

        context['zag_tvar'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=27).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=28).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=29).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=30).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=31).count()

        context['zag_tvar2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=27).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=28).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=29).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=30).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=31).count()

        context['zag_tvar3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=27).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=28).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=29).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=30).count() + \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=31).count()

        context['san_obrobka'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=37).count()

        context['san_obrobka2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=37).count()

        context['san_obrobka3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=37).count()

        context['opendoors'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=38).count()

        context['opendoors2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=38).count()

        context['opendoors3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=38).count()

        context['opencar'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range,
                subtype=39).count()

        context['opencar2'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range2,
                subtype=39).count()

        context['opencar3'] = \
            self.model.objects.filter(
                date_of_receipt_message__range=datetime_range3,
                subtype=39).count()

        context['people_rescued_dopomoga'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=12).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued2_dopomoga'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=12).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued3_dopomoga'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=12).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['children_rescued_dopomoga'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=12).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued2_dopomoga'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=12).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued3_dopomoga'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=12).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['people_rescued_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued2_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued3_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['children_rescued_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued2_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued3_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['people_injured_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured2_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured3_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['children_injured_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured2_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured3_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['people_died_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died2_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died3_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['children_died_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died2_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died3_dtp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=20).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['people_rescued_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued2_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued3_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['children_rescued_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued2_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued3_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['people_injured_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured2_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured3_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['children_injured_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured2_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured3_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['people_died_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died2_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died3_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['children_died_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died2_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died3_voda'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=25).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['people_rescued_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued2_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued3_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['children_rescued_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued2_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued3_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['people_injured_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured2_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured3_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['children_injured_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured2_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured3_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['people_died_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died2_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died3_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['children_died_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died2_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died3_inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, subtype=26).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['vnp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            type_of_fire_id=13).count()

        context['vnp2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            type_of_fire_id=13).count()

        context['vnp3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            type_of_fire_id=13).count()

        context['quantity_vnp'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=13).aggregate(
            sum=Coalesce(Sum('quantity_ammunition'), 0))

        context['quantity_vnp2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=13).aggregate(
            sum=Coalesce(Sum('quantity_ammunition'), 0))

        context['quantity_vnp3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=13).aggregate(
            sum=Coalesce(Sum('quantity_ammunition'), 0))

        context['hibniy_viklik'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            type_of_fire_id=9).count()

        context['hibniy_viklik2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            type_of_fire_id=9).count()

        context['hibniy_viklik3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            type_of_fire_id=9).count()

        context['aps'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            type_of_fire_id=10).count()

        context['aps2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            type_of_fire_id=10).count()

        context['aps3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            type_of_fire_id=10).count()

        context['ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            type_of_fire_id=14).count()

        context['ns2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            type_of_fire_id=14).count()

        context['ns3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            type_of_fire_id=14).count()

        context['tehno_haracter'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            subtype=32).count()

        context['tehno_haracter2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            subtype=32).count()

        context['tehno_haracter3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            subtype=32).count()

        context['prirodnogo_haracter'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            subtype=33).count()

        context['prirodnogo_haracter2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            subtype=33).count()

        context['prirodnogo_haracter3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            subtype=33).count()

        context['social_haracter'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            subtype=34).count()

        context['social_haracter2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            subtype=34).count()

        context['social_haracter3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            subtype=34).count()

        context['voen_haracter'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            subtype=35).count()

        context['voen_haracter2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            subtype=35).count()

        context['voen_haracter3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            subtype=35).count()

        context['quantity_umovi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('violated_conditions'), 0))

        context['quantity_umovi2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('violated_conditions'), 0))

        context['quantity_umovi3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('violated_conditions'), 0))

        context['people_rescued_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued2_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['people_rescued3_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        context['children_rescued_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued2_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['children_rescued3_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        context['people_injured_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured2_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['people_injured3_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        context['children_injured_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured2_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['children_injured3_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        context['people_died_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died2_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['people_died3_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        context['children_died_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died2_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['children_died3_ns'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=14).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        context['zaminuvanya'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            type_of_fire_id=15).count()

        context['zaminuvanya2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            type_of_fire_id=15).count()

        context['zaminuvanya3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            type_of_fire_id=15).count()

        context['zaminuvanya_object'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range, type_of_fire_id=15).aggregate(
            sum=Coalesce(Sum('quantity_objects'), 0))

        context['zaminuvanya2_object'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2, type_of_fire_id=15).aggregate(
            sum=Coalesce(Sum('quantity_objects'), 0))

        context['zaminuvanya3_object'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3, type_of_fire_id=15).aggregate(
            sum=Coalesce(Sum('quantity_objects'), 0))

        context['inshi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            type_of_fire_id=11).count()

        context['inshi2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            type_of_fire_id=11).count()

        context['inshi3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            type_of_fire_id=11).count()

        context['kz'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            subtype=16).count()

        context['kz2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            subtype=16).count()

        context['kz3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            subtype=16).count()

        context['prigoranya_izhi'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            subtype=17).count()

        context['prigoranya_izhi2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            subtype=17).count()

        context['prigoranya_izhi3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            subtype=17).count()

        context['info_ne_pidt'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range,
            subtype=18).count()

        context['info_ne_pidt2'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range2,
            subtype=18).count()

        context['info_ne_pidt3'] = self.model.objects.filter(
            date_of_receipt_message__range=datetime_range3,
            subtype=18).count()

        return context

    def render_to_response(self, context, **response_kwargs):
        """
        check on the authenticated user
        """
        if self.request.user.is_authenticated:
            return super(StatisticJournal3, self).render_to_response(context, **response_kwargs)
        else:
            messages.warning(self.request, 'Схоже ви намагаєтеся зайти Не Авторизувавшись')
            return redirect('login')
