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
from .views import SchoolRegistration, CreateEvent, Import_Data, School_Register, CreateUpdate, School_Profile, Student_Profiles, Profile, Admin_Register, Teacher_Register, Student_Register, Parent_Register, create_grade, create_classroom, Create_School_Lesson, CreateAssessment, CreateActivity, UserList, WeeklyActivity, SingleActivity, CreateWeeklyActivity, login_user, logout_user, RoleRegistrations, delete_update
from quiz.views import elearning, landing, blog, user_profile, QuizListView, CategoriesListView, \
    ViewQuizListByCategory, QuizUserProgressView, QuizMarkingList, \
    QuizMarkingDetail, QuizDetailView, QuizTake

from django.contrib.auth import views as auth_views
from ecommerce_app.views import *
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

    url(r'home/(?P<school_url>[\w-]+)/',
        view=School_Profile.as_view(),
        name='school_profile'),

    url(r'registrations/(?P<school_url>[\w-]+)/',
        view=RoleRegistrations.as_view(),
        name='role_registration'),

    url(r'^import/$',
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


    url(r'^school-register/',
        view=School_Register,
        name='school_register'),

    url(r'^grade/(?P<school_url>[\w-]+)/create_grade/',
        view=create_grade,
        name='create_grade'),
    
    url(r'^class/(?P<school_url>[\w-]+)/(?P<username>[\w-]+)/create_classroom/',
        view=create_classroom,
        name='create_classroom'),
    
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

    url(r'(?P<school_url>[\w-]+)/user/(?P<username>[\w-]+)/',
        view=Profile.as_view(),
        name='profile'),
    
    url(r'^(?P<school_url>[\w-]+)/(?P<username>[\w-]+)/school_lesson/',
        view=Create_School_Lesson,
        name='school_lesson'),
    
    url(r'^(?P<school_url>[\w-]+)/(?P<username>[\w-]+)/(?P<week_of>[\w-]+)/school_lesson/',
        view=Create_School_Lesson,
        name='school_lesson_week'),
    
    url(r'^(?P<school_url>[\w-]+)/assessment/',
        view=CreateAssessment,
        name='assessment'),

    url(r'^l/(?P<school_url>[\w-]+)/(?P<planning_id>[\w-]+)/(?P<username>[\w-]+)/(?P<week_of>[\w-]+)/activity/',
        view=CreateWeeklyActivity,
        name='weeklyactivitycreate'),
    
    url(r'^create/(?P<school_url>[\w-]+)/(?P<planning_id>[\w-]+)/(?P<username>[\w-]+)/activity/',
        view=CreateActivity,
        name='activity'),

    url(r'^weekly/(?P<school_url>[\w-]+)/(?P<username>[\w-]+)/(?P<week_of>[\w-]+)/activity/',
        view=WeeklyActivity,
        name='weekly_activity'),

    url(r'^l/activity/(?P<activity_id>[\w-]+)/',
        view=SingleActivity,
        name='single_activity'),

     url(r'^users/(?P<school_url>[\w-]+)/',
        view=UserList,
        name='user_list'),

        url(r'^elearning$',
        view=elearning.as_view(),
        name='elearning'),


    url(r'^blog/$',
        view=blog.as_view(),
        name='blog'),

     url(r'^profile/$',
        view=user_profile.as_view(),
        name='profile'),

    url(r'^quizzes/$',
        view=QuizListView.as_view(),
        name='quiz_index'),

    url(r'^index/$',
        view=index,
        name='index'),


    path('product/<int:product_id>/<slug:product_slug>/',
        view=show_product, 
        name='product_detail'),


    url(r'^cart/$', 
        view=show_cart, 
        name='show_cart'),

    url(r'^checkout/$', 
        view=checkout, 
        name='checkout'),

    path('process-payment/', 
        view=process_payment, 
        name='process_payment'),

    path('payment-done/', 
        view=payment_done, 
        name='payment_done'),

    path('payment-cancelled/', 
        view=payment_canceled, 
        name='payment_cancelled'),
    
     path('subscribe/', 
        view=subscription, 
        name='subscription'),

    path('process_subscription/', 
        view=process_subscription, 
        name='process_subscription'),

    url(r'^cal_index/$', 
        view=cal_index, name='cal_index'),

    url(r'^cal_search/$', 
        view=EventSearchListView.as_view(), 
        name='event_search_list_view'),
    
    url(r'^calendar/$', 
        view=CalendarView.as_view(), 
        name='calendar'),

    url(r'^category/$',
        view=CategoriesListView.as_view(),
        name='quiz_category_list_all'),

    url(r'^category/(?P<category_name>[\w|\W-]+)/$',
        view=ViewQuizListByCategory.as_view(),
        name='quiz_category_list_matching'),

    url(r'^progress/$',
        view=QuizUserProgressView.as_view(),
        name='quiz_progress'),

    url(r'^marking/$',
        view=QuizMarkingList.as_view(),
        name='quiz_marking'),

    url(r'^marking/(?P<pk>[\d.]+)/$',
        view=QuizMarkingDetail.as_view(),
        name='quiz_marking_detail'),

    #  passes variable 'quiz_name' to quiz_take view
    url(r'^(?P<slug>[\w-]+)/$',
        view=QuizDetailView.as_view(),
        name='quiz_start_page'),

    url(r'^(?P<quiz_name>[\w-]+)/take/$',
        view=QuizTake.as_view(),
        name='quiz_question'),



]