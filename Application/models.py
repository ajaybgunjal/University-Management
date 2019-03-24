from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime
from django.shortcuts import render
from django.urls import reverse
from django.conf.urls import include, url
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.validators import MaxValueValidator, MinValueValidator


class Department(models.Model):
    dept_name = models.CharField(max_length=200, primary_key=True)
    building = models.CharField(max_length=200)
    budget = models.CharField(max_length=200)
    def get(self):
        return self.clean()
    def get_absolute_url(self):
        return reverse('Application:department-detail', kwargs={'pk': self.pk})
    def __str__(self):
        return self.dept_name
    def get_fields(self):
        # for name, value in [(field.name, field.value_to_string(self) for field in Department._meta.fields]:
        #     print(name)
        return [(field.name, field.value_to_string(self)) for field in Department._meta.fields]



class Student(models.Model):
    ID = models.CharField(max_length=200, primary_key=True, verbose_name="Roll Number")
    firstName = models.CharField(max_length=200, verbose_name="First Name")
    lastName = models.CharField(max_length=200, verbose_name="Last Name")
    dept_name = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="Department Name")
    tot_cred = models.IntegerField(verbose_name="Total Credits",
    validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])
    stud_img = models.ImageField(upload_to='media/', verbose_name="Image")
    def get(self):
        return self.clean()
    def get_absolute_url(self):
        return reverse('Application:student-detail', kwargs={'pk': self.pk})
    def __str__(self):
        return self.ID
    # def get_field_names(request):
    #     return [(field.verbose_name) for field in Student._meta.fields]
    def get_fields(self):
        # for name, value in [(field.name, field.value_to_string(self) for field in Department._meta.fields]:
        #     print(name)
        return [(field.verbose_name, field.value_to_string(self)) for field in Student._meta.fields]


class Instructor(models.Model):
    ID = models.CharField(max_length=200, primary_key=True)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    dept_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.FloatField()
    def get(self):
        return self.clean()
    def get_absolute_url(self):
        return reverse('Application:instructor-detail', kwargs={'pk': self.pk})
    def __str__(self):
         return self.firstName + " " + self.lastName


class Advisor(models.Model):
    s_id = models.ForeignKey(Student, on_delete=models.CASCADE, unique=True, default='10')
    i_id = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    def get_absolute_url(self):
        return reverse('Application:advisor-detail', kwargs={'pk': self.pk})
    def get(self):
        return self.clean()
    # def __str__(self):
        # returm str(self.s_id) + " : "  + str(self.i_id);

class Course(models.Model):
    course_id = models.CharField(unique=True, max_length=200)
    title = models.CharField(max_length=200)
    dept_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    credits = models.IntegerField()
    def get(self):
        return self.clean()
    def get_absolute_url(self):
        return reverse('Application:course-detail', kwargs={'pk': self.pk})
    def __str__(self):
        return self.course_id + " : " + self.title

# class Prereq(models.Model):
#     num = models.IntegerField(default=10)
#     course_id = models.ForeignKey(Course, on_delete=models.CASCADE, default='0')
#     # prereq_id = models.ForeignKey(Course, on_delete=models.CASCADE, default='1')

class Section(models.Model):
    def yearValidator(self):
        if (not(int(self.year) >= 2000 and int(self.year) <= int(datetime.datetime.now().year))):
            raise ValidationError(
                ('%(value) is not an valid year'),
                params={'value': self.year}
            )

    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    sec_id = models.CharField(max_length=200)
    semester = models.IntegerField()
    year = models.IntegerField(validators=[yearValidator], default=2016)
    def get(self):
        return self.clean()
    def get_absolute_url(self):
        return reverse('Application:section-detail', kwargs={'pk': self.pk})
    def __str__(self):
        return self.sec_id

    class Meta:
        unique_together = (('course_id', 'sec_id', 'semester', 'year'),)
