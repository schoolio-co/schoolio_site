from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe
from django.views.generic import DetailView, ListView, TemplateView, FormView
import operator
from django.db.models import Q
from functools import reduce
from .models import *
from .utils import Calendar

def cal_index(request):
    return HttpResponse('hello')

class CalendarView(generic.ListView):
    model = Event
    template_name = 'cal/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

class EventListView(ListView):
    model = Event
    
    def get_queryset(self):
        queryset = super(EventListView, self).get_queryset()
        return queryset.filter()

class EventSearchListView(CalendarView):
    """
    Display a Event List page filtered by the search query.
    """
    paginate_by = 10

    def get_queryset(self):
        result = super(EventSearchListView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(title__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(category__icontains=q) for q in query_list))
            )

        return result