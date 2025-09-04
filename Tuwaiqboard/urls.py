"""
URL configuration for Tuwaiqboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from TWboard import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('assignments/',views.assignments,name='assignments'),
    path('assignments/<int:assignment_id>/', views.assignment_detail, name='assignment_detail'),
    path('teacher/', views.teacher_dashboard, name='teacher_dashboard'),
    path('teacher/add/', views.add_assignment, name='add_assignment'),
    path('teacher/<int:assignment_id>/submissions/', views.view_submissions, name='view_submissions'),
    path('teacher/submission/<int:submission_id>/grade/', views.grade_submission, name='grade_submission'),
    path('assignments/<int:assignment_id>/submit/', views.submit_assignment, name='submit_assignment'),
    path("login/", auth_views.LoginView.as_view(template_name="auth/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path('aboutUs/',views.aboutTuwiq,name='aboutUs'),
    path('aboutMe/',views.aboutme,name='aboutMe'),
]
