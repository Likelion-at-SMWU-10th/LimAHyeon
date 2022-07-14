from django.shortcuts import render, get_object_or_404

from .models import Diary

# Create your views here.

def home (request) :
    return render(request, 'diaryapp/home.html')


def planner (request) :
    return render(request, 'diaryapp/planner.html')

def diary(request):
    diarys = Diary.objects
    return render(request, 'diaryapp/diary.html', {'diarys':diarys})

def detail(request, diary_id):
    diary_detail = get_object_or_404(Diary, pk =  diary_id )
    return render(request, 'diaryapp/detail.html',{'diary': diary_detail})
