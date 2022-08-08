# Generated by Django 3.2.7 on 2021-10-04 06:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0008_auto_20211002_1004'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.TextField()),
                ('payment_id', models.TextField()),
                ('amount', models.IntegerField()),
                ('date', models.TextField(default='-')),
                ('card_number', models.TextField(default='****')),
                ('idpay_track_id', models.IntegerField(default=0)),
                ('bank_track_id', models.TextField(default=0)),
                ('status', models.IntegerField(default=0)),
                ('m2m', models.ManyToManyField(blank=True, to='cart.CartItem')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='invoce', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]