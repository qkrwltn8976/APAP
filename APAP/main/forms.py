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
            'price'

        ]
        labels = {
            'color': "컬러/흑백",
            'side': "양면/단면",
            'gather': "다중인쇄",
            'direction': "페이지 방향",
            'price': "배송비"
        }

   