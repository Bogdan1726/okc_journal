from django.db import models


# Create your models here.

class Journal(models.Model):
    objects = None
    DoesNotExist = None
    quantity_departure = models.IntegerField(verbose_name='Порядковий номер виїзду на добу', null=True, default=0)
    date_of_receipt_message = models.DateTimeField(verbose_name='Дата|Час', null=True)
    region = models.ForeignKey('Region', on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey('City', on_delete=models.SET_NULL, null=True)
    town = models.ForeignKey('Town', on_delete=models.SET_NULL, null=True)
    information = models.CharField(max_length=2000, verbose_name='Інформація про подію')
    subdivisions = models.CharField(max_length=2000, verbose_name='Підрозділ')
    quantity_peoples = models.IntegerField(verbose_name='Кількість о.с', null=True, default=0)
    quantity_technics = models.IntegerField(verbose_name='Кількість од.тex.', null=True, default=0)
    quantity_rescued = models.IntegerField(verbose_name='Кількість врятованих', null=True, default=0)
    quantity_victims = models.IntegerField(verbose_name='Кількість постраждалих', null=True, default=0)
    quantity_dead = models.IntegerField(verbose_name='Кількість загиблих', null=True, default=0)
    quantity_rescued_kids = models.IntegerField(verbose_name='Дітей', null=True, default=0)
    quantity_victims_kids = models.IntegerField(verbose_name='Дітей', null=True, default=0)
    quantity_dead_kids = models.IntegerField(verbose_name='Дітей', null=True, default=0)

    quantity_ammunition = models.IntegerField(verbose_name='', null=True, default=0)
    violated_conditions = models.IntegerField(verbose_name='', null=True, default=0)
    quantity_objects = models.IntegerField(verbose_name='', null=True, default=0)

    departure_date = models.TimeField(verbose_name='час виїзду', null=True, default='00:00')
    time_of_arrival_to_the_place = models.TimeField(verbose_name='час прибуття до місця', null=True, default='00:00')
    barrel_feed_time = models.TimeField(verbose_name='час подачі першого ствола на гасіння', null=True, default='00:00')
    area = models.FloatField(verbose_name='площа пожежі(м2)', null=True, default=0)
    localization_time = models.TimeField(verbose_name='час локалізації', null=True, default='00:00')
    area2 = models.FloatField(verbose_name='площа пожежі(м2)', null=True, default=0)
    liquidation = models.BooleanField(default=False, verbose_name='Ліквідовано')
    liquidation_time = models.TimeField(verbose_name='час ліквідації', null=True, default='00:00')
    time_return_to_location = models.TimeField(verbose_name='час повернення до місця розташування', null=True,
                                               default='00:00')
    add_user = models.CharField(max_length=20, verbose_name='Хто додав', default=0)
    edit_user = models.CharField(max_length=20, verbose_name='Хто відредагував', default='Не редагувалось')

    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True,
                                 verbose_name='Категорія', blank=True)

    type_of_fire = models.ForeignKey('FireType', on_delete=models.SET_NULL, null=True,
                                     verbose_name='Тип')

    subtype = models.ForeignKey('Subtype', on_delete=models.SET_NULL, null=True,
                                verbose_name='Підтип', blank=True)

    def __str__(self):
        return f'{self.date_of_receipt_message} - {self.type_of_fire}'

    class Meta:
        verbose_name = 'Журналу виїзду'
        verbose_name_plural = 'Журнал виїзду'
        ordering = ['id']


class FireType(models.Model):
    objects = None
    title = models.CharField(max_length=150, db_index=True, verbose_name='Тип події')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип події'
        verbose_name_plural = 'Тип події'
        ordering = ['id']


class Subtype(models.Model):
    objects = None
    type = models.ForeignKey('FireType', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Підтип події'
        verbose_name_plural = 'Підтип події'
        ordering = ['id']


class Region(models.Model):
    objects = None
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Ройон'
        ordering = ['id']


class City(models.Model):
    objects = None
    region = models.ForeignKey('Region', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тергромада'
        verbose_name_plural = 'Тергромада'
        ordering = ['id']


class Town(models.Model):
    objects = None
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Населений пункт'
        verbose_name_plural = 'Населені пункти'
        ordering = ['id']


class Category(models.Model):
    objects = None
    title = models.CharField(max_length=150, db_index=True, verbose_name='Категорія події')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категорія події'
        verbose_name_plural = 'Категорія події'
        ordering = ['id']


class NoFire(models.Model):
    objects = None
    quantity_departure = models.IntegerField(verbose_name='Порядковий номер виїзду на добу', null=True, default=0)
    date_of_receipt_message = models.DateTimeField(verbose_name='Дата|Час', null=True)
    information = models.CharField(max_length=1000, verbose_name='Інформація про подію')
    subdivisions = models.CharField(max_length=1000, verbose_name='Підрозділ')
    departure_date = models.TimeField(verbose_name='час виїзду', null=True)
    time_of_arrival_to_the_place = models.TimeField(verbose_name='час прибуття до місця', null=True, default='00:00')
    time_return_to_location = models.TimeField(verbose_name='час повернення до місця розташування', null=True,
                                               default='00:00')
    add_user = models.CharField(max_length=20, verbose_name='Хто додав', default=0)
    edit_user = models.CharField(max_length=20, verbose_name='Хто відредагував', default='Не редагувалось')

    def __str__(self):
        return f'{self.date_of_receipt_message} - {self.subdivisions}'

    class Meta:
        verbose_name = "Не пов'язані з пожежею"
        verbose_name_plural = "Не пов'язані з пожежею"
        ordering = ['id']
