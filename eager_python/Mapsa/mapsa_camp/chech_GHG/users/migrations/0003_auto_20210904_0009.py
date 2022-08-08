# Generated by Django 3.2.7 on 2021-09-04 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210903_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regular',
            name='code_meli',
            field=models.IntegerField(max_length=10, verbose_name='کدملی'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='staff_number',
            field=models.IntegerField(max_length=10, verbose_name='کد کارمندی'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='bank_shaba',
            field=models.IntegerField(max_length=24, verbose_name='شماره شبا کارت بانکی خود را وارد کنید'),
        ),
    ]