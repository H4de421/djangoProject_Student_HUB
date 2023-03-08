from django.urls import path

from . import views

app_name = 'Schools'
urlpatterns = [

    # ex: /schools/
    path('', views.index, name='index'),

    #path for the seee of all students
    # ex : schools/students/
    path('students/',views.global_students, name='global_students'),

    #path to add students
    # ex: /schools/students/add/
    path('students/add/',views.add_stud, name='add_stud'),

    # path to see students profile
    # ex: /schools/students/1/
    path('students/<int:id>/',views.students_detail, name='add_stud'),

    # path to delete students profile
    # ex: /schools/students/1/delete/
    path('students/<int:id>/delete/',views.rem_stud, name='rem_stud'),

    # path to update the student
    # ex: /schools/students/1/update/
    path('students/<int:id>/update/',views.update_student,name='upd_stud'),


    # path to add school
    # ex: /schools/add/
    path('add/',views.add_school, name='add_school'),

    # path to see information of a specific school
    # ex: /schools/5/
    path('<int:school_id>/', views.detail, name='detail'),

    # path to see delete a school
    # ex: /schools/5/delete
    path('<int:school_id>/delete', views.rem_school, name='delete'),

    # path to see school's students
    # ex: /schools/5/students/
    path('<int:school_id>/students/', views.students, name='students'),




]