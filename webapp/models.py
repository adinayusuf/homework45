from django.db import models
from django.urls import reverse

from webapp.validate import MinLengthValidator


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Время изменения')

    class Meta:
        abstract = True


class Status(models.Model):
    status = models.CharField(max_length=40, verbose_name='Статус')

    def __str__(self):
        return f"{self.status}"

    class Meta:
        db_table = 'status'
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Type(models.Model):
    type = models.CharField(max_length=40, verbose_name='Тип')

    def __str__(self):
        return f"{self.type}"

    class Meta:
        db_table = 'type'
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class ToDoList(BaseModel):
    summary = models.CharField(max_length=15, null=True, blank=False, verbose_name="Описание",
                               validators=[MinLengthValidator(15)])
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Текст')
    status = models.ForeignKey('webapp.Status', on_delete=models.PROTECT, related_name='status_tasks')
    types = models.ManyToManyField('webapp.Type', related_name='type_tasks', blank=True)
    project = models.ForeignKey('webapp.Project', related_name='project_tasks', on_delete=models.CASCADE,
                                verbose_name='Проект')

    def __str__(self):
        return f"{self.id}. {self.summary}: {self.status}"

    def get_absolute_url(self):
        return reverse('detail_view', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Описание'
        verbose_name_plural = 'Описания'


class Project(models.Model):
    data_begin = models.DateField(max_length=20, verbose_name='Дата начала')
    data_end = models.DateField(max_length=20, null=True, blank=True, verbose_name='Дата Окончания')
    title = models.CharField(max_length=20, verbose_name="Название")
    description = models.TextField(max_length=2000, verbose_name="Описание")

    def __str__(self):
        return f"{self.id}. {self.title}: {self.description}"

    def get_absolute_url(self):
        return reverse('project_detailview.html', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'projects'
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
