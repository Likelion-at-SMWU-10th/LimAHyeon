from django.utils import timezone
from django.shortcuts import redirect, render, get_object_or_404
from .models import Diary
from .forms import DiaryModelForm


# Create your views here.

def home (request) :
    return render(request, 'diaryapp/home.html')

def diary(request):
    diarys = Diary.objects
    return render(request, 'diaryapp/diary.html', {'diarys':diarys})

def detail(request, diary_id):
    diary_detail = get_object_or_404(Diary, pk =  diary_id )
    return render(request, 'diaryapp/detail.html',{'diary': diary_detail})

def new(request):
    return render(request, 'blogapp/new.html')



def modelformcreate(request):
    if request.method == "POST":
        form = DiaryModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diary')
        
    else: 
        form = DiaryModelForm()
    return render(request, 'diaryapp/new.html',{'form':form})


def edit(request):
    return render(request, 'diaryapp/new.html')

def diaryupdate(request, diary_id):
    post = get_object_or_404(Diary, pk=diary_id)
    if  request.method=="POST":
        form = DiaryModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('detail', diary_id=post.pk)
    else:
        form = DiaryModelForm(instance=post)
        return render(request,'diaryapp/edit.html', {'form':form})


def diarydelete(request, diary_id):
    post = get_object_or_404(Diary, pk=diary_id)
    post.delete()
    return redirect('diary')

