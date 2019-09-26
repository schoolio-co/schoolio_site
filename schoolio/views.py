from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.template import loader
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.utils.safestring import mark_safe
from django.template.defaultfilters import slugify
from django.template.defaultfilters import stringfilter
from django.utils.text import normalize_newlines
from django.views.generic import View, FormView, TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.db import transaction
from django.contrib import messages 
from datetime import date
from django import views
from django.db.models import Q
from django.shortcuts import get_list_or_404, get_object_or_404, render
from .forms import SchoolForm, TeacherScheduleForm, StudentAssessmentForm, AdministratorForm, AddStudentClassroomForm, TeacherForm, ParentForm, StudentForm, GradeForm, ClassroomForm, ActivityForm, AssessmentForm, SchoolLessonForm, ClassroomSubjectSummaryForm, WeeklyCreateForm, CreateUpdateForm
from  cal.forms import EventForm
from .models import school, school_user, Event, student_assessment, TeacherSchedule, User, grade_level, classroom, student_profiles, activities, assessments, lesson_school_info, standards, day_of_the_week, classroom_subject_summary, create_updates
from .standard_matching import match_standard, match_activity
from .evaluate import get_MI_BL
from .import_csv import import_csv 
from django.db.models.signals import post_save
from django.dispatch import receiver

class SchoolRegistration(TemplateView):
    template_name = 'home.html'

    def get(self,request, *args, **kwargs):
        return render(request, 'home.html')

class RoleRegistrations(TemplateView):
    template_name = 'roles_registration.html'

    def get(self,request,school_url):
        return render(request, 'roles_registration.html', {'school_url': school_url})


def Import_Data(request, *args, **kwargs):
    path = 'schoolio/standards/Grade One.csv'
    with open(path) as f:
        for line in f:
            line = line.split(',') 
            obj, created = standards.objects.get_or_create(subject=line[0], standard=line[1], skill_topic=line[2], objective=line[3], competency=line[4])
            obj.save()
    path2 = 'schoolio/standards/students_full.csv'
    school_name = school.objects.get(id=1)
    with open(path2) as f:
        for line in f:
            line = line.split(',') 
            obj2, created = student_profiles.objects.get_or_create(first_name=line[0], last_name=line[1], student_ref=line[3], grade_level=line[5], school=school_name)
            obj2.save()
    return render(request, 'import.html')


def login_user(request, school_url=None):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You are logged In!'))
            return redirect('school_profile', school_url=school_url)
        else:
            messages.success(request, ('Error Logging In - Please Try Again...'))
            return render(request, 'registration/login.html', {'school_url': school_url})
    else:
        return render(request, 'registration/login.html', {'school_url': school_url})

def logout_user(request, school_url=None):
    logout(request)
    return redirect('school_profile', school_url=school_url)

def School_Register(request):
    if request.method == "POST":
        form = SchoolForm(request.POST)
        if form.is_valid():
            prev = form.save(commit=False)
            school.url = prev.url
            prev.save()
        return render(request, 'school_register.html', {'school_url': school.url})
    else:
        form = SchoolForm()
    return render(request, 'school_register.html', {'form': form})

class School_Profile(TemplateView):
    model=school
    model=create_updates
    model=Event
    school_url = 'school_url'
    template_name = "school_profile.html"
    
    def get(self,request,school_url):
        obj = school.objects.get(url=school_url)
        obj2 = create_updates.objects.filter(school=obj.id)
        obj3 = Event.objects.filter(school=obj.id)
        school_url = obj.url
        return render(request, 'school_profile.html', {'obj': obj, 'obj2': obj2, 'obj3': obj3, 'school_url': school_url })


def Parent_Register(request, school_url=None, username=None):
    model = User
    obj = school.objects.get(url=school_url)
    school_url = obj.url
    school_pk = obj.id

    if request.method == "POST":
        form = ParentForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'register.html', {'username': username, 'school_url': school_url})

    else:
        data = {'is_parent': 'True', 
                'school': school_pk }
        form = ParentForm(initial=data)
    return render(request, 'register.html', {'form': form, 'school_url': school_url})

def Student_Register(request, school_url=None, username=None):
    model = User
    model = student_profiles
    obj = school.objects.get(url=school_url)
    school_url = obj.url
    school_pk = obj.id

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'register.html', {'username': username, 'school_url': school_url})

    else:
        data = {'school': school_pk }
        form = StudentForm(initial=data)
    return render(request, 'register.html', {'form': form, 'school_url': school_url})

def Admin_Register(request, school_url=None, username=None):
    model = User
    obj = school.objects.get(url=school_url)
    school_url = obj.url
    school_pk = obj.id

    if request.method == "POST":
        form = AdministratorForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'register.html', {'username': username, 'school_url': school_url})

    else:
        data = {'is_admin': 'True', 
                'school': school_pk }
        form = AdministratorForm(initial=data)
    return render(request, 'register.html', {'form': form, 'school_url': school_url})

def Teacher_Register(request, school_url=None, username=None):
    model = User
    obj = school.objects.get(url=school_url)
    school_url = obj.url
    school_pk = obj.id

    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'register.html', {'username': username, 'school_url': school_url })

    else:
        data = {'is_teacher': 'True', 
                'school': school_pk }
        form = TeacherForm(initial=data)
    return render(request, 'register.html', {'form': form, 'school_url': school_url})

class Student_Profiles(TemplateView):
    model=student_profiles
    school_url = 'school_url'
    template_name = "student_profiles.html"
    
    def get(self,request,school_url):
        obj = student_profiles.objects.fiter(school=school_url)
        return render(request, 'student_profiles.html', {'obj': obj, 'school_url': school_url})

def Student_Profile(request, school_url=None, student_id=None):
    obj = student_profiles.objects.get(id=student_id)
    obj2 = student_assessment.objects.filter(student=obj).order_by('assessment')
    return render(request, 'student_profile.html', {'obj': obj, 'obj2': obj2, 'school_url': school_url})

def UserList(request,school_url=None):
    obj = school.objects.get(url=school_url)
    school_pk = obj.id
    school_url = obj.url
    obj = User.objects.all()
    return render(request, 'all_users.html', {'object_list': obj, 'school_url': school_url})

class Profile(TemplateView):
    model=User
    school_url = 'school_url'
    username = 'username'
    template_name = "profile.html"
    
    def get(self,request,school_url,username):
        obj = User.objects.get(username=username)
        current_week = date.today().isocalendar()[1] 
        return render(request, 'profile.html', {'obj': obj, 'school_url': school_url, 'current_week': current_week})

def create_grade(request, school_url=None, slug=None):
    model = grade_level
    obj = school.objects.get(url=school_url)
    school_url = obj.url
    school_pk = obj.id

    if request.method == "POST":
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('school_profile', school_url=school_url)

    else:
        data = {'school': school_pk }
        form = GradeForm(initial=data)
    return render(request, 'create_classroom.html', {'form': form, 'school_url': school_url })

def create_classroom(request, school_url=None):
    obj = school.objects.get(url=school_url)
    school_url = obj.url
    school_pk = obj.id
    classrooms = classroom.objects.filter(school=school_pk)

    if request.method == "POST":
        form = ClassroomForm(request.POST)
        if form.is_valid():
            classroom_name = form.cleaned_data['classroom_name']
            grade_level = form.cleaned_data['grade_level']
            classroom_url = slugify(classroom_name)

            return redirect('add_students_new', school_url=school_url, classroom_url=classroom_url, grade_level=grade_level)

    else:
        data = {'school': school_url}
        form = ClassroomForm(initial=data)
    return render(request, 'create_classroom.html', {'form':form, 'school_url':school_url, 'classrooms': classrooms })

def SingleClassroom(request, school_url=None, classroom_id=None):
    classroom_id = classroom_id
    obj = classroom.objects.get(Classroom=classroom_id)
    classroom_pk = obj.id
    subject_summary = classroom_subject_summary.objects.filter(classroom=classroom_pk)

    return render(request, 'classroom.html', {'obj': obj, 'school_url': school_url, 'subject_summary':subject_summary })

def add_students_new_classroom(request, school_url=None, classroom_url=None, grade_level=None):
    model = classroom
    obj = school.objects.get(url=school_url)
    school_pk = obj.id

    if request.method == "POST":
        form = AddStudentClassroomForm(request.POST, grade_level)
        if form.is_valid():
            form.save()
            return redirect('school_profile', school_url=school_url)
    
    else:
        data = {'Classroom': classroom_url, 
                'grade_level': grade_level,
                'school': school_pk}
        form = AddStudentClassroomForm(initial=data)
        form.fields["student"].queryset = student_profiles.objects.filter(grade_level=grade_level)
    return render(request, 'create_classroom.html', {'form':form, 'school_url':school_url})


def add_students_classroom(request, school_url=None, classroom_id=None, grade_level=None):
    model = classroom
    obj = classroom.objects.get(id=classroom_id)
    school_id = obj.school_id
    if request.method == "POST":
        form = AddStudentClassroomForm(request.POST, grade_level, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('school_profile', school_url=school_url)
    
    else:
        
        form = AddStudentClassroomForm(instance=obj)
        form.fields["student"].queryset = student_profiles.objects.filter(grade_level=grade_level)
    return render(request, 'create_classroom.html', {'form':form, 'school_url':school_url})


def Create_School_Lesson(request, school_url=None, username=None, week_of=None):
    teacher = User.objects.get(username=username)
    teacher_pk = teacher.id
    current_week = date.today().isocalendar()[1] 
    obj = school.objects.get(url=school_url)
    school_pk = obj.id
    teacher_weekly = TeacherSchedule.objects.filter(teacher=teacher_pk, school=school_pk)

    if request.method == "POST":
        form = SchoolLessonForm(request.POST)
        if form.is_valid():
            prev = form.save(commit=False)
            week_of = prev.week_of
            subject_summary = classroom_subject_summary.objects.create(lesson_id = prev.school_lesson_id, classroom = prev.classroom, subject = prev.subject, lu_level = '.25', mu_level = '.50', hu_level = '.25', logical_level = '1', linguistic_level = '1', kinesthetic_level = '1', musical_level = '1', visual_level = '1', naturalist_level = '1', group_level = '1', independent_level = '1')
            subject_summary.save() 
            prev.save()
            return redirect('weeklyactivitycreate', planning_id=prev, school_url=school_url, username=teacher_pk, week_of=week_of)
        else:
            return render(request, 'lesson_school.html', {'form': form, 'school_url': school_url})
    else:
        form = SchoolLessonForm()
        if week_of:
            form.fields['week_of'].initial = week_of
        else:
            form.fields['week_of'].initial = current_week
        form.fields['planning_teacher'].initial = teacher_pk
        form.fields['school'].initial = school_pk
    return render(request, 'lesson_school.html', {'form': form, 'school_url': school_url, 'teacher_weekly': teacher_weekly})


def CreateWeeklyActivity(request, school_url=None, planning_id=None, week_of=None, username=None):
    obj = lesson_school_info.objects.get(school_lesson_id=planning_id)
    classroom_name = obj.classroom
    classroom_id = obj.classroom_id
    teacher_objective = obj.objective
    teacher_subject = obj.subject
    teacher = User.objects.get(id=username)
    teacher_pk = teacher.id 
    teacher_name = teacher.username
    obj2 = school.objects.get(url=school_url)
    school_pk = obj2.id
    classroom_match = classroom.objects.get(Classroom=classroom_name)
    teacher_schedule = TeacherSchedule.objects.filter(teacher=teacher_pk, school=school_pk, classroom=classroom_match, Subject=teacher_subject)
    subject_summary = classroom_subject_summary.objects.filter(classroom=classroom_match).first()
    results = match_standard(obj.objective, obj.subject)
    if results:
        matches = match_activity(classroom_match, teacher_objective, results[0][0], teacher_subject)
        matches = list(map(lambda x: x[0], matches))
    else:
        matches = []
    #for match in matches:
        #activity_match = activities.objects.filter(intro=match[0])


    if request.method == "POST":
        form = WeeklyCreateForm(request.POST)
        if form.is_valid():
            school_lesson_id = form.cleaned_data['school_lesson_id']
            activity_title = form.cleaned_data['activity_title']
            subject =  form.cleaned_data['subject']
            week_of =  form.cleaned_data['week_of']
            standard =  form.cleaned_data['standard']
            mondayintro = form.cleaned_data['mondayintro']
            mondayactivity = form.cleaned_data['mondayactivity']
            mondaywrap_up = form.cleaned_data['mondaywrap_up']
            mondayresources = form.cleaned_data['mondayresources']
            mondayblooms = get_MI_BL(mondayactivity)
            mondayvocabulary = form.cleaned_data['mondayvocabulary']
            mondayperiod = form.cleaned_data['mondayperiod']
            mondayday = form.cleaned_data['mondayday']
            tuesdayintro = form.cleaned_data['tuesdayintro']
            tuesdayactivity = form.cleaned_data['tuesdayactivity']
            tuesdaywrap_up = form.cleaned_data['tuesdaywrap_up']
            tuesdayresources = form.cleaned_data['tuesdayresources']
            tuesdayblooms = get_MI_BL(tuesdayactivity)
            tuesdayvocabulary = form.cleaned_data['tuesdayvocabulary']
            tuesdayperiod = form.cleaned_data['tuesdayperiod']
            tuesdayday = form.cleaned_data['tuesdayday']
            wednesdayintro = form.cleaned_data['wednesdayintro']
            wednesdayactivity = form.cleaned_data['wednesdayactivity']
            wednesdaywrap_up = form.cleaned_data['wednesdaywrap_up']
            wednesdayresources = form.cleaned_data['wednesdayresources']
            wednesdayblooms = get_MI_BL(wednesdayactivity)
            wednesdayvocabulary = form.cleaned_data['wednesdayvocabulary']
            wednesdayperiod = form.cleaned_data['wednesdayperiod']
            wednesdayday = form.cleaned_data['wednesdayday']
            thursdayintro = form.cleaned_data['thursdayintro']
            thursdayactivity = form.cleaned_data['thursdayactivity']
            thursdaywrap_up = form.cleaned_data['thursdaywrap_up']
            thursdayresources = form.cleaned_data['thursdayresources']
            thursdayblooms = get_MI_BL(thursdayactivity)
            thursdayvocabulary = form.cleaned_data['thursdayvocabulary']
            thursdayperiod = form.cleaned_data['thursdayperiod']
            thursdayday = form.cleaned_data['thursdayday']
            fridayintro = form.cleaned_data['fridayintro']
            fridayactivity = form.cleaned_data['fridayactivity']
            fridaywrap_up = form.cleaned_data['fridaywrap_up']
            fridayresources = form.cleaned_data['fridayresources']
            fridayblooms = get_MI_BL(fridayactivity)
            fridayvocabulary = form.cleaned_data['fridayvocabulary']
            fridayperiod = form.cleaned_data['fridayperiod']
            fridayday = form.cleaned_data['fridayday']

            if mondayday:
                monday = activities.objects.create(school_lesson_id=obj, weekly_goal=activity_title, subject=subject, week_of=week_of, standard=standard, day='Monday', period = mondayperiod, intro=mondayintro, activity=mondayactivity , wrap_up=mondaywrap_up , resources=mondayresources , bl=mondayblooms[0], mi1=mondayblooms[1], mi2=mondayblooms[2], mi3=mondayblooms[3], vocabulary=mondayvocabulary)
                monday.save()
            if tuesdayday:
                tuesday = activities.objects.create(school_lesson_id=obj, weekly_goal=activity_title, subject=subject, week_of=week_of, standard=standard, day='Tuesday', period = tuesdayperiod, intro=tuesdayintro, activity=tuesdayactivity , wrap_up=tuesdaywrap_up , resources=tuesdayresources , bl=tuesdayblooms[0], mi1=tuesdayblooms[1], mi2=tuesdayblooms[2], mi3=tuesdayblooms[3], vocabulary=tuesdayvocabulary)
                tuesday.save()
            if wednesdayday:
                wednesday = activities.objects.create(school_lesson_id=obj, weekly_goal=activity_title, subject=subject, week_of=week_of, standard=standard, day='Wednesday', period = wednesdayperiod, intro=wednesdayintro, activity=wednesdayactivity , wrap_up=wednesdaywrap_up , resources=wednesdayresources , bl=wednesdayblooms[0], mi1=wednesdayblooms[1], mi2=wednesdayblooms[2], mi3=wednesdayblooms[3], vocabulary=wednesdayvocabulary)
                wednesday.save()
            if thursdayday:
                thursday = activities.objects.create(school_lesson_id=obj, weekly_goal=activity_title, subject=subject, week_of=week_of, standard=standard, day='Thursday', period = thursdayperiod, intro=thursdayintro, activity=thursdayactivity , wrap_up=thursdaywrap_up , resources=thursdayresources , bl=thursdayblooms[0], mi1=mondayblooms[1], mi2=mondayblooms[2], mi3=mondayblooms[3], vocabulary=thursdayvocabulary)
                thursday.save()
            if fridayday:
                friday = activities.objects.create(school_lesson_id=obj, weekly_goal=activity_title, subject=subject, week_of=week_of, standard=standard, day='Friday', period = fridayperiod, intro=fridayintro, activity=fridayactivity , wrap_up=fridaywrap_up , resources=fridayresources , bl=fridayblooms[0], mi1=fridayblooms[1], mi2=fridayblooms[2], mi3=fridayblooms[3], vocabulary=fridayvocabulary)
                friday.save()
            return redirect('weekly_activity', school_url=school_url, week_of=week_of, username=teacher_name)
    else:
        choices = results
        form = WeeklyCreateForm()
        form.fields['standard'].initial = choices
        form.fields['subject'].initial = teacher_subject
        form.fields['school_lesson_id'].initial = obj
        form.fields['week_of'].initial = week_of
        
    return render(request, 'weekly_create.html', {'form': form, 'matches': matches, 'school_url': school_url, 'username': username, 'obj': obj, 'results': results, 'teacher_schedule':teacher_schedule, 'teacher_subject': teacher_subject, 'classroom_name': classroom_name })


def WeeklyActivity(request, school_url=None, week_of=None, username=None):
    teacher = User.objects.get(username=username)
    teacher_pk = teacher.id 
    teacher_name = teacher.username
    obj2 = school.objects.get(url=school_url)
    school_pk = obj2.id
    teacher_schedule = TeacherSchedule.objects.filter(teacher=teacher_pk, school=school_pk)
    object2 = activities.objects.select_related().filter(school_lesson_id__planning_teacher=teacher_pk).filter(week_of=week_of).order_by('period')
    previous = int(week_of) - 1 
    object1 = activities.objects.select_related().filter(week_of=previous)
    next_week = int(week_of) + 1 
    object3 = activities.objects.select_related().filter(week_of=next_week)
    return render(request, 'weekly_activity.html', {'object2': object2, 'object1': object1, 'object3': object3, 'teacher_name': teacher_name, 'school_url': school_url, 'previous': previous, 'next_week': next_week, 'teacher_schedule': teacher_schedule })

def WeeklyActivityClassroom(request, school_url=None, week_of=None, username=None, classroom_id=None):
    teacher = User.objects.get(username=username)
    teacher_name = teacher.username
    classroom_match = classroom.objects.get(Classroom=classroom_id)
    classroom_lesson = lesson_school_info(classroom=classroom_match)
    classroom_lesson_num = classroom_lesson.school_lesson_id
    object2 = activities.objects.select_related().filter(week_of=week_of, school_lesson_id=classroom_lesson_num)
    previous = int(week_of) - 1 
    object1 = activities.objects.select_related().filter(week_of=previous, school_lesson_id=classroom_lesson_num)
    next_week = int(week_of) + 1 
    object3 = activities.objects.select_related().filter(week_of=next_week, school_lesson_id=classroom_lesson_num)
    return render(request, 'weekly_activity.html', {'object2': object2, 'object1': object1, 'object3': object3, 'teacher_name': teacher_name, 'school_url': school_url, 'previous': previous, 'next_week': next_week})


def SingleActivity(request, school_url=None, activity_id=None):
    obj = activities.objects.filter(id=activity_id)
    return render(request, 'single_activity.html', {'obj': obj, 'school_url': school_url})


def CreateActivity(request, school_url=None, planning_id=None, username=None):
    model = lesson_school_info
    model= standards
    obj = lesson_school_info.objects.get(school_lesson_id=planning_id)
    teacher_objective = obj.objective
    teacher_subject = obj.subject
    week_of = obj.week_of
    days = obj.days 

    if request.method == "POST":
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('weekly_activity', school_url=school_url, week_of=week_of, username=username)
    else:
        results = match_standard(teacher_objective, teacher_subject)
        form = ActivityForm()
    return render(request, 'activity.html', {'form': form, 'results': results, 'obj': obj, 'teacher_objective': teacher_objective })

def delete_activity(request, school_url, username, activity_id):
    query = activities.objects.get(id=activity_id)
    query.delete()
    return redirect('profile', school_url=school_url, username=username)

def CreateAssessment(request, school_url=None, planning_id=None, username=None):
    model = lesson_school_info
    model = classroom

    obj = lesson_school_info.objects.get(school_lesson_id=planning_id)
    classroom_name = obj.classroom_id
    obj2 = classroom.objects.get(id=classroom_name)
    students = obj2.student
    if request.method == "POST":
        form = AssessmentForm(request.POST)
        if form.is_valid():
            prev = form.save(commit=False)
            prev.save()
        return redirect('addstudentassessment', school_url=school_url, planning_id=planning_id, assessment_id=prev)
    else:
        form = AssessmentForm()
    return render(request, 'assessment.html', {'form': form, 'school_url': school_url, 'classroom': classroom, 'obj2': obj2, 'students': students })


def AddStudentAssessment(request, school_url=None, planning_id=None, assessment_id=None):
    model = student_assessment
    model = assessments

    obj = assessments.objects.get(id=assessment_id)
    classroom_name = obj.classroom_id
    obj2 = classroom.objects.get(id=classroom_name)
    students = obj2.student

    if request.method == "POST":
        form = StudentAssessmentForm(request.POST)
        if form.is_valid():
            prev = form.save(commit=False)
            prev.save()
        return render(request, 'assessment.html', {'school_url': school_url})
    else:
        form = StudentAssessmentForm()
    return render(request, 'student_assessment.html', {'form': form, 'school_url': school_url, 'obj': obj, 'obj2': obj2, 'students': students})


def TeacherScheduleView(request, school_url=None, username=None):
    current_week = date.today().isocalendar()[1] 
    school_name = school.objects.get(url=school_url)
    school_pk = school_name.id
    teacher = User.objects.get(username=username)
    teacher_pk = teacher.id
    teacher_name = teacher.username
    teacher_weekly = TeacherSchedule.objects.filter(teacher=teacher_pk, school=school_pk)

    if request.method == "POST":
        form = TeacherScheduleForm(request.POST)
        if form.is_valid():
            prev = form.save(commit=False)
            username = prev.teacher
            prev.save()
        return redirect('teacher_scheduleview', school_url=school_url, username=username)
    else:
        form = TeacherScheduleForm()
    return render(request, 'teacher_schedule.html', {'school_url': school_url, 'form': form, 'teacher_weekly': teacher_weekly, 'teacher_name': teacher_name, 'teacher_pk':teacher_pk, 'current_week': current_week})

def delete_schedule(request, school_url, username, schedule_id):
    query = TeacherSchedule.objects.filter(id=schedule_id)
    query.delete()
    return redirect('teacher_scheduleview', school_url=school_url, username=username )

def CreateUpdate(request, school_url=None):
    obj = school.objects.get(url=school_url)
    school_pk = obj.id

    if request.method == "POST":
        form = CreateUpdateForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('school_profile', school_url=school_url)
    else:
        form = CreateUpdateForm()
        form.fields['school'].initial = school_pk
    return render(request, 'create_update.html', {'form': form, 'school_url': school_url})

def CreateEvent(request, school_url=None):
    obj = school.objects.get(url=school_url)
    school_pk = obj.id
    date_now = date.today().isocalendar()

    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('school_profile', school_url=school_url)
        else:
            print(form.errors)
    else:
        form = EventForm()
        form.fields['school'].initial = school_pk
    return render(request, 'create_event.html', {'form': form, 'school_url': school_url})

def delete_update(request, school_url, update_id):
    query = create_updates.objects.get(id=update_id)
    query.delete()
    return redirect('school_profile', school_url=school_url)