from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Syllabus, Standard, Subject, Teacher, Chapter, Video, File, Chat, Student, Documents, Notification, Scheme

class StandarAdmin(admin.ModelAdmin):
    list_filter = ('syllabus', )


# class TeacherInline(admin.StackedInline):
#     model = Teacher
#     can_delete = False
#     fk_name = 'user'

# class CustomUserAdmin(UserAdmin):
#     inlines = (TeacherInline, )

#     def get_inline_instances(self, request, obj=None):
#         if not obj:
#             return list()
#         return super(CustomUserAdmin, self).get_inline_instances(request, obj)


# admin.site.register(User)
# admin.site.register(User, CustomUserAdmin)

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Syllabus)
admin.site.register(Standard, StandarAdmin)
admin.site.register(Subject)
admin.site.register(Chapter)
admin.site.register(Video)
admin.site.register(File)
admin.site.register(Documents)
admin.site.register(Chat)
admin.site.register(Notification)
admin.site.register(Scheme)
# admin.site.register(City)
# admin.site.register(Country)

