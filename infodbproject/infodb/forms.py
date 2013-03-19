from django.forms import ModelForm
from infodb.models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
