from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class Statistic(models.Model):
    objects = None
    date = models.DateTimeField(verbose_name='Дата')
    number_of_calls = models.IntegerField(default=0, verbose_name='Кількість дзвінків')
    add_user = models.CharField(max_length=100, verbose_name='Додав', null=True)
    subdivisions = models.ForeignKey('Subdivisions', on_delete=models.PROTECT, null=True,
                                     verbose_name='Підрозділ')

    def __str__(self):
        return f'{self.subdivisions} - {self.number_of_calls}'

    class Meta:
        verbose_name = 'Статистику'
        verbose_name_plural = 'Статистика'
        ordering = ['-date']


class Subdivisions(models.Model):

    title = models.CharField(max_length=150, db_index=True, verbose_name='Підрозділ')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Підрозділ'
        verbose_name_plural = 'Підрозділи'
        ordering = ['id']
