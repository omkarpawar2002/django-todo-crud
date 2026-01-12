from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description']
        labels = {
            'title':'Title',
            'description':'Description'
        }
        widgets = {
            'description':forms.Textarea(attrs={
                'rows':'3'
            })
        }