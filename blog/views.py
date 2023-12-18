from django.shortcuts import render
from .models import Post


dummy_data=[
    {
        'author':'yassine',
        'id':1,
        'title':'Learn Django',
        'description':'Django is python framework',
        'date_posted':'August 12, 2023',
    },
    {
        'author':'ali',
        'id':2,
        'title':'Learn HTML',
        'description':'HTML is Hyper Text Makeup Language',
        'date_posted':'August 13, 2023',
    },
    {
        'author':'ali',
        'id':3,
        'title':'Learn HTML',
        'description':'HTML is Hyper Text Makeup Language',
        'date_posted':'August 13, 2023',
    },
    {
        'author':'ali',
        'id':4,
        'title':'Learn HTML',
        'description':'HTML is Hyper Text Makeup Language',
        'date_posted':'August 13, 2023',
    },
    {
        'author':'oussama',
        'id':5,
        'title':'Learn Django with HTML and CSS',
        'description':'HTML is Hyper Text Makeup Language',
        'date_posted':'August 13, 2023',
    },
    {
        'author':'rhayrhay',
        'id':6,
        'title':'Learn Laravel',
        'description':'Laravel is framework build on top of php',
        'date_posted':'April 13, 2023',
    },
   
]

def home(request):
    context={
        'dummy_data':Post.objects.all(),
    }
    return render(request,'blog/home.html',context)


def about(request):
    return render(request,'blog/about.html',{'title':'About'})