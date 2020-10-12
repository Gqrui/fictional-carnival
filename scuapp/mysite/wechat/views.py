from django.shortcuts import HttpResponse
from django.template import loader
from .models import Tbcompany, Tbmanager, Tbstudent
from django.views.decorators.csrf import csrf_exempt
#from  django.http import HttpResponse (暂时不清楚http和shortcuts的区别）


def index(request):
    return HttpResponse("hello")


def detail(request, manager_id):
    return HttpResponse("You're looking at managerid %s." % manager_id)

@csrf_exempt
def dengluzhuce_login(request):
    if request.method == "POST":
        account_num = request.POST.get('no')
        passwd= request.POST.get('pwd')
        try:
            user = Tbmanager.objects.get(manager_id=account_num)
            if user.password != passwd:
                return HttpResponse("用户名或密码错误")

        except Tbmanager.DoesNotExist as e:
            return HttpResponse("用户名不存在")
        # 登录成功
        print(account_num)
        print(passwd)
        return HttpResponse("登录成功！")
    else:
        return HttpResponse("请求错误")

#def results(request, question_id):
    #response = "You're looking at the results of question %s."
    #return HttpResponse(response % question_id)


#def vote(request, question_id):
    #return HttpResponse("You're voting on question %s." % question_id)

