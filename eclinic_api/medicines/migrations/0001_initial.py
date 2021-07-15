# Generated by Django 2.2.6 on 2019-10-04 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('medicine_number', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('unit', models.CharField(blank=True, max_length=100, null=True)),
                ('medicine_type', models.CharField(blank=True, max_length=100, null=True)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('price', models.PositiveIntegerField(default=0)),
                ('is_draft', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('recipe_number', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('recipe_date', models.DateField(blank=True, null=True)),
                ('diagnosis', models.TextField(blank=True, null=True)),
                ('action', models.TextField(blank=True, null=True)),
                ('is_draft', models.BooleanField(default=True)),
                ('register', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.Register')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RecipeItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('price', models.PositiveIntegerField(default=0)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('is_draft', models.BooleanField(default=True)),
                ('medicine', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medicines.Medicine')),
                ('recipe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medicines.Recipe')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
