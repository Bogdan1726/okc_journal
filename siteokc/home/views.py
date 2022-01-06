from datetime import datetime
from babel.dates import format_datetime
from django.contrib import messages
from django.db.models import Count, Sum
from django.db.models.functions import Coalesce
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from journal.models import Journal
from .models import News, Category


# Create your views here.


def index(request):
    if request.user.is_authenticated:
        context = {
            'title': 'Головна сторінка',
            'dnipro': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=1),
            'solone': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=2),
            'sursko_litovske': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=15),
            'novooleksandrivka': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=16),
            'lubimivka': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=17),
            'mukolaivka': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=18),
            'svyatovasilivka': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=19),
            'novopokrovka': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=20),
            'slobozhanske': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=21),
            'pidgorodne': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=22),
            'obuhivka': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=23),
            'chumaki': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=24),
            'petrikivka': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=25),
            'mogiliv': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=26),
            'kitaygorod': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=27),
            'carichanka': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=28),
            'lyashkivka': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=29),
            'kamyanske': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=3),
            'verhivcevo': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=4),
            'krinichki': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=30),
            'zatishne': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=31),
            'bozhedarivka': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=32),
            'saksagany': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=33),
            'pyatihatki': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=34),
            'zhovti_vodi': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=35),
            'vishneve': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=36),
            'vilynogirsk': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=37),
            'verhnyodniprovsk': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=38),
            'lihivka': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=39),
            'kriviy_rig': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=5),
            'sofiivka': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=6),
            'novopillya': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=40),
            'gleyuvatka': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=41),
            'lozuvatka': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=42),
            'devladove': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=43),
            'vakulove': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=44),
            'grechani_podi': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=45),
            'novolativka': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=46),
            'niva_trudova': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=47),
            'shiroke': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=48),
            'apostolove': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=49),
            'karpivka': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=50),
            'zelenodolsk': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=51),
            'grushivka': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=52),
            'nikopol': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=7),
            'marganec': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=8),
            'chervonogrigorivka': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=53),
            'pokrovske': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=54),
            'pokrov': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=55),
            'pershotravneve': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=56),
            'mirove': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=57),
            'tomakivka': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=58),
            'novomoskovsk': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=9),
            'gubiniha': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=10),
            'pishanka': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=59),
            'cherkaske': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=60),
            'magdalinivka': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=61),
            'pereshepino': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=62),
            'lichkove': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=63),
            'chernichina': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=64),
            'pavlograd': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=11),
            'ternivka': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=12),
            'bogdanivka': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=65),
            'troicke': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=66),
            'mezhirich': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=67),
            'verbki': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=68),
            'urivka': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=69),
            'sinelnikove': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=13),
            'vasilkivka': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=14),
            'ilarionove': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=70),
            'zayceve': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=71),
            'raivka': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=72),
            'rozdori': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=73),
            'slavgorod': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=74),
            'duboviki': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=75),
            'pokrovsyke': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=76),
            'velikomihaylivka': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=77),
            'malomihaylivka': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=78),
            'pershotravensk': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=79),
            'mikolaivka': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=80),
            'boginivka': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=81),
            'petropavlivka': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=82),
            'ukrainske': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=83),
            'slovyanka': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=84),
            'mezhova': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=85),
            'novopavlivka': Journal.objects.filter(
                date_of_receipt_message__range=[
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
                    f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
                city_id=86),

        }
        return render(request, 'home/index.html', context)
    else:
        messages.warning(request, 'Схоже ви намагаєтеся зайти Не Авторизувавшись')
        return redirect('login')


def return_queryset(request):
    datetime_range = [f"{format_datetime(datetime.today(), 'Y-MM-dd')} 00:00",
                      f"{format_datetime(datetime.today(), 'Y-MM-dd')} 23:59"]
    if request.is_ajax:
        value = request.GET.get('value')

        departures = Journal.objects.filter(region=value, date_of_receipt_message__range=datetime_range,
                                            category_id=25).count() + \
                     Journal.objects.filter(region=value, date_of_receipt_message__range=datetime_range,
                                            category_id=26).count() + \
                     Journal.objects.filter(region=value, date_of_receipt_message__range=datetime_range,
                                            category_id=28).count()

        events = Journal.objects.filter(region=value, date_of_receipt_message__range=datetime_range,
                                        category_id=25).count() + \
                 Journal.objects.filter(region=value, date_of_receipt_message__range=datetime_range,
                                        category_id=27).count()

        ns = Journal.objects.filter(region=value, date_of_receipt_message__range=datetime_range,
                                    category_id=28).count() + \
             Journal.objects.filter(region=value, date_of_receipt_message__range=datetime_range,
                                    category_id=29).count()

        people_rescued = Journal.objects.filter(
            region=value, date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        children_rescued = Journal.objects.filter(
            region=value, date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        people_injured = Journal.objects.filter(
            region=value, date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        children_injured = Journal.objects.filter(
            region=value, date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        people_died = Journal.objects.filter(
            region=value, date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        children_died = Journal.objects.filter(
            region=value, date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        quantity_peoples = Journal.objects.filter(
            region=value, date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_peoples'), 0))

        quantity_technics = Journal.objects.filter(
            region=value, date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_technics'), 0))

        fire = Journal.objects.filter(
            region=value, date_of_receipt_message__range=datetime_range,
            type_of_fire_id=8).count()

        dopomoga = Journal.objects.filter(
            region=value, date_of_receipt_message__range=datetime_range,
            type_of_fire_id=12).count()

        vnp = Journal.objects.filter(
            region=value, date_of_receipt_message__range=datetime_range,
            type_of_fire_id=13).count()

        hibniy_viklik = Journal.objects.filter(
            region=value, date_of_receipt_message__range=datetime_range,
            type_of_fire_id=9).count()

        zaminuvanya = Journal.objects.filter(
            region=value, date_of_receipt_message__range=datetime_range,
            type_of_fire_id=15).count()

        inshi = Journal.objects.filter(
            region=value, date_of_receipt_message__range=datetime_range,
            type_of_fire_id=11).count()

        return JsonResponse({'departures': departures,
                             'events': events,
                             'ns': ns,
                             'people_rescued': people_rescued,
                             'children_rescued': children_rescued,
                             'people_injured': people_injured,
                             'children_injured': children_injured,
                             'quantity_technics': quantity_technics,
                             'quantity_peoples': quantity_peoples,
                             'people_died': people_died,
                             'children_died': children_died,
                             'fire': fire,
                             'dopomoga': dopomoga,
                             'vnp': vnp,
                             'hibniy_viklik': hibniy_viklik,
                             'zaminuvanya': zaminuvanya,
                             'inshi': inshi, })
    return JsonResponse({'message': 'Invalid ajax'})


def render_of_city(request):
    datetime_range = [f"{format_datetime(datetime.today(), 'Y-MM-dd')} 00:00",
                      f"{format_datetime(datetime.today(), 'Y-MM-dd')} 23:59"]
    if request.is_ajax:

        querysets = Journal.objects.filter(date_of_receipt_message__range=datetime_range)

        departures_obl = Journal.objects.filter(date_of_receipt_message__range=datetime_range,
                                                category_id=25).count() + \
                         Journal.objects.filter(date_of_receipt_message__range=datetime_range,
                                                category_id=26).count() + \
                         Journal.objects.filter(date_of_receipt_message__range=datetime_range,
                                                category_id=28).count()

        events_obl = Journal.objects.filter(date_of_receipt_message__range=datetime_range,
                                            category_id=25).count() + \
                     Journal.objects.filter(date_of_receipt_message__range=datetime_range,
                                            category_id=27).count()

        ns_obl = Journal.objects.filter(date_of_receipt_message__range=datetime_range,
                                        category_id=28).count() + \
                 Journal.objects.filter(date_of_receipt_message__range=datetime_range,
                                        category_id=29).count()

        people_rescued_obl = Journal.objects.filter(
            date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_rescued'), 0))

        children_rescued_obl = Journal.objects.filter(
            date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_rescued_kids'), 0))

        people_injured_obl = Journal.objects.filter(
            date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_victims'), 0))

        children_injured_obl = Journal.objects.filter(
            date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_victims_kids'), 0))

        people_died = Journal.objects.filter(
            date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_dead'), 0))

        children_died_obl = Journal.objects.filter(
            date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_dead_kids'), 0))

        quantity_peoples_obl = Journal.objects.filter(
            date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_peoples'), 0))

        quantity_technics_obl = Journal.objects.filter(
            date_of_receipt_message__range=datetime_range).aggregate(
            sum=Coalesce(Sum('quantity_technics'), 0))

        fire_obl = Journal.objects.filter(
            date_of_receipt_message__range=datetime_range,
            type_of_fire_id=8).count()

        dopomoga_obl = Journal.objects.filter(
            date_of_receipt_message__range=datetime_range,
            type_of_fire_id=12).count()

        vnp_obl = Journal.objects.filter(
            date_of_receipt_message__range=datetime_range,
            type_of_fire_id=13).count()

        hibniy_viklik_obl = Journal.objects.filter(
            date_of_receipt_message__range=datetime_range,
            type_of_fire_id=9).count()

        zaminuvanya_obl = Journal.objects.filter(
            date_of_receipt_message__range=datetime_range,
            type_of_fire_id=15).count()

        inshi_obl = Journal.objects.filter(
            date_of_receipt_message__range=datetime_range,
            type_of_fire_id=11).count()

        day = datetime.now().day
        days = f'{day}'
        try:
            queryset = querysets.values().latest('date_of_receipt_message')
            return JsonResponse({'city': queryset['city_id'],
                                 'index': queryset['id'],
                                 'day': days,
                                 'departures_obl': departures_obl,
                                 'events_obl': events_obl,
                                 'ns_obl': ns_obl,
                                 'people_rescued_obl': people_rescued_obl,
                                 'children_rescued_obl': children_rescued_obl,
                                 'people_injured_obl': people_injured_obl,
                                 'children_injured_obl': children_injured_obl,
                                 'quantity_technics_obl': quantity_technics_obl,
                                 'quantity_peoples_obl': quantity_peoples_obl,
                                 'people_died_obl': people_died,
                                 'children_died_obl': children_died_obl,
                                 'fire_obl': fire_obl,
                                 'dopomoga_obl': dopomoga_obl,
                                 'vnp_obl': vnp_obl,
                                 'hibniy_viklik_obl': hibniy_viklik_obl,
                                 'zaminuvanya_obl': zaminuvanya_obl,
                                 'inshi_obl': inshi_obl,
                                 })
        except Journal.DoesNotExist:
            return redirect('home')
    return JsonResponse({'messages': 'Invalid ajax render of city'})


def queryset_city(request):
    city = request.GET.get('city')
    information = request.GET.get('information')
    queryset = Journal.objects.filter(
        date_of_receipt_message__range=[
            f'{format_datetime(datetime.today(), "Y-MM-dd")} 00:00',
            f'{format_datetime(datetime.today(), "Y-MM-dd")} 23:59'],
        city_id=city)
    context = {
        'city': queryset,
        'information': information
    }
    return render(request, 'home/news.html', context)
