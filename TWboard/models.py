# models.py
from django.conf import settings
from django.db import models

class Program(models.Model):
    name = models.CharField(max_length=200)
    trainer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="programs")
    time = models.CharField(max_length=50)
    days = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    status = models.CharField(choices=[('active', 'جاري التنفيذ'), ('upcoming', 'قادم')], max_length=20)
    type = models.CharField(default='برنامج', max_length=50)
    def __str__(self):
        return self.name

class Session(models.Model):
    title = models.CharField(max_length=200)
    trainer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sessions")
    time = models.CharField(max_length=50)
    day = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    status = models.CharField(choices=[('active', 'جلسة مباشرة'), ('upcoming', 'جلسة قادمة')], max_length=20)

class Assignment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    program = models.ForeignKey("Program", on_delete=models.CASCADE, related_name="assignments", verbose_name="البرنامج")
    due_date = models.DateField()
    status = models.CharField(choices=[('pending','قريب'  ), ('late', 'متأخر')], max_length=20)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="assignments")
    def __str__(self):
        return self.name

class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name="submissions")
    student_name = models.CharField(max_length=100)
    comment = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='submissions/')
    grade = models.CharField(max_length=10, blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
