from django.shortcuts import render
from .models import Diary
from .forms import DiaryForm,UserRegistrationForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.

def index(request):
    return render(request,'index.html')

def diary_list(request):
    diaries = Diary.objects.all().order_by('-created_at')
    return render(request,'diary_list.html',{'diaries':diaries})

@login_required
def diary_create(request):
    if request.method == 'POST':
        form = DiaryForm(request.POST,request.FILES)
        if form.is_valid():
            diary = form.save(commit=False)
            diary.user = request.user
            diary.save()
            return redirect('diary_list')
    else:
        form = DiaryForm()
    return render(request,'diary_form.html',{'form': form})

@login_required
def diary_edit(request,diary_id):
    diary = get_object_or_404(Diary,pk=diary_id,user = request.user)
    if request.method=='POST':
        form = DiaryForm(request.POST,request.FILES,instance=diary)
        if form.is_valid():
            diary = form.save(commit=False)
            diary.user = request.user
            diary.save()
            return redirect('diary_list')
    else:
        form = DiaryForm(instance=diary)
    return render(request,'diary_form.html',{'form': form})

@login_required
def diary_delete(request,diary_id):
    diary =get_object_or_404(Diary,pk=diary_id,user=request.user)
    if request.method == 'POST':
        diary.delete()
        return redirect('diary_list')
    return render(request,'diary_confirm_delete.html',{'diary': diary})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('diary_list')
    else:
        form = UserRegistrationForm()
    return render(request,'registration/register.html',{'form': form})