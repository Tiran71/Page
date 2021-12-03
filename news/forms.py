from django.db.models import fields
from django.forms import ModelForm, widgets
from .models import Public

class PublicForm(ModelForm):
    class Meta:
        model = Public
        fields = ['title', 'text', 'date']

        widgets={ 
            'title': widgets.TextInput(attrs={'placeholder':'Заголовок'}),
            'text': widgets.Textarea(attrs={'placeholder':'текст'}),
            'date': widgets.DateInput(attrs={'placeholder':'дата публикации'})
        }