from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from quiz.models import Question
from django.db import models
import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer


nltk.download('punkt')

@python_2_unicode_compatible
class Essay_Question(Question):

    def check_if_correct(self, guess):
        guess = Answer.objects.get(id=guess)
        answer = Answer.content

    def assess(answer,guess):
        stemmer = nltk.stem.porter.PorterStemmer()
        remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

        def stem_tokens(tokens):
            return [stemmer.stem(item) for item in tokens]


        def normalize(text):
            return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

            vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')

        def cosine_sim(text1, text2):
            tfidf = vectorizer.fit_transform([text1, text2])
            return ((tfidf * tfidf.T).A)[0,1]

            base = cosine_sim(answer, answer)
            results = (cosine_sim(answer, guess))

            score = (base + results)/2

        if score >= .50:
            return True
        else:
            return False

    def get_answers(self):
        return self.order_answers(Answer.objects.filter(question=self))

    def get_answers_list(self):
        return Answer.objects.get(id=guess).content

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