from django.urls import path

# import projectDtl>appSimpleDtl>views.py file here
from . import views

urlpatterns = [
    # url for aboutMe() view created in projectDtl>appSimpleDtl>views.py file
    path('', views.aboutMe),

    # this url have to register in projectDtl>urls.py file
    path('skill', views.mySkills),
]
# this appSimpleDtl>urls.py file have to include in projectDtl>urls.py file