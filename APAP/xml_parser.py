from openpyxl import load_workbook
from django.shortcuts import get_object_or_404
from models.models import *

wb = load_workbook('timetable.xlsx', data_only=True)
sheet = wb['학과별강의목록']
#D 학수강좌번호
#E 교과목명
#I 강의요일/교시
## 대학교명

for row in sheet.rows:
	#for cell in row:
	# print(row[3].value)
	# print(row[4].value)
	# print(row[8].value)
	# print("=============")
	lecture = Lecture.objects.create(name=row[4].value, code=row[3].value, day_time=row[8].value, university=get_object_or_404(University, pk=1))
	lecture.save()
	print("data updated")

#### python manage.py shell < xml_parser.py