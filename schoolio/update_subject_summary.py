from .models import standards, activities, classroom_subject_summary, assessments, student_assessment

def get_understanding_level(score, assessment_id):
    assessment_obj = assessments.objects.all().filter(assessment = assessment_id)[0]
    ss_obj = classroom_subject_summary.objects.all().filter(
              lesson_id = assessment_obj.school_lesson_id)[0]
    if score <= 75:
        understanding_level = 1
    elif score < 90
        understanding_level = 2
    else:
        understanding_level = 3
    assess_attrs = (None, 'lu_low', 'lu_med', 'lu_high')
    ss_attrs = (None, 'lu_level', 'mu_level', 'hu_level')
    setattr(assessment_obj, assess_attrs[understanding_level],
         getattr(assessment_obj, assess_attrs[understanding_level])+1)
    setattr(assessment_obj, ss_attrs[st_assess_obj.understanding_level],
         getattr(ss_obj, ss_attrs[st_assess_obj.understanding_level])+1)
    return understanding_level

def update_MI(lesson_id):
    ss_obj = classroom_subject_summary.objects.all().filter(
             lesson_id = lesson_id)[0]
    for activity_obj in activities.objects.all().filter(
             school_lesson_id = lesson_id):
        mi_to_ss_attr = {
"Logical - Mathematical"  : "logical_level",
"Verbal - Linguistic"     : "linguistic_level",
"Bodily Kinesthetic"      : "kinesthetic_level",
"Musical"                 : "musical_level",
"Visual Spatial"          : "visual_level",
"Naturalist"              : "naturalist_level",
"Interpersonal"           : "group_level",
"Intrapersonal"           : "independent_level"
}
        for mi in activity_obj.mi1, activity_obj.mi2, activity_obj.mi3: 
            attr = mi_to_ss_attr[mi]
            setattr(ss_obj, attr, getattr(ss_obj, attr)+1)


def get_assessment_score(student_score, total_score):
    score = (student_score/total_score) * 100
    return(score)