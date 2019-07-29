from django import forms
from models.models import Lecture, User

class LectureForm(forms.ModelForm):
    lecture = forms.ModelMultipleChoiceField(queryset=Lecture.objects.none())

    class Meta:
        model = Lecture
        fields = ('name','code',)
        widgets = {
            'name': Select2MultipleWidget()
        }

    def __init__(self, all_lectures, *args, **kwargs):
        super(LectureForm, self).__init__(*args, **kwargs)
        self.fields['lecture'].queryset = all_lectures