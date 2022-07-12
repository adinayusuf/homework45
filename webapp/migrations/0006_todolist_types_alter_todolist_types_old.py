# Generated by Django 4.0.5 on 2022-07-12 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_rename_types_todolist_types_old'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='types',
            field=models.ManyToManyField(blank=True, related_name='type_tasks', to='webapp.type'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='types_old',
            field=models.ManyToManyField(blank=True, related_name='old_type_tasks', through='webapp.ToDoListType', to='webapp.type'),
        ),
    ]
