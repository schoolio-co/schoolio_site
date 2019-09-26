from django.contrib import admin
from .models import school, User, TeacherSchedule, student_profiles, standards, day_of_the_week, classroom, lesson_school_info,  subjects, activities, classroom_subject_summary

admin.site.register(school)
admin.site.register(standards)
admin.site.register(lesson_school_info)
admin.site.register(subjects)
admin.site.register(User)
admin.site.register(day_of_the_week)
admin.site.register(student_profiles)
admin.site.register(activities)
admin.site.register(classroom)
admin.site.register(classroom_subject_summary)
admin.site.register(TeacherSchedule)

