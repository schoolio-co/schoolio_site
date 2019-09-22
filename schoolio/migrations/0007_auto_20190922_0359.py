# Generated by Django 2.2.1 on 2019-09-22 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolio', '0006_remove_classroom_class_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacherschedule',
            name='friday',
        ),
        migrations.RemoveField(
            model_name='teacherschedule',
            name='monday',
        ),
        migrations.RemoveField(
            model_name='teacherschedule',
            name='thursday',
        ),
        migrations.RemoveField(
            model_name='teacherschedule',
            name='tuesday',
        ),
        migrations.RemoveField(
            model_name='teacherschedule',
            name='wednesday',
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='friday_eigth',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='friday_fifth',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='friday_first',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='friday_fourth',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='friday_second',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='friday_seventh',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='friday_sixth',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='friday_third',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='monday_eigth',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='monday_fifth',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='monday_first',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='monday_fourth',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='monday_second',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='monday_seventh',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='monday_sixth',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='monday_third',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='thursday_eigth',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='thursday_fifth',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='thursday_first',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='thursday_fourth',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='thursday_second',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='thursday_seventh',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='thursday_sixth',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='thursday_third',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='tuesday_eigth',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='tuesday_fifth',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='tuesday_first',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='tuesday_fourth',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='tuesday_second',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='tuesday_seventh',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='tuesday_sixth',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='tuesday_third',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='wednesday_eigth',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='wednesday_fifth',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='wednesday_first',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='wednesday_fourth',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='wednesday_second',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='wednesday_seventh',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='wednesday_sixth',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='wednesday_third',
            field=models.BooleanField(default=False),
        ),
    ]
