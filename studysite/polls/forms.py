from django.forms import ModelForm
from polls.models import *

class Form(ModelForm):
    class Meta:
        model = Question
        fields=['question_text']