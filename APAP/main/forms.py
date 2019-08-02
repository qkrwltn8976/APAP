from django import forms
from models.models import Lecture, User, Print

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
            'cnt',
            'file'
        ]
        labels = {
            'color': "컬러/흑백",
            'side': "양면/단면",
            'gather': "다중인쇄",
            'direction': "페이지 방향",
            'order': "넘기는 방향",
            'price': "배송비",
            'cnt': "부수",
            'file': "인쇄 파일 업로드",            
        }

   