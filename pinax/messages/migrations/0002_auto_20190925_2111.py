# Generated by Django 2.2.1 on 2019-09-25 21:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pinax_messages', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='userthread',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='thread',
            name='users',
            field=models.ManyToManyField(through='pinax_messages.UserThread', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='message',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='pinax_messages.Thread'),
        ),
    ]
