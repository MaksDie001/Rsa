

from .models import *
from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostAdminForm(forms.ModelForm):
    news_text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = News
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    list_display = ("news_title",)
    form = PostAdminForm

class AdAdminForm(forms.ModelForm):
    ad_text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Ad
        fields = '__all__'

class AdAdmin(admin.ModelAdmin):
    list_display = ("ad_title",)
    form = AdAdminForm
admin.site.register(News,PostAdmin)
admin.site.register(Ad,AdAdmin)
admin.site.register(Journal)

