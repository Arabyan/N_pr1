from django import forms
from .models import DocFile

from django import forms
from .models import DocFile , DocEdited


class DocumentForm(forms.ModelForm):
    class Meta:
        model = DocFile
        fields = ('description', 'document')


class RawProductionForm(forms.Form):
    title_forms = forms.CharField(label='')


class VariablesForm(forms.Form):

    def __init__(self, *args, **kwargs):
        variables = kwargs.pop('variables')
        super().__init__(*args, **kwargs)

        for i, variable in enumerate(variables):
            self.fields['custom_%s' % i] = forms.CharField(label=variable)

    def get_input_text(self):
        for name, value in self.cleaned_data.items():
            if name.startswith('custom_'):
                yield (self.fields[name].label, value)


class EditedDocumentForm(forms.ModelForm):
    class Meta:
        model = DocEdited
        fields = ('edited_description','document_edited')