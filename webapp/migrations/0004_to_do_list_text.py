# Generated by Django 4.0.5 on 2022-06-27 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_alter_to_do_list_date_of_completion'),
    ]

    operations = [
        migrations.AddField(
            model_name='to_do_list',
            name='text',
            field=models.TextField(blank=True, max_length=3000, null=True, verbose_name='Текст'),
        ),
    ]