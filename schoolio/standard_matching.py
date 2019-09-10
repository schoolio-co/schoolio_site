from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from django.db.models import Q
import pandas as pd 
from .models import standards, activities 
from .evaluate import get_MI_BL

pd.set_option('display.max_colwidth', -1)
count_vect = CountVectorizer()


def match_standard(teacher_input, subject):
        obj = standards.objects.all().filter(subject=subject)
        df = pd.DataFrame(list(obj))
        prediction = []
        for standard in df.iterrows():
                standard = ''.join([str(i) for i in standard])
                Document1= teacher_input
                Document2 = standard
                corpus = [Document1,Document2]
                X_train_counts = count_vect.fit_transform(corpus)
                vectorizer = TfidfVectorizer()
                trsfm=vectorizer.fit_transform(corpus)
                result = cosine_similarity(trsfm[0:1], trsfm)
                result = result[0][1]
                total = standard, result
                prediction.append(total)
        prediction.sort(key=lambda x: x[1], reverse=True)
        results = prediction[:5]
        return(results)

# classroom_subject_summary
def match_activity(classroom_subject, teacher_objective, standard, subject):
        obj = activities.objects.all().filter(subject=subject, standard=standard)
        df = pd.DataFrame(list(obj))
        prediction = []
        classroom_bl = {
"Low"    : classroom_subject.lu_level,
"Medium" : classroom_subject.mu_level,
"High"   : classroom_subject.hu_level
}
        classroom_mi = {
"Logical - Mathematical"  : classroom_subject.logical_level,
"Verbal - Linguistic"     : classroom_subject.linguistic_level,
"Bodily Kinesthetic"      : classroom_subject.kinesthetic_level,
"Musical"                 : classroom_subject.musical_level,
"Visual Spatial"          : classroom_subject.visual_level,
"Naturalist"              : classroom_subject.naturalist_level,
"Interpersonal"           : classroom_subject.group_level,
"Intrapersonal"           : classroom_subject.independent_level
}
        for activity in df.iterrows():
                activity = ''.join(str(i) for i in activity)
                bl, mi1, mi2, mi3 = get_MI_BL(activity)
                result = classroom_bl[bl] + classroom_mi[mi1] + \
                         classroom_mi[mi2] + classroom_mi[mi3]
                total = activity, result
                prediction.append(total)
        prediction.sort(key=lambda x: x[1], reverse=True)
        results = prediction[:5]
        return(results)

# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# from django.db.models import Q
# import pandas as pd 
# from .models import standards, activities 
# 
# pd.set_option('display.max_colwidth', -1)
# count_vect = CountVectorizer()
# 
# 
# def match_standard(teacher_input, subject):
#         obj = standards.objects.all().filter(subject=subject)
#         df = pd.DataFrame(list(obj))
#         prediction = []
#         for standard in df.iterrows():
#             standard = ''.join([str(i) for i in standard])
#             Document1= teacher_input
#             Document2 = standard
#             corpus = [Document1,Document2]
#             X_train_counts = count_vect.fit_transform(corpus)
#             pd.DataFrame(X_train_counts.toarray(),columns=count_vect.get_feature_names(), index=['Document 0','Document 1'])
#             vectorizer = TfidfVectorizer()
#             trsfm=vectorizer.fit_transform(corpus)
#             pd.DataFrame(trsfm.toarray(),columns=vectorizer.get_feature_names(),index=['Document 0','Document 1'])
#             result = cosine_similarity(trsfm[0:1], trsfm)
#             result = result[0][1]
#             total = standard, result
#             prediction.append(total)
#             results = sorted(prediction,key=lambda x: x[1], reverse=True)[:5]
#             return(results)
# 
