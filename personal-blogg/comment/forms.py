from django import forms
from django.db import models
from .models import Comment,Edit,Report
# comment form

# class CommentForm(forms.Form):
#     name = forms.CharField(max_length= 30)
#     comment = forms.TextField()

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','comment','activate','time','image']
        labels = {
            'image':'',
        }
        

    # name = forms.CharField(max_length= 30)
    # comment = forms.TextInput()

class EditForm(forms.ModelForm):
    class Meta:
        model = Edit
        fields = ['username','password']


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['report']