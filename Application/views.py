from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import CreateView, View, DetailView, TemplateView
from .models import Department, Student, Instructor, Advisor, Course, Section
from django import forms
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin


class DepartmentCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = 'Application.add_department'
    model = Department
    fields = ('dept_name', 'building', 'budget')
    next = 'Application:department-create'


class DepartmentDetailView(LoginRequiredMixin, DetailView):
    model = Department
    next = "Application:department-detail"


class StudentCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Student
    fields = ('ID', 'firstName', 'lastName', 'dept_name', 'tot_cred', 'stud_img')
    next = "Application:student-create"
    permission_required = 'Application.add_student'


class StudentDetailView(DetailView):
    model = Student


def allViews(request):
    return render(request, 'Application/all-views.html')


class InstructorCreateView(CreateView):
    model = Instructor
    fields = ('ID', 'firstName', 'lastName', 'dept_name', 'salary')


class InstructorDetailView(DetailView):
    model = Instructor


class AdvisorCreateView(CreateView):
    model = Advisor
    fields = ('s_id', 'i_id')


class AdvisorDetailView(DetailView):
    model = Advisor


class CourseCreateView(CreateView):
    model = Course
    fields = ('course_id', 'title', 'dept_name', 'credits')
    

class CourseDetailView(DetailView):
    model = Course


class SectionCreateView(CreateView):
    model = Section
    fields = ('course_id', 'sec_id', 'semester', 'year')


class SectionDetailView(DetailView):
    model = Section

def StudentAllView(request):
    students = Student.objects.all()
    return render(request, 'Application/student_all_view.html', {'students': students})

def AdvisorAllView(request):
    advisors = Advisor.objects.all()
    return render(request, 'Application/advisor_all_view.html', {'advisors': advisors})


def CourseAllView(request):
    courses = Course.objects.all()
    return render(request, 'Application/course_all_view.html', {'courses': courses})


def DepartmentAllView(request):
    departments = Department.objects.all()
    return render(request, 'Application/department_all_view.html', {'departments': departments})


def InstructorAllView(request):
    instructors = Instructor.objects.all()
    return render(request, 'Application/instructor_all_view.html', {'instructors': instructors})


def SectionAllView(request):
    sections = Section.objects.all()
    return render(request, 'Application/section_all_view.html', {'sections': sections})
