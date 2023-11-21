from django.urls import path
from .views import *
urlpatterns = [
    path("",home,name="home"),
    path("article/<int:pk>",Arcticle.as_view(),name="article"),
    path("announcement",announcement,name="announcement"),
    path("announcement/<int:pk>",Announcement_DT.as_view(),name="announcement"),
    path("journal",journal,name="journal"),
    path("journal/<int:pk>",Journal_View,name="journalv"),
]
