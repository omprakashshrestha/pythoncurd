from django.shortcuts import render, redirect
from curdapplication.forms import EmployeeForm
from curdapplication.models import Employee

# Create your views here.
# inserting fuction to enter data in database
def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form =EmployeeForm()
    return render(request, "index.html", {'form':form})

# retriving methods from database
def show(request):
    # works like database query select all from table
    employees = Employee.objects.all()
    return render(request, "show.html", {'employees':employees})

def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, "edit.html", {'employee':employee})

def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance = employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request,"edit.html", {'employee':employee})

def delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")