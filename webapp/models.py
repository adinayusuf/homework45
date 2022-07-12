from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Время изменения')

    class Meta:
        abstract = True


class Status(models.Model):
    status = models.CharField(max_length=40, null=False, blank=False, verbose_name='Статус')

    def __str__(self):
        return f"{self.id}.{self.status}"

    class Meta:
        db_table = 'status'
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Type(models.Model):
    type = models.CharField(max_length=40, verbose_name='Тип')

    def __str__(self):
        return f"{self.id}.{self.type}"

    class Meta:
        db_table = 'type'
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class ToDoList(BaseModel):
    summary = models.CharField(max_length=100, null=True, blank=False, verbose_name="Описание")
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Текст')
    status = models.ForeignKey('webapp.Status', on_delete=models.PROTECT, related_name='status_tasks')
    types = models.ManyToManyField('webapp.Type',
                                   related_name='type_tasks',
                                   through='webapp.ToDoListType',
                                   through_fields=('task', 'type'),
                                   blank=True)

    def __str__(self):
        return f"{self.id}. {self.summary}: {self.status}"

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Описание'
        verbose_name_plural = 'Описания'


class ToDoListType(models.Model):
    task = models.ForeignKey("webapp.ToDoList",
                             related_name='task_type',
                             on_delete=models.CASCADE,
                             verbose_name='Задача'
                             )
    type = models.ForeignKey('webapp.Type',
                             related_name='type_task',
                             on_delete=models.CASCADE,
                             verbose_name='Тип')
