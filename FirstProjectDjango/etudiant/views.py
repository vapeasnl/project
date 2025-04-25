from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import user

# Create your views here.
# Create function to add and show data
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ps = fm.cleaned_data['password']
            reg = user(name=nm, email=em, password=ps)
            reg.save()
            fm = StudentRegistration()

            
    else:
        fm = StudentRegistration()
    stud = user.objects.all()

    return render(request, 'etudiant/addandshow.html',{'form' :fm, 'stu': stud})

# Create function to Delete data
def delete_data(request, id):
    if request.method == 'POST':
        pi = user.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

# Update data
def update_data(request, id):
    if request.method == 'POST':
        pi = user.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = user.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'etudiant/updatestudent.html', {'form': fm})
