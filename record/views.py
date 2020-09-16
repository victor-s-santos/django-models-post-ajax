from django.shortcuts import render, redirect
from .models import Records

def record_value(request):
    records = Records.objects.all()
    return render(request, 'records.html', {'records': records})

def insert(request):
    member = Records(user=request.user, score=request.POST['score'])
    member.save()
    return redirect('record')
# Create your views here.
