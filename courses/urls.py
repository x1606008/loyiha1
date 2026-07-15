from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("biz-haqimizda/", views.about, name="about"),
    path("kurslar/", views.course_list, name="course_list"),
    path("kurs/<slug:slug>/", views.course_detail, name="course_detail"),
    path("aloqa/", views.contact, name="contact"),
    path("oquvchilar/", views.student_list, name="student_list"),
    path("obuna/", views.subscribe, name="subscribe"),
]
