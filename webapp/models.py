from django.db import models

# Create your models here.
STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class To_do_list(models.Model):
    description = models.CharField(max_length=100, null=False, blank=False, verbose_name="Описание")
    status = models.CharField(max_length=40, choices=STATUS_CHOICES, null=False, blank=False,
                              default=STATUS_CHOICES[0][0], verbose_name='Статус')
    date_of_completion = models.DateField(blank=True, null=True, verbose_name='Время выполнения')

    def __str__(self):
        return f"{self.id}. {self.description}: {self.status}"

    class Meta:
        db_table = 'to_do_lists'
        verbose_name = 'Описание'
        verbose_name_plural = 'Описания'
