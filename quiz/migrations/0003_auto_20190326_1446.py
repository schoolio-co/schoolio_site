# Generated by Django 2.1.7 on 2019-03-26 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20190318_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='content',
            field=models.TextField(help_text='Enter the question text that you want displayed', max_length=2500, verbose_name='Question'),
        ),
    ]
