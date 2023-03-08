from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render , redirect
from django.urls import reverse
from schools.forms import Student_forms, School_forms

from .models import School, Student


def index(request):
    longer_school_list = School.objects.order_by('-name')                   #display the main menu of the app

    template = loader.get_template('schools/index.html')
    context = {'longer_school_list': longer_school_list,}
    return render(request, 'schools/index.html', context)

def detail(request, school_id):
    try:
        school = School.objects.get(pk=school_id)
    except School.DoesNotExist:
        raise Http404("that school does not exist")                         #display the list of students of the school
    return render(request, 'schools/detail.html', {'school': school})

def students(request, school_id):
    try:
        school = School.objects.get(pk=school_id)
    except School.DoesNotExist:
        raise Http404("that school does not exist")
    return render(request, 'schools/student.html', {'school': school})      #display the list of all students order buy school

def students_detail(request, id):
    try:
        stud = Student.objects.get(pk=id)
    except stud.DoesNotExist:                                               #display some students informations
        raise Http404("that school does not exist")
    return render(request, 'schools/detail_stud.html', {'student': stud})

def add_stud(request):
    if request.method == 'POST':                # if the request is POST -> this request is the return of the form
        form = Student_forms(request.POST)      # so we need to test the information
        if(form.is_valid()):                    # if the from is valid and if no other students is already named like that we can save our new student else we delete him
            student = form.save()
            for stu in Student.objects.all():
                if student.name == stu.name and student.id != stu.id: # here the id is tested to avoid finding the new student in the list
                    student.delete()
                    return render(request, 'schools/add_stud.html', {'form': form,'error':"there is already a student named like that"})
            school = School.objects.get(name=student.school)
            school.nb_students +=1;
            school.save()
            return redirect('../')
    else:
        form = Student_forms()

    return render(request, 'schools/add_stud.html', {'form': form})

def add_school(request):
    if request.method == 'POST':                # if the request is POST -> this request is the return of the form
        form = School_forms(request.POST)       # so we need to test the information
        if(form.is_valid()):                    # if the from is valid and if no other school is named like that we can save ous new sschool else we delete it
            school = form.save()
            for sch in School.objects.all():
                if school.name == sch.name and school.id!=sch.id:
                    school.delete()
                    return render(request, 'schools/add_school.html', {'form': form,'error':"there is already a school named like that"})
            return redirect('../')
    else:
        form = School_forms()

    return render(request, 'schools/add_school.html', {'form': form})

def rem_stud(request,id):
    student = Student.objects.get(pk=id)
    if request.method == 'POST':
        school = School.objects.get(name=student.school)
        school.nb_students -= 1;
        school.save()
        student.delete()                                           # if the request is a post type then delete the student
        return redirect('../../')
    return render(request,'schools/delete_stud.html',{'student':student})

def rem_school(request,school_id):
    school = School.objects.get(pk=school_id)
    if request.method == 'POST':                                # if the request is a post type then delete the school
        school.delete()
        return redirect('../')
    return render(request,'schools/delete_school.html',{'school':school})

def global_students(request):
    no_s = School.objects.get(name="No school")                 # display the students menu
    return render(request, 'schools/global_students.html',{'list_stud':Student.objects.all,'school_list':School.objects.all,'no_s':no_s})

def update_student(request,id):
    stud = Student.objects.get(pk=id)
    init_sch = stud.schoolinit_sch = stud.schoolinit_sch = stud.school
    if request.method == 'POST':
        form = Student_forms(request.POST,instance=stud)        #if th request is a POST type then update the profile
        if form.is_valid():                                     #else display the update's form
            form.save()
            new_sch = stud.school                              #update of schools stats
            init_sch.nb_students -=1;
            new_sch.nb_students += 1;
            init_sch.save()
            new_sch.save()
            return redirect('../',stud.id)
    else:
        form = Student_forms(instance=stud)
    return render(request, 'schools/update_stud.html',{'form':form,"student":stud})
