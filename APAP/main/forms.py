from django import forms
from models.models import Schedule, User, Print
from bootstrap_datepicker_plus import DateTimePickerInput
from django.shortcuts import get_object_or_404
from django.forms import ModelMultipleChoiceField


class MyModelMultipleChoiceField(ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return "{}".format(obj.lecture.name)


class Printform(forms.ModelForm):	
	def __init__(self, user, *args, **kwargs):
		super (Printform,self ).__init__(*args,**kwargs) # populates the post
		self.fields['schedule'].queryset = Schedule.objects.filter(user=user).distinct()
	class Meta:
		model = Print
		fields = {
			'schedule',
			'color',
			'side',
			'gather',
			'direction',
			'delivery_price',
			
			'date',
			'file',
		}
		labels = {
			'schedule' : "강의",
			'color': "색상",
			'side': "양면 인쇄",
			'gather': "용지당 페이지 수",
			'direction': "페이지 방향",
			'delivery_price': "배송비",
			'date': "종료일시",
			'file': "인쇄 파일 업로드",            
        }
		widgets = {
			'date' : DateTimePickerInput(format='%m/%d/%Y %H:%M:%S'),

		}

	
        # date = forms.DateTimeField(
        # 	widget=DateTimePickerInput(format='%m/%d/%Y %H:%M:%S')
        # )

   