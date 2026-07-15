from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Kategoriya nomi")
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, verbose_name="Tavsif")

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=200, verbose_name="To'liq ismi")
    profession = models.CharField(max_length=200, verbose_name="Kasbi")
    bio = models.TextField(blank=True, verbose_name="Bio")
    photo = models.ImageField(upload_to="teachers/", blank=True, verbose_name="Rasm")
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    instagram = models.URLField(blank=True)

    class Meta:
        verbose_name = "O'qituvchi"
        verbose_name_plural = "O'qituvchilar"

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=300, verbose_name="Kurs nomi")
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="courses", verbose_name="Kategoriya"
    )
    teacher = models.ForeignKey(
        Teacher, on_delete=models.SET_NULL, null=True, blank=True, related_name="courses", verbose_name="O'qituvchi"
    )
    short_description = models.TextField(verbose_name="Qisqa tavsif")
    full_description = models.TextField(blank=True, verbose_name="To'liq tavsif")
    image = models.ImageField(upload_to="courses/", blank=True, verbose_name="Rasm")
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0, verbose_name="Narxi (so'm)")
    duration = models.CharField(max_length=100, blank=True, verbose_name="Davomiyligi")
    lessons_count = models.PositiveIntegerField(default=0, verbose_name="Darslar soni")
    is_featured = models.BooleanField(default=False, verbose_name="Tavsiya etilgan")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="lessons", verbose_name="Kurs"
    )
    title = models.CharField(max_length=300, verbose_name="Dars nomi")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")
    content = models.TextField(blank=True, verbose_name="Dars matni")
    video_url = models.URLField(blank=True, verbose_name="Video havolasi")

    class Meta:
        verbose_name = "Dars"
        verbose_name_plural = "Darslar"
        ordering = ["order"]

    def __str__(self):
        return f"{self.course.title} - {self.title}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=200, verbose_name="Ism")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Telefon")
    subject = models.CharField(max_length=300, verbose_name="Mavzu")
    message = models.TextField(verbose_name="Xabar")
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False, verbose_name="O'qilgan")

    class Meta:
        verbose_name = "Xabar"
        verbose_name_plural = "Xabarlar"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.subject}"


class Student(models.Model):
    RATING_CHOICES = [
        (1, "1 - Oltin"),
        (2, "2 - Kumush"),
        (3, "3 - Bronza"),
    ]
    name = models.CharField(max_length=200, verbose_name="To'liq ismi")
    course = models.ForeignKey(
        Course, on_delete=models.SET_NULL, null=True, blank=True, related_name="students", verbose_name="Bitirgan kurs"
    )
    photo = models.ImageField(upload_to="students/", blank=True, verbose_name="Rasm")
    profession = models.CharField(max_length=200, verbose_name="Hozirgi kasbi")
    company = models.CharField(max_length=200, blank=True, verbose_name="Ish joyi")
    quote = models.TextField(blank=True, verbose_name="O'z so'zi")
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, default=3, verbose_name="Reyting")
    is_top = models.BooleanField(default=False, verbose_name="Top o'quvchi")
    graduated_year = models.PositiveIntegerField(default=2025, verbose_name="Bitirgan yili")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "O'quvchi"
        verbose_name_plural = "O'quvchilar"
        ordering = ["rating", "-graduated_year"]

    def __str__(self):
        return self.name

    @property
    def rating_label(self):
        return dict(self.RATING_CHOICES).get(self.rating, "")


class Subscriber(models.Model):
    email = models.EmailField(unique=True, verbose_name="Email")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Obunachi"
        verbose_name_plural = "Obunachilar"

    def __str__(self):
        return self.email
