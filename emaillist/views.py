from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from emaillist.models import Emaillist


def index(request):
    # 이메일 리스트 객체와 동등한 object 의 전체
    # all_of_emaillist = Emaillist.objects.all().order_by('-id')
    # print(all_of_emaillist)

    # return render(request, 'index.html', data)

    all_of_emaillist = Emaillist.objects.all().order_by('-id')
    data = {'all_of_emaillist': all_of_emaillist}
    print(data)
    return render(request, 'emaillist/index.html', data)

def form(request):
    return render(request, 'emaillist/form.html')

def add(request):
    emaillist = Emaillist()
    emaillist.first_name = request.POST['fn']
    emaillist.last_name = request.POST['ln']
    emaillist.email = request.POST['email']

    emaillist.save()

    # 폼 전송양식은 전송 후 redirect 하지 않으면 F5(refresh) 시 재전송...
    # return render(request, 'success.html')
    return HttpResponseRedirect('/emaillist')