# Generated by Django 2.2.1 on 2019-09-13 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schoolio', '0005_auto_20190912_1956'),
    ]

    operations = [
        migrations.CreateModel(
            name='create_update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_title', models.TextField(max_length=150)),
                ('update', models.TextField(max_length=1000)),
                ('school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schoolio.school')),
            ],
        ),
    ]
