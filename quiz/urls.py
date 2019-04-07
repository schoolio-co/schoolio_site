try:
    from django.conf.urls import url
except ImportError:
    from django.urls import re_path as url
    
from django.urls import path

from .views import Home, QuizListView, CategoriesListView, \
    ViewQuizListByCategory, QuizUserProgressView, QuizMarkingList, \
    QuizMarkingDetail, QuizDetailView, QuizTake

from ecommerce_app.views import *
from cal.views import *

urlpatterns = [

    url(r'^$',
        view=Home.as_view(),
        name='home'),

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
