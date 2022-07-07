from django.db import models

STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class BaseModel(models.Model):
    date_of_completion = models.DateField(blank=True, null=True, verbose_name='Время выполнения')
    update = models.DateField(blank=True, null=True, auto_now=True, verbose_name='Время изменения')

    class Meta:
        abstract = True


class ToDoList(BaseModel):
    description = models.CharField(max_length=100, null=True, blank=False, verbose_name="Описание")
    text = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Текст')
    status = models.CharField(max_length=40, choices=STATUS_CHOICES, null=False, blank=False,
                              default=STATUS_CHOICES[0][0], verbose_name='Статус')

    def __str__(self):
        return f"{self.id}. {self.description}: {self.status}"

    class Meta:
        db_table = 'to_do_lists'
        verbose_name = 'Описание'
        verbose_name_plural = 'Описания'


class Comment(BaseModel):
    author = models.CharField(max_length=40, null=True, blank=True, verbose_name='Аноним')
    text = models.TextField(max_length=400, verbose_name='Коментарий')
    list = models.ForeignKey('webapp.ToDoList', on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'{self.id}. {self.text}:{self.author}'

    class Meta:
        db_table = 'comments'
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'