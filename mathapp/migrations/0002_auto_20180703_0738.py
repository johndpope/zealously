# Generated by Django 2.0.6 on 2018-07-03 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mathapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ('created_date',)},
        ),
        migrations.AlterField(
            model_name='question',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date created'),
        ),
    ]