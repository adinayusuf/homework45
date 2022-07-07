# Generated by Django 4.0.5 on 2022-07-07 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_alter_to_do_list_date_of_completion_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='To_do_list',
            new_name='ToDoList',
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_completion', models.DateField(blank=True, null=True, verbose_name='Время выполнения')),
                ('update', models.DateField(auto_now=True, null=True, verbose_name='Время изменения')),
                ('author', models.CharField(blank=True, max_length=40, null=True, verbose_name='Аноним')),
                ('text', models.TextField(max_length=400, verbose_name='Коментарий')),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='webapp.todolist')),
            ],
            options={
                'verbose_name': 'Коментарий',
                'verbose_name_plural': 'Коментарии',
                'db_table': 'comments',
            },
        ),
    ]