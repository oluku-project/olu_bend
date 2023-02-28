from django.contrib import admin

from .models import *
import admin_thumbnails
# Register your models here.


@admin_thumbnails.thumbnail('imageurl')
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('name', 'company')


@admin_thumbnails.thumbnail('imageurl')
class AboutsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


@admin_thumbnails.thumbnail('imageurl')
class BrandsAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin_thumbnails.thumbnail('icon')
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('name', 'bgColor')


admin.site.register(Testimonials, TestimonialsAdmin)
admin.site.register(Abouts, AboutsAdmin)
admin.site.register(Brands, BrandsAdmin)
admin.site.register(Skills, SkillsAdmin)
admin.site.register(Contact)
admin.site.register(Experience)
admin.site.register(WorkExperience)
admin.site.register(Work)
admin.site.register(Tag)
