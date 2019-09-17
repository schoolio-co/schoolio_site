# Generated by Django 2.2.1 on 2019-09-17 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quiz', '0001_initial'),
        ('essay', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Essay_Question',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='quiz.Question')),
            ],
            options={
                'verbose_name': 'Essay style question',
                'verbose_name_plural': 'Essay style questions',
            },
            bases=('quiz.question',),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='essay.Essay_Question', verbose_name='Question'),
        ),
    ]
