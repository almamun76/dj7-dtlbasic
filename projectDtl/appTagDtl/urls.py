from django.urls import path

# import appTagDtl>views.py file here
from . import views

urlpatterns = [
    path('gp/', views.myGradePoint),
    path('tabulation/', views.myResult),
]
# this appSimpleDtl>urls.py file have to include in projectDtl>urls.py file