from django import forms
from django.core import validators

from examination.models import examination, ExaminationQuestionModel, ExaminationAnswerModel


def name_check(value):
    if value.isalpha() != True:
        raise forms.ValidationError("only string are allowed")
     
class examinationForm(forms.ModelForm):
   

    class Meta:
        model = examination
        fields ='__all__'


class examinationquestionForm(forms.ModelForm):
    subject = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    question1 = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    question2 = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    question3 = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    question4 = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    question5 = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    question6 = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    question7 = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    question8 = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    question9 = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    question10 = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)

    def __str__(self):
        return self.subject

    class Meta:
        model = ExaminationQuestionModel
        fields = ['subject', 'question1', 'question2', 'question3', 'question4', 'question5', 'question6', 'question7',
                  'question8', 'question9', 'question10']


class examinationanswerForm(forms.ModelForm):
    subject = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    answer1 = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    answer2 = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    answer3 = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    answer4 = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    answer5 = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    answer6 = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    answer7 = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    answer8 = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    answer9 = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    answer10 = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)

    def __str__(self):
        return self.subject

    class Meta:
        model = ExaminationAnswerModel
        fields = ['subject', 'answer1', 'answer2', 'answer3', 'answer4', 'answer5', 'answer6', 'answer7', 'answer8',
                  'answer9', 'answer10']
