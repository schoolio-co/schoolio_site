from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe
from django.views.generic import DetailView, ListView, TemplateView, FormView

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
        return queryset.filter(draft=False)

def search(request):
        if 'q' in request.GET:
          #Get the selected category id 
          sel_category = request.GET.get('category', None)
          #If it exists, get the category object
          if sel_category: 
                category = get_object_or_404(Category, pk = sel_category)
          query = request.GET['q']
          results = Adv.objects.filter(title__icontains=query)
          #If category objects exists filter the result set based on that
          if category:
                    results =results.filter(cate__name__icontains=category.name)
       #   print results.query 
        else:
          query = ""
          results = None
          categories = Category.objects.all()
        template = loader.get_template('search/search1.html')
        context = Context({ 'query': query, 'results': results, 'city_list': ChoiceCity.objects.all(), 'categories':categories })
        response = template.render(context)
        return HttpResponse(response) 
