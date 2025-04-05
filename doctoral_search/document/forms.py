from django import forms
from .models import ResearchDocument
from crispy_forms.helper import FormHelper

class ResearchDocumentForm(forms.ModelForm):
    class Meta:
        model = ResearchDocument
        fields = '__all__' # ['keywords', 'title']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        
        # Force HTML5 date input for DateField
        self.fields['publication_date'].widget = forms.DateInput(
            attrs={'type': 'date', 'class': 'form-control'}
        )