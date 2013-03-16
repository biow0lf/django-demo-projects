from django.shortcuts import render_to_response
from infodb.models import Person


def main(request):
    persons = Person.objects.all()
    return render_to_response('main/index.html', {'persons': persons})
