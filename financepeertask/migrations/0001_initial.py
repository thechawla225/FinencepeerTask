# Generated by Django 3.2.7 on 2021-09-21 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField()),
                ('id1', models.IntegerField()),
                ('title', models.CharField(max_length=1000)),
                ('body', models.CharField(max_length=1000)),
            ],
        ),
    ]
