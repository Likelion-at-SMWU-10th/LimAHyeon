from cmath import isnan
import re
from django.utils import timezone
from django.shortcuts import redirect, render, get_object_or_404
from .models import Diary, Comment
from .forms import DiaryModelForm, CommentForm


# Create your views here.

def home (request) :
    return render(request, 'diaryapp/home.html')

def diary(request):
    diarys = Diary.objects
    return render(request, 'diaryapp/diary.html', {'diarys':diarys})

def detail(request, diary_id):
 
    diary = get_object_or_404(Diary, pk = diary_id)
    form = CommentForm()
    return render(request, 'diaryapp/detail.html', {'form': form, 'diary':diary})



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


def result(request):
    query = request.GET.get('query', '')
    if query:
        diary_objects = Diary.objects.filter(title__contains = query)
        return render(request, 'diaryapp/result.html', {'result': diary_objects} )
    else: 
        return render(request, 'diaryapp/result.html', {'error': "검색어를 입력해주세요. "} )
    


def commentcreate(request, diary_id):
    diary = get_object_or_404(Diary, pk = diary_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.diary = diary
            comment.save()
        
    return redirect('detail', diary_id=diary.pk)
    
 
def edit_comment(request):
    return render(request, 'diaryapp/comment_update.html')


def update_comment(request, diary_id):
    post = get_object_or_404(Diary, pk=diary_id)
    if request.method == "POST":
         form = CommentForm(request.POST, instance=post )
         if form.is_valid():
            comment = form.save(commit=False)
            comment.diary = diary
            form.save()
            return redirect('detail', diary_id=post.pk)
    else:
        form = CommentForm(instance=post)
        return render(request,'diaryapp/comment_update.html', {'form':form})

def delete_comment(request, diary_id) :
    post = get_object_or_404(Diary, pk=diary_id)
    post.delete()
    return redirect('diary')
    
        