# Generated by Django 3.2.15 on 2022-08-08 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_alter_auction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='bid',
            field=models.DecimalField(decimal_places=2, max_digits=19),
        ),
    ]