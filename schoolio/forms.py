from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import inlineformset_factory
from django.forms import ModelChoiceField
from django.forms import formset_factory
from django.db import transaction
import datetime
from .models import school, school_user, User, grade_level, classroom, student_profiles, lesson_school_info, assessments, activities, standards, day_of_the_week, subjects, classroom_subject_summary  

      
class SchoolForm(forms.ModelForm):
    name = forms.CharField(label='School Name', max_length=30)
    address = forms.CharField(max_length=250)
    url = forms.SlugField(max_length=50)

    class Meta:
        model = school
        fields = ['name', 'address', 'url',]

class AdministratorForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    school = forms.ModelChoiceField(queryset = school.objects.all())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'school')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin = True
        user.save()
        administrator = school_user.objects.create(user=user)
        return user

class TeacherForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    school = forms.ModelChoiceField(queryset = school.objects.all())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'school')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        teacher = school_user.objects.create(user=user)
        return user


class ParentForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    school = forms.ModelChoiceField(queryset = school.objects.all())
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'school')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_parent = True
        user.save()
        parent = school_user.objects.create(user=user)
        return user


class StudentForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    school = forms.ModelChoiceField(queryset = school.objects.all())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'school')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = school_user.objects.create(user=user)
        return user



class GradeForm(forms.ModelForm):

    class Meta:
        model = grade_level
        fields = '__all__'

class ClassroomForm(forms.ModelForm):

    class Meta:
        model = classroom
        fields = '__all__'

class SchoolLessonForm(forms.ModelForm):
    DAY_CHOICES=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
    ]
    days = forms.MultipleChoiceField(choices=DAY_CHOICES, widget = forms.CheckboxSelectMultiple)


    class Meta:
        model = lesson_school_info
        fields = '__all__'


class AssessmentForm(forms.ModelForm):

    class Meta:
        model = assessments
        fields = '__all__'

def unique_values():
    return ReadOnlyTable.objects.values_list('subject').distinct()

class ActivityForm(forms.ModelForm):

    class Meta:
            model = activities
            fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ActivityForm, self).__init__(*args, **kwargs)
        self.fields['standard'].widget.attrs['class'] = 'form-control'


class ClassroomSubjectSummaryForm(forms.ModelForm):

    class Meta:
            model = classroom_subject_summary
            fields = '__all__'

