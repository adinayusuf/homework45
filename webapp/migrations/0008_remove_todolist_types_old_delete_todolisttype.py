# Generated by Django 4.0.5 on 2022-07-12 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20220712_1206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='types_old',
        ),
        migrations.DeleteModel(
            name='ToDoListType',
        ),
    ]