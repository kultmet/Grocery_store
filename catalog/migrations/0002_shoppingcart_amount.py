# Generated by Django 4.2 on 2023-04-13 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcart',
            name='amount',
            field=models.PositiveIntegerField(default=1, verbose_name='amount'),
        ),
    ]
