from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
import re
# Create your views here.
from user.forms import RegisterForms
from user.models import RegisterModel, Malware_Recogition_Model, FeedbackModel


def index(request):
    if request.method=="POST":
        usid=request.POST.get('username')
        pswd = request.POST.get('password')
        try:
            check = RegisterModel.objects.get(userid=usid,password=pswd)
            request.session['userid']=check.id
            return redirect('userpage')
        except:
            pass
    return render(request,'user/index.html')
def register(request):
    if request.method=="POST":
        forms=RegisterForms(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('index')
    else:
        forms=RegisterForms()
    return render(request,'user/register.html',{'form':forms})
def userpage(request):
    userid = request.session['userid']
    objec = RegisterModel.objects.get(id=userid)
    cate1=[]
    cate2,cate3,cate4,cate5,cate6,cate7,cate8,cate9,cate10,cate11,cate12,cate13,cate14,cate15,cate16,cate17,=[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
    s=''
    txt=''
    c=''
    if request.method == "POST":
        txt=request.POST.get("name")

        c = (re.findall(r"[\w']+", str(txt)))

    for f in c:
        if f in ('E tag'):
            cate1.append(f)
        elif f in ('ECSID'):
            cate2.append(f)
        elif f in ('phonemodel'):
            cate3.append(f)
        elif f in ('nginx'):
            cate4.append(f)
        elif f in ('2F4'):
            cate5.append(f)
        elif f in ('keyid'):
            cate6.append(f)
        elif f in ('apikey'):
            cate7.append(f)
        elif f in ('iosid'):
            cate8.append(f)
        elif f in ('networkoperator'):
            cate9.append(f)
        elif f in ('NLOM'):
            cate10.append(f)
        elif f in ('2C'):
            cate11.append(f)
        elif f in ('3A'):
            cate12.append(f)
        elif f in ('NID'):
            cate13.append(f)
        elif f in ('ashx'):
            cate14.append(f)
        elif f in ('vvid'):
            cate15.append(f)
        elif f in ('privateid'):
            cate16.append(f)
        elif f in ('decid'):
            cate17.append(f)


    if len(cate1)>len(cate2) and len(cate1)>len(cate3) and len(cate1)>len(cate4) and len(cate1)>len(cate5) and len(cate1)>len(cate6) and len(cate1)>len(cate7) and len(cate1)>len(cate8) and len(cate1)>len(cate9) and len(cate1)>len(cate10) and len(cate1)>len(cate11) and len(cate1)>len(cate12) and len(cate1)>len(cate13) and len(cate1)>len(cate14) and len(cate1)>len(cate15) and len(cate1)>len(cate16) and len(cate1)>len(cate17):
        s='E tag'
    elif len(cate2)>len(cate1) and len(cate2)>len(cate3) and len(cate2)>len(cate4) and len(cate2)>len(cate5) and len(cate2)>len(cate6) and len(cate2)>len(cate7) and len(cate2)>len(cate8) and len(cate2)>len(cate9) and len(cate2)>len(cate10) and len(cate2)>len(cate11) and len(cate2)>len(cate12) and len(cate2)>len(cate13) and len(cate2)>len(cate14) and len(cate2)>len(cate15) and len(cate2)>len(cate16) and len(cate2)>len(cate17):
        s='ECSID'
    elif len(cate3)>len(cate1) and len(cate3)>len(cate2) and len(cate3)>len(cate4) and len(cate3)>len(cate5) and len(cate3)>len(cate6) and len(cate3)>len(cate7) and len(cate3)>len(cate8) and len(cate3)>len(cate9) and len(cate3)>len(cate10) and len(cate3)>len(cate11) and len(cate3)>len(cate12) and len(cate3)>len(cate13) and len(cate3)>len(cate14) and len(cate3)>len(cate15) and len(cate3)>len(cate16) and len(cate3)>len(cate17):
        s='phonemodel'
    elif len(cate4)>len(cate1) and len(cate4)>len(cate2) and len(cate4)>len(cate3) and len(cate4)>len(cate5) and len(cate4)>len(cate6) and len(cate4)>len(cate7) and len(cate4)>len(cate8) and len(cate4)>len(cate9) and len(cate4)>len(cate10) and len(cate4)>len(cate11) and len(cate4)>len(cate12) and len(cate4)>len(cate13) and len(cate4)>len(cate14) and len(cate4)>len(cate15) and len(cate4)>len(cate16) and len(cate4)>len(cate17):

        s='nginx'
    elif len(cate5)>len(cate1) and len(cate5)>len(cate3) and len(cate5)>len(cate4) and len(cate5)>len(cate2) and len(cate5)>len(cate6) and len(cate5)>len(cate7) and len(cate5)>len(cate8) and len(cate5)>len(cate9) and len(cate5)>len(cate10) and len(cate5)>len(cate11) and len(cate5)>len(cate12) and len(cate5)>len(cate13) and len(cate5)>len(cate14) and len(cate5)>len(cate15) and len(cate5)>len(cate16) and len(cate5)>len(cate17):

        s='2F4'
    elif len(cate6)>len(cate1) and len(cate6)>len(cate3) and len(cate6)>len(cate4) and len(cate6)>len(cate5) and len(cate6)>len(cate2) and len(cate6)>len(cate7) and len(cate6)>len(cate8) and len(cate6)>len(cate9) and len(cate6)>len(cate10) and len(cate6)>len(cate11) and len(cate6)>len(cate12) and len(cate6)>len(cate13) and len(cate6)>len(cate14) and len(cate6)>len(cate15) and len(cate6)>len(cate16) and len(cate6)>len(cate17):

        s='keyid'
    elif len(cate7) > len(cate1) and len(cate7)>len(cate3) and len(cate7)>len(cate4) and len(cate7)>len(cate5) and len(cate7)>len(cate6) and len(cate7)>len(cate2) and len(cate7)>len(cate8) and len(cate7)>len(cate9) and len(cate7)>len(cate10) and len(cate7)>len(cate11) and len(cate7)>len(cate12) and len(cate7)>len(cate13) and len(cate7)>len(cate14) and len(cate7)>len(cate15) and len(cate7)>len(cate16) and len(cate7)>len(cate17):

        s = 'apikey'
    elif len(cate8)>len(cate1) and len(cate8)>len(cate3) and len(cate8)>len(cate4) and len(cate8)>len(cate5) and len(cate8)>len(cate6) and len(cate8)>len(cate7) and len(cate8)>len(cate2) and len(cate8)>len(cate9) and len(cate8)>len(cate10) and len(cate8)>len(cate11) and len(cate8)>len(cate12) and len(cate8)>len(cate13) and len(cate8)>len(cate14) and len(cate8)>len(cate15) and len(cate8)>len(cate16) and len(cate8)>len(cate17):

        s='iosid'
    elif len(cate9)>len(cate1) and len(cate9)>len(cate3) and len(cate9)>len(cate4) and len(cate9)>len(cate5) and len(cate9)>len(cate6) and len(cate9)>len(cate7) and len(cate9)>len(cate8) and len(cate9)>len(cate2) and len(cate9)>len(cate10) and len(cate9)>len(cate11) and len(cate9)>len(cate12) and len(cate9)>len(cate13) and len(cate9)>len(cate14) and len(cate9)>len(cate15) and len(cate9)>len(cate16) and len(cate9)>len(cate17):

        s='networkoperator'
    elif len(cate10)>len(cate1) and len(cate10)>len(cate3) and len(cate10)>len(cate4) and len(cate10)>len(cate5) and len(cate10)>len(cate6) and len(cate10)>len(cate7) and len(cate10)>len(cate8) and len(cate10)>len(cate9) and len(cate10)>len(cate2) and len(cate10)>len(cate11) and len(cate10)>len(cate12) and len(cate10)>len(cate13) and len(cate10)>len(cate14) and len(cate10)>len(cate15) and len(cate10)>len(cate16) and len(cate10)>len(cate17):

        s='NLOM'
    elif len(cate11)>len(cate1) and len(cate11)>len(cate3) and len(cate11)>len(cate4) and len(cate11)>len(cate5) and len(cate11)>len(cate6) and len(cate11)>len(cate7) and len(cate11)>len(cate8) and len(cate11)>len(cate9) and len(cate11)>len(cate10) and len(cate11)>len(cate2) and len(cate11)>len(cate12) and len(cate11)>len(cate13) and len(cate11)>len(cate14) and len(cate11)>len(cate15) and len(cate11)>len(cate16) and len(cate11)>len(cate17):

        s=' '
    elif len(cate12)>len(cate1) and len(cate12)>len(cate3) and len(cate12)>len(cate4) and len(cate12)>len(cate5) and len(cate12)>len(cate6) and len(cate12)>len(cate7) and len(cate12)>len(cate8) and len(cate12)>len(cate9) and len(cate12)>len(cate10) and len(cate12)>len(cate11) and len(cate12)>len(cate2) and len(cate12)>len(cate13) and len(cate12)>len(cate14) and len(cate12)>len(cate15) and len(cate12)>len(cate16) and len(cate12)>len(cate17):

        s='3A'
    elif len(cate13)>len(cate1) and len(cate13)>len(cate3) and len(cate13)>len(cate4) and len(cate13)>len(cate5) and len(cate13)>len(cate6) and len(cate13)>len(cate7) and len(cate13)>len(cate8) and len(cate13)>len(cate9) and len(cate13)>len(cate10) and len(cate13)>len(cate11) and len(cate13)>len(cate12) and len(cate13)>len(cate2) and len(cate13)>len(cate14) and len(cate13)>len(cate15) and len(cate13)>len(cate16) and len(cate13)>len(cate17):

        s='NID'
    elif len(cate14)>len(cate1) and len(cate14)>len(cate3) and len(cate14)>len(cate4) and len(cate14)>len(cate5) and len(cate14)>len(cate6) and len(cate14)>len(cate7) and len(cate14)>len(cate8) and len(cate14)>len(cate9) and len(cate14)>len(cate10) and len(cate14)>len(cate11) and len(cate14)>len(cate12) and len(cate14)>len(cate13) and len(cate14)>len(cate2) and len(cate14)>len(cate15) and len(cate14)>len(cate16) and len(cate14)>len(cate17):

        s='ashx'
    elif len(cate15)>len(cate1) and len(cate15)>len(cate3) and len(cate15)>len(cate4) and len(cate15)>len(cate5) and len(cate15)>len(cate6) and len(cate15)>len(cate7) and len(cate15)>len(cate8) and len(cate15)>len(cate9) and len(cate15)>len(cate10) and len(cate15)>len(cate11) and len(cate15)>len(cate12) and len(cate15)>len(cate13) and len(cate15)>len(cate14) and len(cate15)>len(cate2) and len(cate15)>len(cate16) and len(cate15)>len(cate17):

        s='vvid'
    elif len(cate16)>len(cate1) and len(cate16)>len(cate3) and len(cate16)>len(cate4) and len(cate16)>len(cate5) and len(cate16)>len(cate6) and len(cate16)>len(cate7) and len(cate16)>len(cate8) and len(cate16)>len(cate9) and len(cate16)>len(cate10) and len(cate16)>len(cate11) and len(cate16)>len(cate12) and len(cate16)>len(cate13) and len(cate16)>len(cate14) and len(cate16)>len(cate15) and len(cate16)>len(cate2) and len(cate16)>len(cate17):

        s='privateid'
    elif len(cate17)>len(cate1) and len(cate17)>len(cate3) and len(cate17)>len(cate4) and len(cate17)>len(cate5) and len(cate17)>len(cate6) and len(cate17)>len(cate7) and len(cate17)>len(cate8) and len(cate17)>len(cate9) and len(cate17)>len(cate10) and len(cate17)>len(cate11) and len(cate17)>len(cate12) and len(cate17)>len(cate13) and len(cate17)>len(cate14) and len(cate17)>len(cate15) and len(cate17)>len(cate16) and len(cate17)>len(cate2):

        s='decid'
    else:
        s="not malware affected"
    Malware_Recogition_Model.objects.create(usid=objec,links=txt,result=s)


    return render(request,'user/userpage.html',{'form':s})

def logout(request):
    return redirect('index')

def mydetails(request):
    userid = request.session['userid']
    ted = RegisterModel.objects.get(id=userid)
    return render(request,'user/mydetails.html', {'object': ted})

def updatemydetails(request):
    userid = request.session['userid']
    objec = RegisterModel.objects.get(id=userid)
    if request.method == "POST":
        FirstName = request.POST.get('FirstName', '')
        LastName = request.POST.get('LastName', '')
        UserId = request.POST.get('UserId', '')
        Password = request.POST.get('Password', '')
        MobileNumber = request.POST.get('MobileNumber', '')
        EmailId = request.POST.get('EmailId', '')
        Gender = request.POST.get('Gender', '')

        obj = get_object_or_404(RegisterModel, id=userid)
        obj.firstname = FirstName
        obj.lastname = LastName
        obj.userid = UserId
        obj.password = Password
        obj.mblenum = MobileNumber
        obj.email = EmailId
        obj.gender = Gender

        obj.save(update_fields=["firstname", "lastname", "userid", "password", "mblenum", "email",
                                "gender", ])
        return redirect('mydetails')

    return render(request,'user/updatemydetails.html',{'obj': objec})

def analysisresult(request):
    chart = Malware_Recogition_Model.objects.values('result').annotate(dcount=Count('result'))
    return render(request,'user/analysisresult.html',{'objects':chart})

def graph_page(request,chart_type):
    chart = Malware_Recogition_Model.objects.values('result').annotate(dcount=Count('result'))
    return render(request,'user/graph_page.html',{'chart_type':chart_type,'objects':chart})

def feedback(request):
    userid = request.session['userid']
    object = RegisterModel.objects.get(id=userid)
    if request.method == "POST":
        feed = request.POST.get('feedback')
        FeedbackModel.objects.create(uid=object, feedback=feed)
    return render(request,'user/feedback.html')