from django.shortcuts import render

# Create your views here.

# creating function based myGradePoint() view in appTagDtl>views.py file (custom)
# an url for this view have to create in appTagDtl>urls.py file
def myGradePoint(request):
    return render(request, 'tagdtl/gradepoint.html',{'score':79})

# creating function based myResult() view in appTagDtl>views.py file (custom)
# an url for this view have to create in appTagDtl>urls.py file
def myResult(request):
    stdScore=[55,85,65,32,56,85,12,54,65,39]
    stdInfo={'studentScore':stdScore}
    return render(request, 'tagdtl/result.html', stdInfo)