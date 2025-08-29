from django import forms

from apps.pages.models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        exclude = ['is_read', 'comment']


    def clean(self):
        print("1. object level validation")
        print(self.cleaned_data)
        return super().clean()

    def clean_phone_number(self):
        print("2. field level validation")
        phone_number: str = self.cleaned_data.get('phone_number')
        if not phone_number.startswith('+'):
            raise forms.ValidationError("Phone number should start with +")
        return self.cleaned_data.get('phone_number')

    # ========= HOMEWORK (QUERY) LAR =========

    # BASIC
    def homework1_get_courses_without_enrollments(self):
        """Hech bir sectionida yozilish boвЂlmagan fanlarni qaytaradi"""
        pass

    def homework2_get_students_not_enrolled_in_term(self, term_id):
        """Berilgan termda umuman yozilmagan talabalarni qaytaradi"""
        pass

    def homework3_get_instructors_with_full_sections(self, term_id):
        """Berilgan termda toвЂliq toвЂlgan (capacity ga teng) sectionlari bor oвЂqituvchilarni qaytaradi"""
        pass

    def homework4_get_overbooked_sections(self, term_id):
        """Capacity dan ortiq yozilgan sectionlarni (xato holat) topadi"""
        pass

    def homework5_get_top_students_in_course(self, course_code, term_id, limit=5):
        """Kurs boвЂyicha eng yuqori oвЂrtacha imtihon balliga ega talabalarni qaytaradi"""
        pass

    def homework6_get_all_active_students(self):
        """Faol (is_active=True) talabalarni qaytaradi"""
        return Student.objects.filter(is_active=True)

    def homework7_get_courses_in_department(self, department_id):
        """Berilgan kafedradagi fanlarni qaytaradi"""
        return Course.objects.filter(department_id=department_id)

    def homework8_get_instructors_in_department(self, department_name):
        """Berilgan kafedradagi oвЂqituvchilarni qaytaradi"""
        return Instructor.objects.filter(department__name=department_name)

    def homework9_get_students_by_year(self, year):
        """Berilgan kurs (year_of_study) dagi talabalarni qaytaradi"""
        return Student.objects.filter(year_of_study=year)

    def homework10_get_sections_for_course(self, course_code):
        """Berilgan kursga tegishli barcha sectionlarni qaytaradi"""
        return Section.objects.filter(course__code=course_code)

    def homework11_get_students_born_this_year(self):
        """Hozirgi yilda tugвЂilgan talabalarni qaytaradi"""
        year = timezone.now().year
        return Student.objects.filter(birth_date__year=year)

    def homework12_get_courses_taught_by_instructor(self, instructor_id):
        """Berilgan instructor tomonidan oвЂtiladigan fanlarni qaytaradi"""
        return Course.objects.filter(sections__instructor_id=instructor_id).distinct()

    def homework13_get_courses_without_prerequisites(self):
        """Hech qanday prerequisite talab qilmaydigan fanlarni qaytaradi"""
        return Course.objects.filter(prereqs_for__isnull=True)

    def homework14_get_enrollments_of_student(self, student_id):
        """Berilgan talabaning barcha yozilishlarini qaytaradi"""
        return Enrollment.objects.filter(student_id=student_id)

    def homework15_get_exam_results_of_student(self, student_id):
        """Berilgan talabaning barcha imtihon natijalarini qaytaradi"""
        return ExamResult.objects.filter(student_id=student_id)
