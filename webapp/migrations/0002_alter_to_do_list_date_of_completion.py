# Generated by Django 4.0.5 on 2022-06-23 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='to_do_list',
            name='date_of_completion',
            field=models.DateField(blank=True, null=True, verbose_name='Время выполнения'),
        ),
    ]