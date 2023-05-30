from django.shortcuts import render
from  django.http import HttpResponse
from . models import Student
import json
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.


def add(request):
    if request.method=='POST':
        name = request.POST.get('StudentName')
        print(name)
        Id = request.POST.get('ID')
        print(Id)
        gpa = request.POST.get('GPA')
        print(gpa)
        phone = request.POST.get('Number')
        print(phone)
        mail = request.POST.get('Email')
        print(mail)
        birthday = request.POST.get('birthday')
        print(birthday)
        gender = request.POST.get('gender')
        print(gender)
        state = request.POST.get('statue')
        print(state)
        level = request.POST.get('level')
        print(level)
        department = request.POST.get('department')
        print(department)
        data = Student.objects.create(
            name=name, id=Id, gpa=gpa, phone=phone, mail=mail, birthday=birthday,
            gender=gender, state=state, level=level, department=department,
        )
    return render(request, 'pages/add_student_page.html')


def edit(request):
    if request.method=='POST':
            id = request.POST.get('idd')
            print(id)
            info = request.POST.get('info')
            print(info)
            option = request.POST.get('options')
            print(option)
            btn1=request.POST.get('update')
            print(btn1)
            btn2 = request.POST.get('delete')
            print(btn2)
            x=False
            for s in Student.objects.all():
                if s.id ==id:
                    x=True
                    break
            if x==True:
                if btn2 is None:
                    if option =='GPA':
                        Student.objects.filter(id = id).update(gpa=info)
                    elif option =='ID':
                        Student.objects.filter(id=id).update(id=info)

                    elif option == 'Mobile number':
                        Student.objects.filter(id=id).update(phone=info)
                    elif option =='Name':
                        Student.objects.filter(id=id).update(name=info)
                    elif option =='Status':
                        Student.objects.filter(id=id).update(state=info)
                    elif option == 'Gender':
                        Student.objects.filter(id=id).update(gender=info)
                    elif option == 'date of birth':
                        Student.objects.filter(id=id).update(birthday=info)
                    elif option == 'Email':
                        Student.objects.filter(id=id).update(email=info)
                else:
                    Student.objects.filter(id=id).delete()

    return render(request, 'pages/edit_page.html')
def home(request):
    return render(request, 'pages/home_page.html')
def projects(request):
    return render(request, 'pages/projects_page.html')   

def search(request):
    stud = {'search': Student.objects.all()}
    return render(request, 'pages/search_page.html',stud)

def search_ajax(request):
    if request.method == "GET":
        id = request.GET.get("id")
        status = request.GET.get("status")
        if status == "All":
            students = Student.objects.filter(id=id).values()

        else:
            students = Student.objects.filter(id=id, state=status).values()

        if students != "":
            output = "["
            for x in students:
                output = output + json.dumps(x,cls=DjangoJSONEncoder) + ","
            index = len(output) - 1
            output = output[:index] + "]"
            if output== "]":
                output = ""
            return HttpResponse(output)
        else:
            return HttpResponse("")

def view(request):
    st = Student.objects.all().values()
    if request.method == 'POST':
        option = request.POST.get('student status')
        if option =='Active':
            st = Student.objects.filter(state='Active').values()
        elif option == 'Inactive':
            st = Student.objects.filter(state='Inactive').values()
        else:
            st = Student.objects.all().values()
        return render(request, 'pages/view_students_page.html', {'view': st})
    return render(request, 'pages/view_students_page.html', {'view': st})


def department(request):
    if request.method=='POST':
        id = request.POST.get('studentID')
        option = request.POST.get('department')
        print(id)
        print(option)
        x = False
        for s in Student.objects.all():
            if s.id == id:
                x = True
                break
        if x == True:
            stLevel=Student.objects.get(id=id).level
            if stLevel != '3':
                return render(request, 'pages/department_page.html')
            else:
              Student.objects.filter(id=id).update(department=option)
    return render(request, 'pages/department_page.html')



