from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
cursor = connection.cursor()



def okay(request):
    return HttpResponse('pretend-binary-data-here', content_type='image/jpeg')

def home(request):
    return render(request, 'home.html')


def company(request):
    return render(request, 'company.html')


def newjob(request):
    cursor.execute('''select max(companyid) from company;''')
    company_id=cursor.fetchone()
    company_id=company_id[0]+1
    company_name=request.POST.get('companyname','default')
    role=request.POST.get('role','default')
    salary=request.POST.get('salary','1')
    openings=request.POST.get('openings','1')
    cursor.execute('''insert into company values(%s,%s,%s,%s,%s);''',[company_id,company_name,role,salary,openings])
    return render(request,'home.html',{'alert' : 'Job Added Successfully!!','set':1})




def jobs(request):
    cursor.execute('''select * from company;''')
    data1=cursor.fetchall()
    para = {'data' : data1}
    return render(request, 'jobs.html',para)

def employee(request):
    return render(request,'employee.html')


def newemployee(request):
    cursor.execute('''select max(employeeid) from employee;''')
    employeeid=cursor.fetchone()
    employeeid=employeeid[0]+1
    name=request.POST.get('name','default')
    phone=request.POST.get('phone','default')
    email=request.POST.get('email','123@gmail.com')
    file=request.POST.get('file','1')
    cursor.execute('''insert into employee values(%s,%s,%s,%s,%s);''',[employeeid,name,phone,email,file])
    return render(request,'home.html',{'alert2' : 'Application Submitted Successfully!!','set':2})
