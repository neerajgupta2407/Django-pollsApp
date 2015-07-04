from django.contrib import admin
from .models import Choice, Question
# Register your models here.
#admin.site.register(Question)
admin.site.register(Choice)
class QuestionAdmin(admin.ModelAdmin):
	#fields = ['pub_date','question_text']
	
	fieldsets = [
			(None, {'fields' : ['question_text']}),
			('Date Information', {'fields': ['pub_date'], 'classes' : ['collapse']}),
			] 

admin.site.register(Question, QuestionAdmin)