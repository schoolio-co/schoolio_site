# Generated by Django 2.2.1 on 2019-09-09 23:07

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_parent', models.BooleanField(default=False)),
                ('is_teacher', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='activities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_lesson_id', models.IntegerField()),
                ('activity_title', models.CharField(max_length=500)),
                ('subject', models.CharField(max_length=500)),
                ('week_of', models.CharField(max_length=5)),
                ('standard', models.CharField(max_length=500)),
                ('intro', models.CharField(max_length=500)),
                ('activity', models.TextField(max_length=1000)),
                ('wrap_up', models.CharField(max_length=500)),
                ('resources', models.CharField(max_length=100)),
                ('blooms', models.CharField(max_length=100)),
                ('vocabulary', models.CharField(max_length=100)),
                ('day', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='day_of_the_week',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='grade_level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='school',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.TextField(max_length=250)),
                ('url', models.SlugField(help_text='www.schoolio.co/....', max_length=60, verbose_name='www.schoolio.co/....')),
            ],
        ),
        migrations.CreateModel(
            name='standards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField(max_length=50)),
                ('standard', models.TextField(max_length=100)),
                ('skill_topic', models.TextField(max_length=100)),
                ('objective', models.TextField(max_length=150)),
                ('competency', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='student_profiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schoolio.classroom')),
                ('grade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schoolio.grade_level')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_info', to=settings.AUTH_USER_MODEL)),
                ('school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schoolio.school')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher_info', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_info', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='lesson_school_info',
            fields=[
                ('school_lesson_id', models.AutoField(primary_key=True, serialize=False)),
                ('teacher', models.CharField(max_length=30)),
                ('week_of', models.CharField(max_length=30)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('subject', models.CharField(max_length=100)),
                ('days', models.CharField(max_length=100)),
                ('objective', models.TextField(max_length=500)),
                ('classroom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schoolio.classroom')),
                ('grade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schoolio.grade_level')),
                ('school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schoolio.school')),
            ],
        ),
        migrations.AddField(
            model_name='grade_level',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schoolio.school'),
        ),
        migrations.CreateModel(
            name='classroom_subject_summary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField(max_length=50)),
                ('lu_level', models.IntegerField(max_length=10)),
                ('mu_level', models.IntegerField(max_length=10)),
                ('hu_level', models.IntegerField(max_length=10)),
                ('logical_level', models.IntegerField(max_length=10)),
                ('linguistic_level', models.IntegerField(max_length=10)),
                ('kinesthetic_level', models.IntegerField(max_length=10)),
                ('musical_level', models.IntegerField(max_length=10)),
                ('visual_level', models.IntegerField(max_length=10)),
                ('naturalist_level', models.IntegerField(max_length=10)),
                ('group_level', models.IntegerField(max_length=10)),
                ('independent_level', models.IntegerField(max_length=10)),
                ('classroom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schoolio.classroom')),
            ],
        ),
        migrations.CreateModel(
            name='classroom_averages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mi_one', models.TextField()),
                ('mi_two', models.TextField()),
                ('mi_three', models.TextField()),
                ('lu_low', models.TextField()),
                ('lu_med', models.TextField()),
                ('lu_high', models.TextField()),
                ('classroom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schoolio.classroom')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schoolio.subjects')),
            ],
        ),
        migrations.AddField(
            model_name='classroom',
            name='grade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schoolio.grade_level'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schoolio.school'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='assessments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assessment', models.TextField(max_length=500)),
                ('is_formal', models.BooleanField(default=False)),
                ('is_final', models.BooleanField(default=False)),
                ('is_informal', models.BooleanField(default=False)),
                ('assessment_mark', models.TextField(max_length=50)),
                ('activity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schoolio.school')),
                ('student', models.ManyToManyField(blank=True, null=True, related_name='student_assessment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schoolio.school'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.CreateModel(
            name='school_user',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user_role', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schoolio.school')),
            ],
        ),
    ]
