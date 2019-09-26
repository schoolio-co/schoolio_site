from .models import standards, activities, classroom_subject_summary, assessments, student_assessment

def get_understanding_level(assessment_id, student_id):
    assessment_obj = assessments.objects.all().filter(assessment = assessment_id)[0]
    st_assess_obj  = student_assessment.objects.all().filter(assessment = assessment_id,
                      student = student_id)[0]
    ss_obj = classroom_subject_summary.objects.all().filter(
              lesson_id = assessment_obj.school_lesson_id)[0]
    score = st_assess_obj.assessment_mark // assessment_obj.total_possible
    st_assess_obj.assessment_score = score
    if score <= 75:
        understanding_level = 1
    elif score < 90
        understanding_level = 2
    else:
        understanding_level = 3
    assess_attrs = (None, 'lu_low', 'lu_med', 'lu_high')
    ss_attrs = (None, 'lu_level', 'mu_level', 'hu_level')
    if st_assess_obj.understanding_level != 0:
        setattr(assessment_obj, assess_attrs[st_assess_obj.understanding_level],
             getattr(ss_obj, assess_attrs[st_assess_obj.understanding_level])-1)
        setattr(assessment_obj, ss_attrs[st_assess_obj.understanding_level],
             getattr(ss_obj, ss_attrs[st_assess_obj.understanding_level])-1)
    st_assess_obj.understanding_level = understanding_level
    setattr(assessment_obj, assess_attrs[understanding_level],
         getattr(assessment_obj, assess_attrs[understanding_level])+1)
    setattr(assessment_obj, ss_attrs[st_assess_obj.understanding_level],
         getattr(ss_obj, ss_attrs[st_assess_obj.understanding_level])+1)
    labels = (None, 'Low', 'Med', 'High')
    return labels[understanding_level]
