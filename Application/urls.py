from django.urls import path, include
from . import views
app_name = 'Application'

urlpatterns = [
    # path('', views.IndexView),
    path('', views.allViews, name = 'all-views'),
    path('department/add/', views.DepartmentCreateView.as_view(), name = 'department-add'),
    path('department/<str:pk>/', views.DepartmentDetailView.as_view(), name = 'department-detail'),
    path('department/', views.DepartmentAllView, name = 'department'),
    path('student/add/', views.StudentCreateView.as_view(), name = 'student-add'),
    path('student/<str:pk>/', views.StudentDetailView.as_view(), name = 'student-detail'),
    path('student/',views.StudentAllView, name = 'student'),
    path('instructor/add/', views.InstructorCreateView.as_view(), name = 'instructor-add'),
    path('instructor/<str:pk>/', views.InstructorDetailView.as_view(), name = 'instructor-detail'),
    path('instructor/',views.InstructorAllView, name = 'instructor'),
    path('advisor/add/', views.AdvisorCreateView.as_view(), name='advisor-add'),
    path('advisor/<str:pk>/', views.AdvisorDetailView.as_view(), name='advisor-detail'),
    path('advisor/', views.AdvisorAllView, name='advisor'),
    path('course/add/', views.CourseCreateView.as_view(), name='course-add'),
    path('course/<str:pk>/', views.CourseDetailView.as_view(), name='course-detail'),
    path('course/', views.CourseAllView, name='course'),
    path('section/add/', views.SectionCreateView.as_view(), name='section-add'),
    path('section/<str:pk>/', views.SectionDetailView.as_view(), name='section-detail'),
    path('section/', views.SectionAllView, name='section'),
]