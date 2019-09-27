#from .models import standards, activities, classroom_subject_summary, assessments, student_assessment
import dash
import dash_core_components as dcc
import dash_html_components as html
from .as_dash import create_app

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}


def visualize_assessment_understanding_level(assessment_id):
    assessment_obj = assessments.objects.all().filter(assessment = assessment_id)[0]
    return visualize_understanding_level(assessment_obj.lu_low, assessment_obj.lu_med, assessment_obj.lu_high)
def visualize_subject_summary_understanding_level(lesson_id):
    ss_obj = classroom_subject_summary.objects.all().filter(assessment = assessment_id)[0]
    return visualize_understanding_level(ss_obj.lu_level, ss_obj.mu_level, ss_obj.hu_level)
def visualize_subject_summary_MI(lesson_id):
    ss_obj = classroom_subject_summary.objects.all().filter(assessment = assessment_id)[0]
    return visualize_MI(ss_obj.logical_level,
        ss_obj.linguistic_level,
        ss_obj.kinesthetic_level,
        ss_obj.musical_level,
        ss_obj.visual_level,
        ss_obj.naturalist_level,
        ss_obj.group_level,
        ss_obj.independent_level)
def visualize_subject_summary(lesson_id):
    pass


def visualize_understanding_level(low, medium, high):
    app = create_app()
    
    app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
        html.H1(
            children='Understanding Levels',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
        ),
    
        #html.Div(children='Dash: A web application framework for Python.', style={
        #    'textAlign': 'center',
        #    'color': colors['text']
        #}),
    
        dcc.Graph(
            id='example-graph-2',
            figure={
                'data': [
                    {'x': ['Low', 'Medium', 'High'], 'y': [3, 8, 4], 'type': 'bar'},
                ],
                'layout': {
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': {
                        'color': colors['text']
                    }
                }
            }
        )
    ])
    return app
def visualize_MI(log, verb, bod, mus, vis, nat, inter, intra):
    app = create_app()
    
    app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
        html.H1(
            children='Multiple Intelligences',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
        ),
    
        html.Div(children='History of multiple intelligences used this week.', style={
            'textAlign': 'center',
            'color': colors['text']
        }),
    
        dcc.Graph(
            id='example-graph-2',
            figure={
                'data': [
                    {'x': [
"Logical - Mathematical",
"Verbal - Linguistic"   ,
"Bodily Kinesthetic"    ,
"Musical"               ,
"Visual Spatial"        ,
"Naturalist"            ,
"Interpersonal"         ,
"Intrapersonal"         ], 'y': [
log,
verb,
bod,
mus,
vis,
nat,
inter,
intra], 'type': 'bar'},
                ],
                'layout': {
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': {
                        'color': colors['text']
                    }
                }
            }
        )
    ])
    return app



if __name__ == '__main__':
    app = visualize_MI(1, 2, 3, 2, 5, 2, 1, 8)
    app.run_server(debug=True)
