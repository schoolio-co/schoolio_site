from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from quiz.models import Question
from django.db import models
from sklearn.feature_extraction.text import TfidfVectorizer




@python_2_unicode_compatible
class Essay_Question(Question):

    def check_if_correct(self, guess):
        guess = guess
        answer = Answer.content

    def order_answers(self, queryset):
        return queryset.order_by()


    def get_answers(self):
        return self.order_answers(Answer.objects.filter(question=self))

    def get_answers_list(self):
        return Answer.content.get(id=guess)

    def answer_choice_to_string(self, guess):
        return str(guess)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = _("Essay style question")
        verbose_name_plural = _("Essay style questions")

@python_2_unicode_compatible
class Answer(models.Model):
    question = models.ForeignKey(Essay_Question, verbose_name=_("Question"), on_delete=models.CASCADE)

    content = models.CharField(max_length=1000,
                               blank=False,
                               help_text=_("Enter the answer text that "
                                           "you want displayed"),
                               verbose_name=_("Content"))


    def __str__(self):
        return self.content

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
