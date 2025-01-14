from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import inlineformset_factory
from django.forms import ModelChoiceField
from django.db import transaction
import datetime
from .models import school, school_user, student_assessment, TeacherSchedule, User, grade_level, create_updates, classroom, student_profiles, lesson_school_info, assessments, activities, standards, day_of_the_week, subjects, classroom_subject_summary  

      
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

class SchoolProfileForm(forms.ModelForm):
    GRADE_CHOICES=[
        ('Kinders2', 'Kinders2'),
        ('Kinders3', 'Kinders3'),
        ('Kinders4', 'Kinders4'),
        ('Kinders5', 'Kinders5'),
        ('Zero', 'Zero'),
        ('One', 'One'),
        ('Two', 'Two'),
        ('Three', 'Three'),
        ('Four', 'Four'),
        ('Five', 'Five'),
        ('Six', 'Six'),
        ('Seven', 'Seven'),
        ('Eight', 'Eight'),
        ('Nine', 'Nine'),
        ('Ten', 'Ten'),
        ('Eleven', 'Eleven'),
        ('Twelve', 'Twelve'),
    ]
    grade_level = forms.ChoiceField(choices=GRADE_CHOICES)
    
    class Meta:
        model = student_profiles
        fields = '__all__'

class ClassroomForm(forms.Form):
    GRADE_CHOICES=[
        ('Kinders2', 'Kinders2'),
        ('Kinders3', 'Kinders3'),
        ('Kinders4', 'Kinders4'),
        ('Kinders5', 'Kinders5'),
        ('Zero', 'Zero'),
        ('One', 'One'),
        ('Two', 'Two'),
        ('Three', 'Three'),
        ('Four', 'Four'),
        ('Five', 'Five'),
        ('Six', 'Six'),
        ('Seven', 'Seven'),
        ('Eight', 'Eight'),
        ('Nine', 'Nine'),
        ('Ten', 'Ten'),
        ('Eleven', 'Eleven'),
        ('Twelve', 'Twelve'),
    ]
    classroom_name = forms.CharField(max_length=30, required=False)
    grade_level = forms.ChoiceField(choices=GRADE_CHOICES)
    school = forms.CharField(max_length=30, required=False)

    class Meta:
        fields = '__all__'

class AddStudentClassroomForm(forms.ModelForm):
    student = forms.ModelMultipleChoiceField(queryset = student_profiles.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)
    
    
    class Meta:
        model = classroom
        fields = '__all__'
        readonly_fields = ('Classroom',)

class SchoolLessonForm(forms.ModelForm):


    class Meta:
        model = lesson_school_info
        fields = '__all__'


class WeeklyCreateForm(forms.Form):
    school_lesson_id = forms.CharField(max_length=30, required=False)
    activity_title = forms.CharField(max_length=200, required=False)
    subject =  forms.CharField(max_length=50, required=False)
    week_of =  forms.CharField(max_length=30, required=False)
    standard =  forms.CharField(max_length=500, required=False)
    day = forms.CharField(max_length=30, required=False)
    mondayintro = forms.CharField(max_length=500, required=False)
    mondayactivity = forms.CharField(max_length=1000, required=False)
    mondaywrap_up = forms.CharField(max_length=500, required=False)
    mondayresources = forms.CharField(max_length=500, required=False)
    mondayblooms = forms.CharField(max_length=500, required=False)
    mondayvocabulary = forms.CharField(max_length=30, required=False)
    mondayday = forms.CharField(max_length=30, required=False)
    mondayperiod = forms.CharField(max_length=30, required=False)
    tuesdayintro = forms.CharField(max_length=500, required=False)
    tuesdayactivity = forms.CharField(max_length=1000, required=False)
    tuesdaywrap_up = forms.CharField(max_length=500, required=False)
    tuesdayresources = forms.CharField(max_length=500, required=False)
    tuesdayblooms = forms.CharField(max_length=500, required=False)
    tuesdayvocabulary = forms.CharField(max_length=30, required=False)
    tuesdayperiod = forms.CharField(max_length=30, required=False)
    tuesdayday = forms.CharField(max_length=30, required=False)
    wednesdayintro = forms.CharField(max_length=500, required=False)
    wednesdayactivity = forms.CharField(max_length=1000, required=False)
    wednesdaywrap_up = forms.CharField(max_length=500, required=False)
    wednesdayresources = forms.CharField(max_length=500, required=False)
    wednesdayblooms = forms.CharField(max_length=500, required=False)
    wednesdayvocabulary = forms.CharField(max_length=30, required=False)
    wednesdayperiod = forms.CharField(max_length=30, required=False)
    wednesdayday = forms.CharField(max_length=30, required=False)
    thursdayintro = forms.CharField(max_length=500, required=False)
    thursdayactivity = forms.CharField(max_length=1000, required=False)
    thursdaywrap_up = forms.CharField(max_length=500, required=False)
    thursdayresources = forms.CharField(max_length=500, required=False)
    thursdayblooms = forms.CharField(max_length=500, required=False)
    thursdayvocabulary = forms.CharField(max_length=30, required=False)
    thursdayperiod = forms.CharField(max_length=30, required=False)
    thursdayday = forms.CharField(max_length=30, required=False)
    fridayintro = forms.CharField(max_length=500, required=False)
    fridayactivity = forms.CharField(max_length=1000, required=False)
    fridaywrap_up = forms.CharField(max_length=500, required=False)
    fridayresources = forms.CharField(max_length=500, required=False)
    fridayblooms = forms.CharField(max_length=500, required=False)
    fridayvocabulary = forms.CharField(max_length=30, required=False)
    fridayperiod = forms.CharField(max_length=30, required=False)
    fridayday = forms.CharField(max_length=30, required=False)


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


class CreateUpdateForm(forms.ModelForm):

    class Meta:
            model = create_updates
            fields = '__all__'

class TeacherScheduleForm(forms.ModelForm):


    class Meta:
            model = TeacherSchedule
            fields = '__all__'


class StudentAssessmentForm(forms.ModelForm):
    assessment_score = forms.CharField(required=False, widget=forms.HiddenInput())
    understanding_level = forms.CharField(required=False, widget=forms.HiddenInput())
    
    class Meta:
            model = student_assessment
            fields = '__all__'

