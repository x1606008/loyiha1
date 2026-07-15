from django.core.management.base import BaseCommand
from courses.models import Category, Teacher, Course, Lesson, Student


class Command(BaseCommand):
    help = "Boshlang'ich o'zbekcha kontentni yuklaydi"

    def handle(self, *args, **options):
        self.stdout.write("Kontent yuklanmoqda...")

        categories_data = [
            {"name": "Dasturlash", "slug": "dasturlash", "description": "Dasturlash tillari bo'yicha kurslar"},
            {"name": "Veb-dasturlash", "slug": "veb-dasturlash", "description": "Frontend va Backend dasturlash"},
            {"name": "Mobil ilovalar", "slug": "mobil-ivoalar", "description": "Mobil ilovalar yaratish kurslari"},
            {"name": "Sun'iy intellekt", "slug": "suniy-intellekt", "description": "AI va Machine Learning kurslari"},
            {"name": "Dizayn", "slug": "dizayn", "description": "Grafik va UI/UX dizayn kurslari"},
            {"name": "Ma'lumotlar bazasi", "slug": "malumotlar-bazasi", "description": "DB management kurslari"},
        ]

        categories = {}
        for cd in categories_data:
            cat, _ = Category.objects.get_or_create(slug=cd["slug"], defaults=cd)
            categories[cd["slug"]] = cat
            self.stdout.write(f"  Kategoriya: {cat.name}")

        teachers_data = [
            {
                "name": "Abdulloh Karimov",
                "profession": "Senior Python Developer",
                "bio": "10 yillik tajribaga ega Python dasturchi. Django, FastAPI va Data Science sohasida mutaxassis.",
            },
            {
                "name": "Nodira Abdullayeva",
                "profession": "Frontend Developer",
                "bio": "React, Vue.js va AngularFrameworklarida tajribali frontend dasturchi.",
            },
            {
                "name": "Sardor Raximov",
                "profession": "Mobile Developer",
                "bio": "Flutter va React Native bo'yicha tajribali mobil dasturchi. 20+ ilovani ishlab chiqqan.",
            },
            {
                "name": "Malika Toshmatova",
                "profession": "AI/ML Engineer",
                "bio": "Sun'iy intellekt va machine learning sohasida 7 yillik tajribaga ega muhandis.",
            },
        ]

        teachers = {}
        for td in teachers_data:
            t, _ = Teacher.objects.get_or_create(name=td["name"], defaults=td)
            teachers[td["name"]] = t
            self.stdout.write(f"  O'qituvchi: {t.name}")

        courses_data = [
            {
                "title": "Python Dasturlash asoslari",
                "slug": "python-dasturlash",
                "category": "dasturlash",
                "teacher": "Abdulloh Karimov",
                "short_description": "Python dasturlash tilini noldan o'rganing. OOP, Ma'lumotlar tuzilmalari va amaliy loyihalar.",
                "full_description": "Python - bugungi kunda eng mashhur va talab qilinadigan dasturlash tillaridan biri. Uning oddiy sintaksisi va kuchli kutubxonalari uni ham yangi boshlanuvchilar, ham tajribali dasturchilar uchun ideal qiladi.\n\nBu kursda siz quyidagilarni o'rganasiz:\n- Python o'rnatish va muhitni sozlash\n- O'zgaruvchilar, turlar va operatorlar\n- Shartli operatorlar va tsikllar\n- Funksiyalar va modullar\n- OOP (Ob'ektga yo'naltirilgan dasturlash)\n- Ma'lumotlar tuzilmalari (list, dict, set, tuple)\n- Fayllar bilan ishlash\n- Xatolarni boshqarish (exception handling)\n- Amaliy loyiha: Kalkulyator yaratish",
                "price": 350000,
                "duration": "2 oy",
                "lessons_count": 16,
                "is_featured": True,
            },
            {
                "title": "React.js Frontend Dasturlash",
                "slug": "reactjs-frontend",
                "category": "veb-dasturlash",
                "teacher": "Nodira Abdullayeva",
                "short_description": "React.js frameworki yordamida zamonaviy veb-ilovalar yarating. Hooks, Redux va komponentlar arxitekturasi.",
                "full_description": "React.js - Facebook tomonidan yaratilgan va dunyodagi eng mashhur frontend frameworklaridan biri. Bu kursda siz React ning asosiy tushunchalaridan Professional darajagacha o'rganasiz.\n\nKurs dasturi:\n- HTML, CSS, JavaScript asoslari\n- React o'rnatish va JSX\n- Komponentlar va props\n- State va Lifecycle\n- Hooks (useState, useEffect, useContext)\n- Redux va Redux Toolkit\n- React Router v6\n- API bilan ishlash\n- Tailwind CSS bilan stilizatsiya\n- Amaliy loyiha: To'liq e-commerce sayti",
                "price": 500000,
                "duration": "3 oy",
                "lessons_count": 24,
                "is_featured": True,
            },
            {
                "title": "Flutter bilan Mobil Ilova Yaratish",
                "slug": "flutter-mobil",
                "category": "mobil-ivoalar",
                "teacher": "Sardor Raximov",
                "short_description": "Flutter frameworki yordamida iOS va Android uchun bir vaqtda ilova yarating. Dart tili va UI dizayn.",
                "full_description": "Flutter - Google tomonidan yaratilgan ochiq manba framework bo'lib, u yordamida bitta kod asosi bilan iOS va Android uchun ilovalar yaratish mumkin.\n\nBu kursda siz o'rganasiz:\n- Dart tili asoslari\n- Flutter o'rnatish va muhitni sozlash\n- Widgetlar tizimi\n- Layout va dizayn\n- State Management (Provider, BLoC)\n- Navigatsiya va marshrutlash\n- Ma'lumotlar saqlash\n- Firebase integratsiyasi\n- REST API bilan ishlash\n- App Store va Play Store ga joylashtirish",
                "price": 600000,
                "duration": "3 oy",
                "lessons_count": 20,
                "is_featured": True,
            },
            {
                "title": "Sun'iy Intellekt va Machine Learning",
                "slug": "ai-machine-learning",
                "category": "suniy-intellekt",
                "teacher": "Malika Toshmatova",
                "short_description": "AI va ML asoslari, Python kutubxonalari (TensorFlow, PyTorch) va amaliy loyihalar.",
                "full_description": "Sun'iy intellekt (AI) va uning tarmog'i bo'lgan Machine Learning (ML) bugungi kunda eng tez rivojlanayotgan sohalardan biri.\n\nKurs dasturi:\n- AI va ML asoslari\n- Python va Matematik asoslar\n- NumPy va Pandas\n- Matplotlib va Seaborn vizualizatsiya\n- Supervised Learning (Linear Regression, Decision Trees, Random Forest)\n- Unsupervised Learning (K-Means, PCA)\n- Neural Networks asoslari\n- TensorFlow va PyTorch\n- NLP (Tabiiy tilni qayta ishlash)\n- Amaliy loyiha: Tasvirlarni aniqlash tizimi",
                "price": 700000,
                "duration": "4 oy",
                "lessons_count": 28,
                "is_featured": True,
            },
            {
                "title": "Web Dizayn va UI/UX",
                "slug": "web-dizayn",
                "category": "dizayn",
                "teacher": "Nodira Abdullayeva",
                "short_description": "Zamonaviy veb-dizayn tamoyillari, Figma va Adobe XD bilan amaliy loyihalar.",
                "full_description": "Yaxshi veb-dizayn - muvaffaqiyatli veb-saytning asosidir. Bu kursda siz professional veb-dizayner bo'lish uchun kerakli bilimlarni olasiz.\n\nKurs dasturi:\n- Dizayn tamoyillari va rang nazariyasi\n- Tipografiya asoslari\n- Figma dasturi bilan ishlash\n- Adobe XD bilan prototiplash\n- UI/UX dizayn metodologiyasi\n- Responsive dizayn\n- Design Systems yaratish\n- User Research usullari\n- Amaliy loyiha: To'liq veb-sayt dizayni",
                "price": 400000,
                "duration": "2 oy",
                "lessons_count": 14,
                "is_featured": True,
            },
            {
                "title": "PostgreSQL va Ma'lumotlar Bazasi",
                "slug": "postgresql-malumotlar",
                "category": "malumotlar-bazasi",
                "teacher": "Abdulloh Karimov",
                "short_description": "Ma'lumotlar bazasi tushunchalari, SQL, PostgreSQL va database design amaliyoti.",
                "full_description": "Ma'lumotlar bazasi har qanday veb-ilovaning asosiy qismidir. Bu kursda siz professional database administrator yoki backend dasturchi bo'lish uchun zarur bilimlarni olasiz.\n\nKurs dasturi:\n- Ma'lumotlar bazasi asoslari\n- SQL tili (DDL, DML, DQL)\n- PostgreSQL o'rnatish va sozlash\n- Jadvaklar, indekslar va bog'lanishlar\n- Normalizatsiya\n- Stored Procedures va Functions\n- Triggerlar va Events\n- Backup va Recovery\n- Performance tuning\n- Amaliy loyiha: E-commerce DB yaratish",
                "price": 300000,
                "duration": "2 oy",
                "lessons_count": 12,
                "is_featured": False,
            },
        ]

        for cd in courses_data:
            course, created = Course.objects.get_or_create(
                slug=cd["slug"],
                defaults={
                    "title": cd["title"],
                    "category": categories[cd["category"]],
                    "teacher": teachers[cd["teacher"]],
                    "short_description": cd["short_description"],
                    "full_description": cd["full_description"],
                    "price": cd["price"],
                    "duration": cd["duration"],
                    "lessons_count": cd["lessons_count"],
                    "is_featured": cd["is_featured"],
                },
            )
            if created:
                self.stdout.write(f"  Kurs: {course.title}")

                lessons_data = {
                    "python-dasturlash": [
                        "Kirish va muhitni sozlash",
                        "O'zgaruvchilar va turlar",
                        "Operatorlar",
                        "Shartli operatorlar",
                        "Tsikllar",
                        "Funksiyalar",
                        "List va Tuple",
                        "Dictionary va Set",
                        "OOP asoslari",
                        "Klasslar va ob'ektlar",
                        "Inheritance va Polymorphism",
                        "Xatolarni boshqarish",
                        "Fayllar bilan ishlash",
                        "Modullar va paketlar",
                        "Amaliy loyiha: Kalkulyator",
                        "Kurs yakuniy loyihasi",
                    ],
                    "reactjs-frontend": [
                        "HTML/CSS/JS yangilanishi",
                        "React o'rnatish va JSX",
                        "Komponentlar yaratish",
                        "Props va State",
                        "Lifecycle metodlari",
                        "Hooks: useState",
                        "Hooks: useEffect",
                        "Hooks: useContext",
                        "Redux asoslari",
                        "Redux Toolkit",
                        "React Router v6",
                        "API bilan ishlash",
                        "Form handling",
                        "Tailwind CSS",
                        "Responsive dizayn",
                        "Performance optimization",
                        "Testing",
                        "Deployment",
                        "Loyiha: E-commerce - 1-qism",
                        "Loyiha: E-commerce - 2-qism",
                        "Loyiha: E-commerce - 3-qism",
                        "Loyiha: E-commerce - 4-qism",
                        "Loyiha: E-commerce - 5-qism",
                        "Kurs yakuniy loyihasi",
                    ],
                    "flutter-mobil": [
                        "Dart tili asoslari",
                        "Flutter o'rnatish",
                        "Widgetlar tizimi",
                        "Matn va tugmalar",
                        "Layout: Row, Column, Stack",
                        "ListView va GridView",
                        "Navigatsiya",
                        "State Management: Provider",
                        "BLoC pattern",
                        "Formlar va validatsiya",
                        "Ma'lumotlar saqlash",
                        "HTTP va API",
                        "Firebase Auth",
                        "Firestore Database",
                        "Push Notifications",
                        "Rasm va kamera",
                        "Maps integratsiyasi",
                        "App Publishing",
                        "Loyiha: To'liq ilova - 1",
                        "Loyiha: To'liq ilova - 2",
                    ],
                    "ai-machine-learning": [
                        "AI va ML kirish",
                        "Python asoslari",
                        "NumPy bilan ishlash",
                        "Pandas bilan ishlash",
                        "Vizualizatsiya: Matplotlib",
                        "Linear Regression",
                        "Logistic Regression",
                        "Decision Trees",
                        "Random Forest",
                        "K-Means Clustering",
                        "PCA",
                        "Neural Networks asoslari",
                        "TensorFlow kirish",
                        "CNN asoslari",
                        "RNN asoslari",
                        "NLP kirish",
                        "Transfer Learning",
                        "Model deployment",
                        "Loyiha: Tasvir aniqlash - 1",
                        "Loyiha: Tasvir aniqlash - 2",
                        "Loyiha: Matn tahlili - 1",
                        "Loyiha: Matn tahlili - 2",
                        "Kurs yakuniy loyihasi - 1",
                        "Kurs yakuniy loyihasi - 2",
                        "Kurs yakuniy loyihasi - 3",
                        "Kurs yakuniy loyihasi - 4",
                        "Kurs yakuniy loyihasi - 5",
                    ],
                    "web-dizayn": [
                        "Dizayn asoslari",
                        "Rang nazariyasi",
                        "Tipografiya",
                        "Kompozitsiya",
                        "Figma: Kirish",
                        "Figma: Komponentlar",
                        "Figma: Prototiplash",
                        "Adobe XD kirish",
                        "UI dizayn tamoyillari",
                        "UX research",
                        "Responsive dizayn",
                        "Design System",
                        "Loyiha: Landing page",
                        "Kurs yakuniy loyihasi",
                    ],
                    "postgresql-malumotlar": [
                        "DB asoslari",
                        "SQL: DDL",
                        "SQL: DML",
                        "SQL: DQL",
                        "PostgreSQL o'rnatish",
                        "Jadvaklar yaratish",
                        "Bog'lanishlar (JOIN)",
                        "Indekslar",
                        "Normalizatsiya",
                        "Stored Procedures",
                        "Triggerlar",
                        "Kurs yakuniy loyihasi",
                    ],
                }

                course_lessons = lessons_data.get(cd["slug"], [])
                for i, lesson_title in enumerate(course_lessons, 1):
                    Lesson.objects.get_or_create(
                        course=course,
                        title=lesson_title,
                        defaults={"order": i},
                    )

        students_data = [
            {
                "name": "Jasur Toshmatov",
                "profession": "Senior Python Developer",
                "company": "epam.uz",
                "quote": "IT Online mening hayotimni o'zgartirdi. Endi men sevimli kasbim bilan shug'ullanaman!",
                "rating": 1,
                "is_top": True,
                "graduated_year": 2024,
                "course_slug": "python-dasturlash",
            },
            {
                "name": "Nilufar Karimova",
                "profession": "React Frontend Developer",
                "company": "IT Park",
                "quote": "Darslar juda sifatli va amaliyotga yo'naltirilgan. Tavsiya qilaman!",
                "rating": 1,
                "is_top": True,
                "graduated_year": 2024,
                "course_slug": "reactjs-frontend",
            },
            {
                "name": "Sardor Aliyev",
                "profession": "Flutter Developer",
                "company": "TexnoLider",
                "quote": "Mobil dasturlashni noldan o'rganib, 3 oyda ish topdim.",
                "rating": 2,
                "is_top": True,
                "graduated_year": 2025,
                "course_slug": "flutter-mobil",
            },
            {
                "name": "Malika Normatova",
                "profession": "Data Scientist",
                "company": "UzCard",
                "quote": "AI kursi menga yangi karyera eshiklarini ochdi. Juda minnatdorman!",
                "rating": 2,
                "is_top": True,
                "graduated_year": 2025,
                "course_slug": "ai-machine-learning",
            },
            {
                "name": "Otabek Raximov",
                "profession": "Full-Stack Developer",
                "company": "Freelance",
                "quote": "Python asoslaridan boshlab, to'liq full-stack dasturchi bo'ldim.",
                "rating": 3,
                "is_top": False,
                "graduated_year": 2025,
                "course_slug": "python-dasturlash",
            },
            {
                "name": "Gulnora Eshmatova",
                "profession": "UI/UX Dizayner",
                "company": "Creative Studio",
                "quote": "Dizayn kursi orqali o'z brendimni yaratdim.",
                "rating": 3,
                "is_top": False,
                "graduated_year": 2025,
                "course_slug": "web-dizayn",
            },
            {
                "name": "Dilshod Karimov",
                "profession": "Backend Developer",
                "company": "NAPA Automotive",
                "quote": "PostgreSQL kursi juda foydali bo'ldi. Endi ma'lumotlar bazasi bilan erkin ishlayman.",
                "rating": 3,
                "is_top": False,
                "graduated_year": 2024,
                "course_slug": "postgresql-malumotlar",
            },
            {
                "name": "Mohira Toshpulatova",
                "profession": "React Developer",
                "company": "Boost Valley",
                "quote": "React kursi menga zamonaviy veb-ilovalar yaratishni o'rgatdi.",
                "rating": 2,
                "is_top": True,
                "graduated_year": 2024,
                "course_slug": "reactjs-frontend",
            },
        ]

        for sd in students_data:
            course = None
            if sd.get("course_slug"):
                course = Course.objects.filter(slug=sd["course_slug"]).first()
            Student.objects.get_or_create(
                name=sd["name"],
                defaults={
                    "profession": sd["profession"],
                    "company": sd["company"],
                    "quote": sd["quote"],
                    "rating": sd["rating"],
                    "is_top": sd["is_top"],
                    "graduated_year": sd["graduated_year"],
                    "course": course,
                },
            )
            self.stdout.write(f"  O'quvchi: {sd['name']}")

        self.stdout.write(self.style.SUCCESS("Kontent muvaffaqiyatli yuklandi!"))
