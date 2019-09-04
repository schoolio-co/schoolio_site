import csv

# import the relevant model
from .models import standards

def import_csv(self):
    path = 'schoolio/standards/Grade One.csv'
    with open(path) as f:
        for line in f:
            line = line.split(',') 
            obj, created = standards.objects.get_or_create(subject=line[0], standard=line[1], skill_topic=line[2], objective=line[3], competency=line[4])
            obj.save()