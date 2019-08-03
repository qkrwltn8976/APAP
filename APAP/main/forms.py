from django import forms
from models.models import Lecture, User, Print
from bootstrap_datepicker_plus import DateTimePickerInput

class Printform(forms.ModelForm):
    class Meta:
        model = Print
        fields = [
        	'lecture',
            'color',
            'side',
            'gather',
            'direction',
            'price',
            'cnt',
            'date',
            'file'
        ]
        labels = {
        	'lecture' : "강의",
            'color': "색상",
            'side': "양면 인쇄",
            'gather': "용지당 페이지 수",
            'direction': "페이지 방향",
            'price': "배송비",
            'cnt': "매수",
            'date': "종료일시",
            'file': "인쇄 파일 업로드",            
        }
        date = forms.DateTimeField(
        	widget=DateTimePickerInput(format='%m/%d/%Y %H:%M:%S')
        )

   