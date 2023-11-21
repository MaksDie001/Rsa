from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse


class News(models.Model):
    data=models.DateField(auto_created=True)
    news_title=models.CharField(max_length=150)
    news_text_card=models.TextField()
    news_text=RichTextUploadingField()
    news_img=models.ImageField(upload_to="photos/%Y/%m/%d/",null=True)

    def __str__(self):
        return self.news_title

    def get_absolute_url(self):
        return reverse('news_title', kwargs={'article_id': self.pk})
class Ad(models.Model):
    data = models.DateField(auto_created=True)
    ad_title = models.CharField(max_length=150)
    ad_text_card=models.TextField()
    ad_text = RichTextUploadingField()
    ad_img = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True)

class Journal(models.Model):
    title=models.CharField(max_length=155)
    img=models.ImageField(upload_to="photos/%Y/%m/%d/",null=True)
    inner=models.ManyToManyField(News,null=True)

    def get_absolute_url(self):
        return reverse('journal', kwargs={'pk': self.pk})
