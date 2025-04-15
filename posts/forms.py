from django import forms
from .models import PostContent, PostSchedule

class PostContentForm(forms.ModelForm):
    class Meta:
        model = PostContent
        fields = ['title', 'body', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class PostScheduleForm(forms.ModelForm):
    class Meta:
        model = PostSchedule
        fields = ['content', 'scheduled_time']
        widgets = {
            'scheduled_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-input'}),
        }