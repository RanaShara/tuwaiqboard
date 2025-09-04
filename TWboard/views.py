from django.shortcuts import render, get_object_or_404, redirect
from .models import Program, Session, Assignment, Submission
from .forms import AssignmentForm, SubmissionForm,GradeForm
from django.contrib.auth.decorators import login_required

def index(request):
    programs = Program.objects.all()
    sessions = Session.objects.all()
    assignments = Assignment.objects.all()[:3]  # آخر 3 واجبات
    return render(request, 'index.html', {
        'programs': programs,
        'sessions': sessions,
        'assignments': assignments
    })

# قائمة الواجبات
def assignments(request):
    assignments = Assignment.objects.all()
    return render(request, 'assignment_detail.html', {'assignments': assignments})

# تفاصيل الواجب + الحلول
def assignment_detail(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    submissions = assignment.submissions.all()
    return render(request, 'assignment_detail.html', {
        'assignment': assignment,
        'submissions': submissions
    })

# تقديم واجب
def submit_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    if request.method == "POST":
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.assignment = assignment
            submission.save()
            return redirect('assignment_detail', assignment_id=assignment.id)
    else:
        form = SubmissionForm()
    return render(request, 'submit_assignment.html', {'assignment': assignment, 'form': form})

# إضافة واجب بدون تسجيل دخول
def add_assignment(request):
    if request.method == "POST":
        form = AssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.teacher = form.cleaned_data['teacher_name']
            assignment.save()
            return redirect('assignments')
    else:
        form = AssignmentForm()
    return render(request, 'add_assignment.html', {'form': form})

@login_required
def teacher_dashboard(request):
    programs = request.user.programs.all()
    sessions = request.user.sessions.all()
    assignments = request.user.assignments.all()
    return render(request, "teacher/dashboard.html", {
        "programs": programs,
        "sessions": sessions,
        "assignments": assignments,
    })



# إضافة واجب
@login_required
def add_assignment(request):
    if request.method == "POST":
        form = AssignmentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.teacher = request.user
            obj.save()
            return redirect("teacher_dashboard")
    else:
        form = AssignmentForm()
    return render(request, "teacher/add_assignment.html", {"form": form})

def view_submissions(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    submissions = assignment.submissions.all()
    return render(request, 'teacher/view_submissions.html', {
        'assignment': assignment,
        'submissions': submissions
    })


@login_required
def grade_submission(request, submission_id):
    submission = get_object_or_404(Submission, id=submission_id, assignment__teacher=request.user)
    if request.method == "POST":
        form = GradeForm(request.POST, instance=submission)
        if form.is_valid():
            form.save()
            return redirect("view_submissions", assignment_id=submission.assignment.id)
    else:
        form = GradeForm(instance=submission)
    return render(request, "teacher/grade_submission.html", {
        "submission": submission,
        "form": form,
    })
def aboutTuwiq(request):
      return render(request, 'aboutTuwaiqEdu.html')
def aboutme(request):
      return render(request, 'aboutme.html')

