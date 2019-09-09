from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

class school(models.Model):
	name = models.CharField(max_length=30)
	address = models.TextField(max_length=250)
	url = models.SlugField(
        max_length=60, blank=False,
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
	email = models.EmailField()
	school = models.ForeignKey(school, 
							on_delete=models.CASCADE,
							blank=True,
        					null=True)


	def __str__(self):
		return "%s %s" % (self.first_name, self.last_name)


class classroom(models.Model):
	classroom = models.CharField(max_length=30)
	grade = models.ForeignKey(grade_level, 
							on_delete=models.CASCADE,
							blank=True,
        					null=True)
	school = models.ForeignKey(school, 
							on_delete=models.CASCADE,
							blank=True,
        					null=True)
	teacher = models.ForeignKey(User,
							on_delete=models.CASCADE,
							blank=True,
        					null=True, 
							related_name='teacher')
	

	def __str__(self):
		return "%s" % (self.classroom)

class classroom_subject_summary(models.Model):
	classroom = models.ForeignKey(classroom,
							on_delete=models.CASCADE,
							blank=True,
        					null=True)
	subject = models.TextField(max_length=50)
	lu_level = models.IntegerField(max_length=10)
	mu_level = models.IntegerField(max_length=10)
	hu_level = models.IntegerField(max_length=10)
	logical_level = models.IntegerField(max_length=10)
	linguistic_level = models.IntegerField(max_length=10)
	kinesthetic_level = models.IntegerField(max_length=10)
	musical_level = models.IntegerField(max_length=10)
	visual_level = models.IntegerField(max_length=10)
	naturalist_level = models.IntegerField(max_length=10)
	group_level = models.IntegerField(max_length=10)
	independent_level = models.IntegerField(max_length=10)
	

	

	def __str__(self):
		return "%s" % (self.classroom)


class student_profiles(models.Model):
	user = models.OneToOneField(User,
							on_delete=models.CASCADE,
							blank=True,
        					null=True, 
							related_name='student_info')
	teacher = models.ForeignKey(User,
							on_delete=models.CASCADE,
							blank=True,
        					null=True, 
							related_name='teacher_info')
	parent = models.ForeignKey(User,
							on_delete=models.CASCADE,
							blank=True,
        					null=True, 
							related_name='parent_info')
	classroom = models.ForeignKey(classroom,
							on_delete=models.CASCADE,
							blank=True,
        					null=True)
	grade = models.ForeignKey(grade_level,
							on_delete=models.CASCADE,
							blank=True,
        					null=True)
	school = models.ForeignKey(school, 
							on_delete=models.CASCADE,
							blank=True,
        					null=True)

	def __str__(self):
		return "%s" % (self.user)

class standards(models.Model):
	subject = models.TextField(max_length=50)
	standard = models.TextField(max_length=100)
	skill_topic = models.TextField(max_length=100)
	objective = models.TextField(max_length=150)
	competency = models.TextField(max_length=1000)

	def __str__(self):
		return "%s" % (self.competency)

class day_of_the_week(models.Model):
	days = models.CharField(max_length=15)

	def __str__(self):
		return "%s" % (self.days)

class subjects(models.Model):
	subject = models.CharField(max_length=50)

	def __str__(self):
		return "%s" % (self.subject)



class assessments(models.Model):
	activity =  models.ForeignKey(school, 
							on_delete=models.CASCADE,
							blank=True,
        					null=True)
	assessment = models.TextField(max_length=500)
	is_formal = models.BooleanField(default=False)
	is_final = models.BooleanField(default=False)
	is_informal = models.BooleanField(default=False)
	student = models.ManyToManyField(User,
							blank=True,
        					null=True, 
							related_name='student_assessment')
	assessment_mark = models.TextField(max_length=50)

	def __str__(self):
		return "%s" % (self.assessment)


class lesson_school_info(models.Model):
	school_lesson_id = models.AutoField(primary_key=True)
	classroom = models.ForeignKey(classroom, 
							on_delete=models.CASCADE,
							blank=True,
        					null=True)
	grade = models.ForeignKey(grade_level, 
							on_delete=models.CASCADE,
							blank=True,
        					null=True)
	school = models.ForeignKey(school, 
							on_delete=models.CASCADE,
							blank=True,
        					null=True)
	teacher = models.CharField(max_length=30)
	week_of = models.CharField(max_length=30)	
	date = models.DateTimeField(default=now)
	subject = models.CharField(max_length=100)
	days = models.CharField(max_length=100)	
	objective = models.TextField(max_length=500)

	def get_absolute_url(self):
		return ("school_lesson")

	def __str__(self):
		return "%s" % (self.school_lesson_id)


		
class activities(models.Model):
	school_lesson_id = models.IntegerField()
	activity_title = models.CharField(max_length=500)
	subject =  models.CharField(max_length=500)
	week_of =  models.CharField(max_length=5)
	standard =  models.CharField(max_length=500)
	intro = models.CharField(max_length=500)
	activity = models.TextField(max_length=1000)
	wrap_up = models.CharField(max_length=500)
	resources = models.CharField(max_length=100)
	blooms = models.CharField(max_length=100)
	vocabulary = models.CharField(max_length=100)
	day = models.CharField(max_length=100)
	

	def __str__(self):
		return "%s" % (self.activity_title)

class classroom_averages(models.Model):
	classroom = models.ForeignKey(classroom, 
							on_delete=models.CASCADE,
							blank=True,
        					null=True)
	subject = models.ForeignKey(subjects, 
							on_delete=models.CASCADE,
							blank=True,
        					null=True)
	mi_one = models.TextField()
	mi_two = models.TextField()
	mi_three = models.TextField()
	lu_low = models.TextField()
	lu_med= models.TextField()
	lu_high = models.TextField()
