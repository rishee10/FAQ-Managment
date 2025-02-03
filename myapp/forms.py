from django import forms
from .models import FAQ
from ckeditor.widgets import CKEditorWidget

class FAQForm(forms.ModelForm):
    answer = forms.CharField(widget=CKEditorWidget(config_name='default'))

    class Meta:
        
        model = FAQ
        fields = ('question', 'answer', 'question_hi', 'answer_hi', 'question_bn', 'answer_bn')
