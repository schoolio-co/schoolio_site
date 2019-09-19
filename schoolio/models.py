from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

class school(models.Model):
	name = models.CharField(max_length=30)
	address = models.TextField(max_length=250)
	url = models.SlugField(blank=False, unique=True,
        help_text=_("www.schoolio.co/...."),
        verbose_name=_("www.schoolio.co/...."))

	def get_absolute_url(self):
		return reverse("school_profile", kwargs={"slug": self.url})

	def __str__(self):
		return self.url

class User(AbstractUser):
	is_parent = models.BooleanField(default=False)
	is_teacher = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)
	is_student = models.BooleanField(default=False)
	school = models.ForeignKey(school, 
							on_delete=models.CASCADE,
							blank=True,
        					null=True)

class grade_level(models.Model):
	grade = models.CharField(max_length=30)
	school = models.ForeignKey(school, 
							on_delete=models.CASCADE,
							blank=True,
        					null=True)

	def __str__(self):
		return "%s" % (self.grade)


class school_user(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='user_role')
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	username = models.CharField(max_length=30)
	email = models.EmailField(blank=True,
        					  null=True)
	school = models.ForeignKey(school, 
							on_delete=models.CASCADE,
							blank=True,
        					null=True)


	def __str__(self):
		return "%s" % (self.username)



class standards(models.Model):
	grade_level = models.TextField(max_length=50)
	subject = models.TextField(max_length=500)
	standard = models.TextField(max_length=500)
	skill_topic = models.TextField(max_length=500)
	objective = models.TextField(max_length=500)
	competency = models.TextField(max_length=1000)

	def __str__(self):
		return "%s" % (self.competency)

class day_of_the_week(models.Model):
	days = models.CharField(max_length=15)

	def __str__(self):
		return "%s" % (self.days)

class create_updates(models.Model):
	update_title = models.TextField(max_length=150)
	update = models.TextField(max_length=1000)
	school = models.ForeignKey(school, 
							on_delete=models.CASCADE,
							blank=True,
        					null=True)

	def __str__(self):
		return "%s" % (self.update_title)

class subjects(models.Model):
	subject = models.CharField(max_length=50)

	def __str__(self):
		return "%s" % (self.subject)

class student_profiles(models.Model):
	student_ref = models.CharField(max_length=50)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	grade_level = models.CharField(max_length=30)
	school = models.ForeignKey(school, 
							on_delete=models.CASCADE,
							blank=True,
        					null=True)
	d_o_b = models.DateTimeField(blank=True,
        					     null=True)

	def __str__(self):
		return '%s %s' % (self.first_name, self.last_name)

class classroom(models.Model):
	Classroom = models.CharField(max_length=30)
	grade_level = models.CharField(max_length=30)
	school = models.ForeignKey(school, 
							on_delete=models.CASCADE,
							blank=True,
        					null=True)
	student = models.ManyToManyField(student_profiles,
							blank=True,
							related_name='student')
	

	def __str__(self):
		return "%s" % (self.Classroom)


class lesson_school_info(models.Model):
	school_lesson_id = models.AutoField(primary_key=True)
	classroom = models.ForeignKey(classroom, 
							on_delete=models.CASCADE,
							blank=True,
        					null=True)
	school = models.ForeignKey(school, 
							on_delete=models.CASCADE,
							blank=True,
        					null=True)
	week_of = models.CharField(max_length=30)	
	date = models.DateTimeField(default=now)
	subject = models.CharField(max_length=100)
	days = models.CharField(max_length=100)	
	objective = models.TextField(max_length=500)
	planning_teacher = models.CharField(max_length=30)

	def get_absolute_url(self):
		return ("school_lesson")

	def __str__(self):
		return "%s" % (self.school_lesson_id)


		
class activities(models.Model):
	school_lesson_id = models.IntegerField()
	weekly_goal = models.CharField(max_length=500)
	subject =  models.CharField(max_length=500)
	week_of =  models.CharField(max_length=5)
	standard =  models.CharField(max_length=500)
	intro = models.CharField(max_length=500)
	activity = models.TextField(max_length=1000)
	wrap_up = models.CharField("Essential Questions", max_length=500)
	resources = models.CharField(max_length=100)
	bl = models.CharField(max_length=50)
	mi1 = models.CharField(max_length=50)
	mi2 = models.CharField(max_length=50)
	mi3 = models.CharField(max_length=50)
	vocabulary = models.CharField(max_length=100)
	day = models.CharField(max_length=100)
	

	def __str__(self):
		return "%s" % (self.intro)


class assessments(models.Model):
	activity =  models.ForeignKey(activities, 
							on_delete=models.CASCADE,
							blank=True,
        					null=True)
	assessment = models.CharField(max_length=150)
	is_formal = models.BooleanField(default=False)
	is_final = models.BooleanField(default=False)
	is_informal = models.BooleanField(default=False)
	classroom = models.ForeignKey(classroom, 
							on_delete=models.CASCADE,
							blank=True,
        					null=True)
	assessment_total = models.IntegerField()

	def __str__(self):
		return "%s" % (self.pk)

class student_assessment(models.Model):
	assessment =  models.ForeignKey(assessments, 
							on_delete=models.CASCADE,
							blank=True,
        					null=True)
	student = models.ManyToManyField(student_profiles,
							blank=True,)
	assessment_mark = models.IntegerField()

	def __str__(self):
		return "%s" % (self.student)

class classroom_averages(models.Model):
	classroom = models.ForeignKey(classroom, 
							on_delete=models.CASCADE,
							blank=True,
        					null=True)
	subject = models.ForeignKey(subjects, 
							on_delete=models.CASCADE,
							blank=True,
        					null=True)
	mi_one = models.CharField(max_length=30)
	mi_two = models.CharField(max_length=30)
	mi_three = models.CharField(max_length=30)
	lu_low = models.CharField(max_length=30)
	lu_med = models.CharField(max_length=30)
	lu_high = models.CharField(max_length=30)

class classroom_subject_summary(models.Model):
	classroom = models.ForeignKey(classroom,
							on_delete=models.CASCADE,
							blank=True,
        					null=True)
	subject = models.TextField()
	lu_level = models.FloatField(null=True, blank=True)
	mu_level = models.FloatField(null=True, blank=True)
	hu_level = models.FloatField(null=True, blank=True)
	logical_level = models.IntegerField()
	linguistic_level = models.IntegerField()
	kinesthetic_level = models.IntegerField()
	musical_level = models.IntegerField()
	visual_level = models.IntegerField()
	naturalist_level = models.IntegerField()
	group_level = models.IntegerField()
	independent_level = models.IntegerField()
	
	def __str__(self):
		return "%s" % (self.classroom)

class TeacherSchedule(models.Model):
	classroom = models.ForeignKey(classroom,
						on_delete=models.CASCADE,
						blank=True,
						null=True)
	location = models.CharField(max_length=100)
	Subject = models.CharField(max_length=100)
	teacher = models.ForeignKey(User, 
							on_delete=models.CASCADE,
							blank=True,
        					null=True, 
							related_name='teacher')
	period = models.IntegerField()
	day = models.CharField(max_length=100)

	def __str__(self):
		return "%s" % (self.teacher)

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=30, default='main')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    school = models.ForeignKey(school, 
							on_delete=models.CASCADE,
							blank=True,
        					null=True)

    def __str__(self):
        return self.title