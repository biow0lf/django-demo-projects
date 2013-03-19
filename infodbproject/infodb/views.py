from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from infodb.models import Person
from infodb.forms import PersonForm


def main(request):
    persons = Person.objects.all()
    return render_to_response('main/index.html', {'persons': persons},
        context_instance=RequestContext(request))


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def edit(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    form = PersonForm(request.POST or None, instance=person)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    else:
        return render_to_response('main/edit.html',
                                  {'form': form,
                                   'person_id': person_id},
                context_instance=RequestContext(request))
