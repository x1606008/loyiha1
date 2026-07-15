from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Course, Category, Teacher, ContactMessage, Student, Subscriber


def index(request):
    courses = Course.objects.filter(is_featured=True)[:4]
    teachers = Teacher.objects.all()[:4]
    categories = Category.objects.all()
    top_students = Student.objects.filter(is_top=True)[:4]
    total_students = Student.objects.count()
    return render(request, "courses/index.html", {
        "courses": courses,
        "teachers": teachers,
        "categories": categories,
        "top_students": top_students,
        "total_students": total_students,
    })


def about(request):
    teachers = Teacher.objects.all()
    total_courses = Course.objects.count()
    total_teachers = Teacher.objects.count()
    total_categories = Category.objects.count()
    return render(request, "courses/about.html", {
        "teachers": teachers,
        "total_courses": total_courses,
        "total_teachers": total_teachers,
        "total_categories": total_categories,
    })


def course_list(request):
    courses = Course.objects.all()
    categories = Category.objects.all()
    category_slug = request.GET.get("category")
    if category_slug:
        courses = courses.filter(category__slug=category_slug)
    return render(request, "courses/course_list.html", {
        "courses": courses,
        "categories": categories,
        "active_category": category_slug,
    })


def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    related_courses = Course.objects.filter(category=course.category).exclude(id=course.id)[:3]
    return render(request, "courses/course_detail.html", {
        "course": course,
        "related_courses": related_courses,
    })


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        subject = request.POST.get("subject", "")
        message_text = request.POST.get("message", "")
        if name and email and subject and message_text:
            ContactMessage.objects.create(
                name=name, email=email, phone=phone,
                subject=subject, message=message_text,
            )
            messages.success(request, "Xabaringiz muvaffaqiyatli yuborildi!")
            return redirect("contact")
        else:
            messages.error(request, "Iltimos, barcha majburiy maydonlarni to'ldiring.")
    return render(request, "courses/contact.html")


def student_list(request):
    students = Student.objects.all()
    return render(request, "courses/student_list.html", {"students": students})


def subscribe(request):
    if request.method == "POST":
        email = request.POST.get("email", "")
        if email:
            _, created = Subscriber.objects.get_or_create(email=email)
            if created:
                messages.success(request, "Obuna muvaffaqiyatli amalga oshirildi!")
            else:
                messages.info(request, "Siz allaqachon obuna bo'lgansiz.")
    return redirect("index")
