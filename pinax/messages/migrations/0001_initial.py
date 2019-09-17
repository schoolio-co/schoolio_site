# Generated by Django 2.2.1 on 2019-09-17 05:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', models.TextField()),
            ],
            options={
                'ordering': ('sent_at',),
            },
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='UserThread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unread', models.BooleanField()),
                ('deleted', models.BooleanField()),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pinax_messages.Thread')),
            ],
        ),
    ]
