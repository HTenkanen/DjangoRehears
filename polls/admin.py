from django.contrib import admin
from polls.models import Question, Choice

# Register your models here.

# Method to add many choices directly
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 5

#Modify the Question's admin page appearing
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,      {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),   # New order and split the form and collapse the date info
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']

# Register also Question admin
admin.site.register(Question, QuestionAdmin)

