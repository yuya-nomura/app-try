# Generated by Django 4.2.7 on 2024-04-18 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kosu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrator_data',
            name='menu_row',
            field=models.CharField(max_length=4, verbose_name='一覧表示項目数'),
        ),
    ]