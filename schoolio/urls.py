try:
    from django.conf.urls import url
except ImportError:
    from django.urls import re_path as url

from django.conf import settings
if getattr(settings, 'POSTMAN_I18N_URLS', False):
    from django.utils.translation import pgettext_lazy
else:
    def pgettext_lazy(c, m): return m

from django.urls import path
from django.conf.urls import url
from django.urls import reverse_lazy
from .views import SchoolRegistration, WeeklyActivityClassroom, delete_activity, TeacherScheduleView, delete_schedule, add_students_new_classroom, Student_Profile, SingleClassroom, CreateEvent, add_students_classroom, Import_Data, School_Register, CreateUpdate, School_Profile, Student_Profiles, Profile, Admin_Register, Teacher_Register, Student_Register, Parent_Register, create_grade, create_classroom, Create_School_Lesson, CreateAssessment, CreateActivity, UserList, WeeklyActivity, SingleActivity, CreateWeeklyActivity, login_user, logout_user, RoleRegistrations, AddStudentAssessment, delete_update
from quiz.views import landing, blog

from django.contrib.auth import views as auth_views
from pinax.messages.views import *
from cal.views import *

urlpatterns = [

    url(r"^inbox/$", 
        view=InboxView.as_view(),
        name="inbox"),
    url(r"^create/$", 
        view=MessageCreateView.as_view(),
        name="message_create"),
    url(r"^create/(?P<user_id>\d+)/$", 
        view=MessageCreateView.as_view(),
        name="message_user_create"),
    url(r"^thread/(?P<pk>\d+)/$", 
        view=ThreadView.as_view(),
        name="thread_detail"),
    url(r"^thread/(?P<pk>\d+)/delete/$", 
        view=ThreadDeleteView.as_view(),
        name="thread_delete"),

    url(r'^$',
        view=landing.as_view(),
        name='landing'),

    url(r'home/(?P<school_url>[\w-]+)/create-update/$',
        view=CreateUpdate,
        name='create_update'),

    url(r'home/(?P<school_url>[\w-]+)/create-event/$',
        view=CreateEvent,
        name='create_event'),

    url(r'home/(?P<school_url>[\w-]+)/school-registration/$',
        view=SchoolRegistration.as_view(),
        name='school_registration'),


    url(r'registrations/(?P<school_url>[\w-]+)/',
        view=RoleRegistrations.as_view(),
        name='role_registration'),

    url(r'import/import/',
        view=Import_Data,
        name='import'),

    url('login/(?P<school_url>[\w-]+)',
        view=login_user,
        name='login'),

    url('logout/(?P<school_url>[\w-]+)',
        view=logout_user,
        name='logout'),
    
    url('update-delete/(?P<school_url>[\w-]+)/(?P<update_id>[\w-]+)',
        view=delete_update,
        name='delete_update'),

     url('activity-delete/(?P<school_url>[\w-]+)/(?P<username>[\w-]+)/(?P<activity_id>[\w-]+)',
        view=delete_activity,
        name='delete_activity'),


    url(r'^school-register/',
        view=School_Register,
        name='school_register'),

    url(r'^grade/(?P<school_url>[\w-]+)/create_grade/',
        view=create_grade,
        name='create_grade'),
    
    url(r'^class/(?P<school_url>[\w-]+)/create_classroom/',
        view=create_classroom,
        name='create_classroom'),

    url(r'^class/(?P<school_url>[\w-]+)/(?P<classroom_id>[\w-]+)/classroom/',
        view=SingleClassroom,
        name='single_classroom'),

    url(r'^class/(?P<school_url>[\w-]+)/(?P<username>[\w-]+)/teacher_schedule/',
        view=TeacherScheduleView,
        name='teacher_scheduleview'),

    url(r'^class/(?P<school_url>[\w-]+)/(?P<username>[\w-]+)/(?P<schedule_id>[\w-]+)/schedule_delete/',
        view=delete_schedule,
        name='teacher_scheduledelete'),

    url(r'add-students-new/(?P<school_url>[\w-]+)/(?P<classroom_url>[\w-]+)/(?P<grade_level>[\w-]+)/create-new-classroom/',
        view=add_students_new_classroom,
        name='add_students_new'),

    url(r'add-students/(?P<school_url>[\w-]+)/(?P<grade_level>[\w-]+)/(?P<classroom_id>[\w-]+)/create-classroom/',
        view=add_students_classroom,
        name='add_students'),
    

    url(r'^(?P<school_url>[\w-]+)/admin-register/',
    view=Admin_Register,
    name='admin_register'),

    url(r'^(?P<school_url>[\w-]+)/parent-register/',
    view=Parent_Register,
    name='parent_register'),

    url(r'^(?P<school_url>[\w-]+)/student-register/',
    view=Student_Register,
    name='student_register'),

    url(r'^(?P<school_url>[\w-]+)/teacher-register/',
    view=Teacher_Register,
    name='teacher_register'),

    url(r'^(?P<school_url>[\w-]+)/parent-register/',
    view=Parent_Register,
    name='parent_register'),

    url(r'^(?P<school_url>[\w-]+)/student_profiles/',
    view=Student_Profiles.as_view(),
    name='Student_Profiles'),

    url(r'student/(?P<school_url>[\w-]+)/(?P<student_id>[\w-]+)/',
    view=Student_Profile,
    name='Student'),

    url(r'user-profile/(?P<school_url>[\w-]+)/(?P<username>[\w-]+)/',
        view=Profile.as_view(),
        name='profile'),
    
    url(r'^school_lesson/(?P<school_url>[\w-]+)/(?P<username>[\w-]+)/',
        view=Create_School_Lesson,
        name='school_lesson'),
    
    url(r'^school_lesson/(?P<school_url>[\w-]+)/(?P<username>[\w-]+)/(?P<week_of>[\w-]+)/',
        view=Create_School_Lesson,
        name='school_lesson_week'),
    
    url(r'^assessment/(?P<school_url>[\w-]+)/(?P<planning_id>[\w-]+)/',
        view=CreateAssessment,
        name='assessment'),

    url(r'^student-assessment/(?P<school_url>[\w-]+)/(?P<planning_id>[\w-]+)/(?P<assessment_id>[\w-]+)/',
        view=AddStudentAssessment,
        name='addstudentassessment'),

    url(r'^l/(?P<school_url>[\w-]+)/(?P<planning_id>[\w-]+)/(?P<username>[\w-]+)/(?P<week_of>[\w-]+)/activity/',
        view=CreateWeeklyActivity,
        name='weeklyactivitycreate'),
    
    url(r'^create/(?P<school_url>[\w-]+)/(?P<planning_id>[\w-]+)/(?P<username>[\w-]+)/activity/',
        view=CreateActivity,
        name='activity'),

    url(r'^weekly/(?P<school_url>[\w-]+)/(?P<username>[\w-]+)/(?P<week_of>[\w-]+)/activity/',
        view=WeeklyActivity,
        name='weekly_activity'),

    url(r'weekly-classroom/(?P<school_url>[\w-]+)/(?P<username>[\w-]+)/(?P<week_of>[\w-]+)/(?P<classroom_id>[\w-]+)/activity/',
        view=WeeklyActivityClassroom,
        name='weekly_activity_classroom'),

    url(r'^l/(?P<school_url>[\w-]+)/activity/(?P<activity_id>[\w-]+)/',
        view=SingleActivity,
        name='single_activity'),

     url(r'^users/(?P<school_url>[\w-]+)/',
        view=UserList,
        name='user_list'),

    url(r'^blog/$',
        view=blog.as_view(),
        name='blog'),


]