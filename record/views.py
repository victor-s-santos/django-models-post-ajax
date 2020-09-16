from django.shortcuts import render
from .models import Records

def record_value(request):
    records = Records.objects.all()
    return render(request, 'records.html', {'records': records})
# Create your views here.
