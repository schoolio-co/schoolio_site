from django.contrib import admin
from .models import school, User, standards, day_of_the_week, lesson_school_info,  subjects, activities, classroom_subject_summary

admin.site.register(school)
admin.site.register(User)
admin.site.register(standards)
admin.site.register(lesson_school_info)
admin.site.register(subjects)
admin.site.register(day_of_the_week)
admin.site.register(activities)
admin.site.register(classroom_subject_summary)

