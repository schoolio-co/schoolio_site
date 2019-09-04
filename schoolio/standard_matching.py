from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from django.db.models import Q
import pandas as pd 
from .models import standards, activities 

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
            pd.DataFrame(X_train_counts.toarray(),columns=count_vect.get_feature_names(), index=['Document 0','Document 1'])
            vectorizer = TfidfVectorizer()
            trsfm=vectorizer.fit_transform(corpus)
            pd.DataFrame(trsfm.toarray(),columns=vectorizer.get_feature_names(),index=['Document 0','Document 1'])
            result = cosine_similarity(trsfm[0:1], trsfm)
            result = result[0][1]
            total = standard, result
            prediction.append(total)
            results = sorted(prediction,key=lambda x: x[1], reverse=True)[:5]
            return(results)

