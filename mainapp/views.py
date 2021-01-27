from django.shortcuts import render, redirect, HttpResponse
from rest_framework import viewsets

from .serializers import SerializeStudent
from .models import StudentDetails


# REST API CLASS
class StudentViewSet(viewsets.ModelViewSet):
    queryset = StudentDetails.objects.all().order_by('name')
    serializer_class = SerializeStudent


def view(request):
    if request.method == 'GET':
        details = StudentDetails.objects.all()
        return render(request, 'mainapp/view.html', {"details": details})
    else:
        if request.POST['action'] == 'Update':
            if(StudentDetails.objects.filter(name=request.POST['name']).update(
                mark1=request.POST['mark1'],
                mark2=request.POST['mark2'],
                mark3=request.POST['mark3'],
                total=request.POST['total']
            )):
                return HttpResponse("<script>alert('successfully updated');location.href = '/'</script>")
            else:
                return HttpResponse("<script>alert('Something went wrong');location.href = '/'</script>")

        elif request.POST['action'] == 'Delete':
            if(StudentDetails.objects.filter(name=request.POST['name']).delete()[0]):
                return HttpResponse("<script>alert('successfully deleted');location.href = '/'</script>")
            else:
                return HttpResponse("<script>alert('Something went wrong');location.href = '/'</script>")


def add(request):
    if request.method == 'GET':
        return render(request, 'mainapp/add.html')
    else:
        s = StudentDetails(name=request.POST['name'].replace(" ", "_"),
                           mark1=request.POST['mark1'],
                           mark2=request.POST['mark2'],
                           mark3=request.POST['mark3'],
                           total=request.POST['total'])
        s.save()
        return HttpResponse("<script>alert('success');location.href = '/'</script>")


