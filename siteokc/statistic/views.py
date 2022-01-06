from datetime import datetime, timedelta
from django.db.models import Sum
from django.views.generic import ListView
from django.shortcuts import redirect
from .models import *
from babel.dates import format_datetime
from .forms import StatisticForms
from django.contrib import messages
from django.db.models.functions import Coalesce


# Create your views here.

class StatisticCalls(ListView):
    model = Statistic
    template_name = 'statistic/statistic_calls.html'
    context_object_name = 'statistic'

    def get_context_data(self, **kwargs):
        # Render statistic_calls.html
        context = super().get_context_data(**kwargs)
        context['title'] = 'Статистика дзвінків'
        context['date'] = format_datetime(datetime.today() - timedelta(days=1), "EEEE  d MMMM Y року",
                                          locale='uk_UA')
        context['form'] = StatisticForms()
        context['number_101'] = self.number_101()
        context['days7_101'] = self.number_101_days7()
        context['month_101'] = self.number_101_month()
        context['number_112'] = \
            self.model.objects.filter(date=format_datetime(datetime.today() - timedelta(days=1), "Y-MM-dd"),
                                      subdivisions_id=1).aggregate(sum=Coalesce(Sum('number_of_calls'), 0))

        context['total'] = \
            self.model.objects.filter(date=format_datetime(datetime.today() - timedelta(days=1), "Y-MM-dd")).aggregate(
                sum=Coalesce(Sum('number_of_calls'), 0))

        context['days7'] = \
            self.model.objects.filter(
                date__range=[format_datetime(datetime.today() - timedelta(days=7), "Y-MM-dd"),
                             format_datetime(datetime.today() - timedelta(days=1), "Y-MM-dd")]).aggregate(
                sum=Coalesce(Sum('number_of_calls'), 0))

        context['days7_112'] = \
            self.model.objects.filter(
                date__range=[format_datetime(datetime.today() - timedelta(days=7), "Y-MM-dd"),
                             format_datetime(datetime.today() - timedelta(days=1), "Y-MM-dd")],
                subdivisions_id=1).aggregate(sum=Coalesce(Sum('number_of_calls'), 0))

        context['month_112'] = \
            self.model.objects.filter(date__month=datetime.today().month, subdivisions_id=1).aggregate(
                sum=Coalesce(Sum('number_of_calls'), 0))

        context['total_month'] = \
            self.model.objects.filter(date__month=datetime.today().month).aggregate(
                sum=Coalesce(Sum('number_of_calls'), 0))
        return context

    def render_to_response(self, context, **response_kwargs):
        """
        The check on authenticated
        """
        if self.request.user.is_authenticated:
            return super(StatisticCalls, self).render_to_response(context, **response_kwargs)
        else:
            messages.warning(self.request, 'Схоже ви намагаєтеся зайти Не Авторизувавшись')
            return redirect('login')

    def get_queryset(self):
        return Statistic.objects.filter(date=format_datetime(datetime.today() - timedelta(days=1), "Y-MM-dd"))

    def number_101(self):
        """
        Return number of calls to number 101
        """
        number_101 = (sum([item.number_of_calls for item in
                           self.model.objects.filter(
                               date=format_datetime(datetime.today() - timedelta(days=1), "Y-MM-dd"))])
                      -
                      sum([item.number_of_calls for item in
                           self.model.objects.filter(
                               date=format_datetime(datetime.today() - timedelta(days=1), "Y-MM-dd"),
                               subdivisions_id=1)]))
        return int(number_101)

    def number_101_days7(self):
        """
        Return number of calls to number 101 in the 7 days
        """
        number_101_days7 = (sum([item.number_of_calls for item in
                                 self.model.objects.filter(
                                     date__range=[format_datetime(datetime.today() - timedelta(days=7), "Y-MM-dd"),
                                                  format_datetime(datetime.today() - timedelta(days=1), "Y-MM-dd")])])
                            -
                            sum([item.number_of_calls for item in
                                 self.model.objects.filter(
                                     date__range=[format_datetime(datetime.today() - timedelta(days=7), "Y-MM-dd"),
                                                  format_datetime(datetime.today() - timedelta(days=1), "Y-MM-dd")],
                                     subdivisions_id=1)]))
        return int(number_101_days7)

    def number_101_month(self):
        """
        Return number of calls to number 101 in the month
        """
        number_101_month = (sum([item.number_of_calls for item in
                                 self.model.objects.filter(date__month=datetime.today().month)])
                            -
                            sum([item.number_of_calls for item in
                                 self.model.objects.filter(date__month=datetime.today().month, subdivisions_id=1)]))
        return int(number_101_month)


def statistic_add(request):
    if request.method == 'POST':
        form = StatisticForms(request.POST)
        if form.is_valid():
            if Statistic.objects.filter(date=form.instance.date, subdivisions=form.instance.subdivisions):
                messages.warning(request,
                                 f'Ваш підрозділ вже передав статистику за: '
                                 f"{format_datetime(form.instance.date, 'EEEE  d MMMM Y року', locale='uk_UA')}")
                return redirect('statistic')
            if form.instance.number_of_calls < 0:
                messages.warning(request, 'Кількість дзвінків не може бути менше 0!')
                return redirect('statistic')
            else:
                obj = form.save(commit=False)
                obj.add_user = f'{request.user.first_name}\n ' \
                               f'{request.user.last_name}'
                obj.save()
                messages.success(request, f'Статистику підрозділу {form.instance.subdivisions} успішно передано!')
                return redirect('statistic')
        else:
            messages.error(request, 'Помилка при передачі статистики!')
            return redirect('statistic')

    else:
        return redirect('statistic')
