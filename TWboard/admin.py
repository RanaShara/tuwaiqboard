from django.contrib import admin


# Register your models here.

from .models import Program, Session, Assignment,Submission




@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'trainer', 'time', 'days', 'duration', 'status', 'type')
    list_filter = ('status', 'type')
    search_fields = ('name', 'trainer__username')  # استخدم username

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'trainer', 'time', 'day', 'duration', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'trainer__username')  # استخدم username

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'program', 'due_date', 'status')
    list_filter = ('status', 'program', 'due_date')
    search_fields = ('title', 'teacher__username', 'program__name')
    

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('assignment', 'student_name', 'submitted_at', 'grade')
    list_filter = ('assignment', 'submitted_at')
    search_fields = ('student_name', 'assignment__title')
