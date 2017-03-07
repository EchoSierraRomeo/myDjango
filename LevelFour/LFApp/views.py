from django.shortcuts import render

# Create your views here.

def index(request):
    index_dict = {'text':'hello world','number':1000}
    return render(request,'LFApp/index.html',context=index_dict)


def other(request):
    return render(request,'LFApp/other.html')


def relative(request):
    return render(request,'LFApp/relative_url_templates.html')
