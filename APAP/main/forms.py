from django import forms
from models.models import Lecture, User, Print

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


class Printform(forms.ModelForm):
    class Meta:
        model = Print
        fields = [
            'color',
            'side',
            'gather',
            'direction',
            'order',
            'price',
            'cnt'
        ]
        labels = {
            'color': "컬러/흑백",
            'side': "양면/단면",
            'gather': "다중인쇄",
            'direction': "페이지 방향",
            'order': "넘기는 방향",
            'price': "배송비",
            'cnt': "부수"            
        }

   