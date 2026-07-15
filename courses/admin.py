from django.contrib import admin
from .models import Category, Teacher, Course, Lesson, ContactMessage, Student, Subscriber


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["name", "profession"]
    search_fields = ["name", "profession"]


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1
    ordering = ["order"]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "teacher", "price", "is_featured", "created_at"]
    list_filter = ["category", "is_featured"]
    search_fields = ["title", "short_description"]
    prepopulated_fields = {"slug": ("title",)}
    inlines = [LessonInline]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["title", "course", "order"]
    list_filter = ["course"]
    ordering = ["course", "order"]


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "subject", "is_read", "created_at"]
    list_filter = ["is_read"]
    search_fields = ["name", "email", "subject", "message"]
    readonly_fields = ["name", "email", "phone", "subject", "message", "created_at"]

    def has_add_permission(self, request):
        return False


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "course", "profession", "company", "rating", "is_top", "graduated_year"]
    list_filter = ["rating", "is_top", "graduated_year", "course"]
    search_fields = ["name", "profession", "company"]
    list_editable = ["is_top", "rating"]


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ["email", "created_at"]
    search_fields = ["email"]
