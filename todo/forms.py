from django import forms
from .models import Todo


class TodoForm(forms.Form):
	title = forms.CharField(required=True, max_length=128, label='Enter Todo')

	def save(self):
		return Todo.objects.create(title=self.cleaned_data['title'])


class TodoModelForm(forms.ModelForm):
	class Meta:
		model = Todo
		fields = ('title', 'content',)
		widgets = {
            'content': forms.Textarea(attrs={'cols': 20, 'rows': 2, 'class': 'form-control'}),
        	'title': forms.TextInput(attrs={'class': 'form-control'})
        }