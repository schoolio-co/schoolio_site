# Generated by Django 2.2.1 on 2019-09-24 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schoolio', '0008_remove_lesson_school_info_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activities',
            name='school_lesson_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schoolio.lesson_school_info'),
        ),
    ]
