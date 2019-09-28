from .models import standards, activities, classroom_subject_summary, assessments, student_assessment, student_assessment, student_profiles

def get_student_stats(student_id):
    student = student_profiles.objects.all().filter(id = student_id)[0]
    MI_to_BL_scores = {
"Logical - Mathematical": [0,0,0],
"Verbal - Linguistic"   : [0,0,0],
"Bodily Kinesthetic"    : [0,0,0],
"Musical"               : [0,0,0],
"Visual Spatial"        : [0,0,0],
"Naturalist"            : [0,0,0],
"Interpersonal"         : [0,0,0],
"Intrapersonal"         : [0,0,0]
}
    for assessment in student_assessment.objects.all().filter(student = student_id):
        index = int(assessment.understanding_level - 1)
        for activity in activities.objects.all().filter(school_lesson_id = assessment.school_lesson_id):
            MI_to_BL_scores[activity.mi1][index] += 1
            MI_to_BL_scores[activity.mi2][index] += 1
            MI_to_BL_scores[activity.mi3][index] += 1
    # So now we have all the numbers. Time to normalize them.
    for key in MI_to_BL_scores.keys():
        if all(x == 0 for x in MI_to_BL_scores[key]):
            MI_to_BL_scores[key][1] = 1 # default to medium level of understanding. TODO maybe I should return something to signal that no lessons have covered this?
        else:
            l, m, h = MI_to_BL_scores[key]
            MI_to_BL_scores[key] = (.9*h+.1*m)/(l+m+h)
    return MI_to_BL_scores
