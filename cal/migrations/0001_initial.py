# Generated by Django 2.2.1 on 2019-09-09 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('category', models.CharField(default='main', max_length=30)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
    ]
