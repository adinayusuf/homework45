from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# PROJECT_MANAGER = "project_manager"
# TEAM_LEAD = "team_lead"
# DEVELOPER = "developer"
# ROLE_CHOIСES = [
#     (PROJECT_MANAGER, "Project Manager"),
#     (TEAM_LEAD, "Team Lead"),
#     (DEVELOPER, "Developer")
# ]


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Updated at')

    class Meta:
        abstract = True


class Status(models.Model):
    status = models.CharField(max_length=40, verbose_name='Status')

    def __str__(self):
        return f"{self.status}"

    class Meta:
        db_table = 'status'
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Type(models.Model):
    type = models.CharField(max_length=40, verbose_name='Type')

    def __str__(self):
        return f"{self.type}"

    class Meta:
        db_table = 'type'
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class ToDoList(BaseModel):
    summary = models.CharField(max_length=15, null=True, blank=False, verbose_name="Name")
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Description')
    status = models.ForeignKey('webapp.Status', on_delete=models.PROTECT, related_name='status_tasks',
                               verbose_name='Status')
    types = models.ManyToManyField('webapp.Type', related_name='type_tasks', blank=True, verbose_name='Types')
    project = models.ForeignKey('webapp.Project', related_name='project_tasks', default=1, on_delete=models.CASCADE,
                                verbose_name='Project')

    def __str__(self):
        return f"{self.id}. {self.summary}: {self.status}"

    def get_absolute_url(self):
        return reverse('webapp:detail_view', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Описание'
        verbose_name_plural = 'Описания'


class Project(models.Model):
    data_begin = models.DateField(max_length=20, verbose_name='Date begin')
    data_end = models.DateField(max_length=20, null=True, blank=True, verbose_name='Date end')
    title = models.CharField(max_length=20, verbose_name="Name")
    description = models.TextField(max_length=2000, verbose_name="Description")
    is_deleted = models.BooleanField(default=False)
    members = models.ManyToManyField(User, related_name='projects',
                                     verbose_name='Projects')

    def __str__(self):
        return f"{self.id}. {self.title}: {self.description}"

    def get_absolute_url(self):
        return reverse('webapp:project_detail', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'projects'
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


# class ProjectUser(models.Model):
#     project = models.ForeignKey('ToDoList.Project', on_delete=models.CASCADE, related_name='projectusers',
#                                 verbose_name='Project')
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userprojects', verbose_name='User')
#     role = models.CharField(max_length=250, choices=ROLE_CHOIСES, default=PROJECT_MANAGER, verbose_name='Role')
#
#     class Meta:
#         db_table = 'projectuser'
#         unique_together = ('project', 'user')
#
#     def __str__(self):
#         return f"{self.user}. {self.project.summary} - {self.role}"
