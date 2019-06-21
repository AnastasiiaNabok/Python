# Generated by Django 2.2.1 on 2019-06-04 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.URLField()),
                ('price', models.PositiveSmallIntegerField()),
                ('description', models.CharField(max_length=200)),
                ('countable', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('role', models.CharField(max_length=5)),
                ('phone_number', models.PositiveSmallIntegerField()),
                ('address', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cakeplease.Item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cakeplease.User')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='delivery date')),
                ('delivery', models.BooleanField(default=False)),
                ('count', models.PositiveSmallIntegerField()),
                ('status', models.BooleanField(default=False)),
                ('payment_method', models.CharField(max_length=5)),
                ('item', models.ManyToManyField(to='cakeplease.Item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cakeplease.User')),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cakeplease.User')),
            ],
        ),
    ]
