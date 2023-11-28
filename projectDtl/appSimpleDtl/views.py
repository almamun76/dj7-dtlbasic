from django.shortcuts import render

# Create your views here.

# creating function based aboutMe() view (custom)
# an url for this view have to create in projectDtl>appSimpleDtl>urls.py file
def aboutMe(request):
    valName='Abdullah Al Mamun'
    valProfile='00 level DJango Developer'
    valEmail='mamun@gmail.com'
    valPhone=12345678910
    myIntro={'name':valName, 'profile':valProfile, 'email':valEmail, 'phone':valPhone}
    # pass some value to about.html page in the form of python dictionary
    # key's of the dictionary is used to receive data value in the about.html page
    return render(request, 'simpledtl/about.html', myIntro)

# creating function based mySkills() view (custom)
# an url for this view have to create in projectDtl>appSimpleDtl>urls.py file
def mySkills(request):
    # pass some value to about.html page in the form of python dictionary
    # key's of the dictionary is used to receive data value in the about.html page
    return render(request, 'simpledtl/skill.html',{'html':0,'css':0,'bs':0,'js':0})