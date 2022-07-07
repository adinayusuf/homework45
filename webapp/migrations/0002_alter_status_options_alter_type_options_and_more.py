# Generated by Django 4.0.5 on 2022-07-07 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Статус', 'verbose_name_plural': 'Статусы'},
        ),
        migrations.AlterModelOptions(
            name='type',
            options={'verbose_name': 'Тип', 'verbose_name_plural': 'Типы'},
        ),
        migrations.AlterField(
            model_name='todolist',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='status_tasks', to='webapp.status'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='type_tasks', to='webapp.type'),
        ),
        migrations.AlterModelTable(
            name='status',
            table='status',
        ),
        migrations.AlterModelTable(
            name='todolist',
            table='tasks',
        ),
        migrations.AlterModelTable(
            name='type',
            table='type',
        ),
    ]
