# Generated by Django 2.2.1 on 2019-06-05 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakeplease', '0004_auto_20190605_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='note',
        ),
        migrations.AddField(
            model_name='item',
            name='minimal_order',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]