# Generated by Django 4.0.3 on 2022-03-08 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('job_desc', models.TextField()),
                ('age', models.IntegerField()),
                ('img', models.ImageField(upload_to='')),
                ('salary', models.FloatField()),
                ('date_created', models.DateTimeField()),
            ],
        ),
    ]
