from django.shortcuts import render, get_object_or_404, redirect,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.db.models import Q
from .models import Rquiz,Quiz
from homepage.models import Myusr
from forums.models import ForumDB
from django.http import HttpResponse
# Create your views here.
def basic(request):
	return render(request,'randomq/basic.html')

def q(request):
    if not request.user.is_authenticated():
        return render(request,'homepage/login.html')
    else:
        flag=0
        obj=Myusr.objects.get(user=request.user)
        if obj.house=='0':
            q1 = Rquiz.objects.get(numberr=1)
            q2 = Rquiz.objects.get(numberr=2)
            q3 = Rquiz.objects.get(numberr=3)
            q4 = Rquiz.objects.get(numberr=4)
            q5 = Rquiz.objects.get(numberr=5)
            q6 = Rquiz.objects.get(numberr=6)
            q7 = Rquiz.objects.get(numberr=7)
            q8 = Rquiz.objects.get(numberr=8)
            q9 = Rquiz.objects.get(numberr=9)
            q10 = Rquiz.objects.get(numberr=10)
            context = {'q1': q1,'q2':q2,'q3':q3,'q4':q4,'q5':q5,'q6':q6,'q7':q7,'q8':q8,'q9':q9,'q10':q10,'flag':flag}
            choice = request.POST.get('option')
            obj = Myusr.objects.get(user=request.user)
            if choice=='1':
                obj.preferredh="Gryffindor"
            if choice == '2':
                    obj.preferredh = "Slytherin"
            if choice == '3':
                obj.preferredh = "Ravenclaw"
            if choice == '4':
                obj.preferredh = "Hufflepuff"
            obj.save()
            return render(request, 'randomq/q.html', context)
        else:
            flag=1
            return render(request,'randomq/basic.html',{'flag':flag})
def cal(request):
    obj=Myusr.objects.get(user=request.user)
    d={}
    flag={}
    flag[0]=0
    total_score=0
    choice = request.POST.getlist('option')
    k=0
    i=0
    j=1
    for c in choice:
        if c=='4':
            d[i]=j
            flag[0]=1
        else:
            d[i]=0
            if Rquiz.objects.filter(answer=choice[i]).filter(numberr=j):
                total_score=total_score+1
        j=j+1
        i=i+1

    if total_score>=8:
        obj.house=obj.preferredh
    else:
        if total_score<2:
            obj.house="Hufflepuff"
        if total_score >=2 and total_score<4:
            obj.house = "Ravenclaw"
        if total_score<6 and total_score>=4:
            obj.house="Slytherin"
        if total_score<8 and total_score>=6:
            obj.house="Gryffindor"
    obj.tempscore=total_score
    sort=obj.house
    obj.save()

    if flag[0]==1:
       q1 = Rquiz.objects.filter(numberr=d[0])
       q2 = Rquiz.objects.filter(numberr=d[1])
       q3 = Rquiz.objects.filter(numberr=d[2])
       q4 = Rquiz.objects.filter(numberr=d[3])
       q5 = Rquiz.objects.filter(numberr=d[4])
       q6 = Rquiz.objects.filter(numberr=d[5])
       q7 = Rquiz.objects.filter(numberr=d[6])
       q8 = Rquiz.objects.filter(numberr=d[7])
       q9 = Rquiz.objects.filter(numberr=d[8])
       q10 = Rquiz.objects.filter(numberr=d[9])
       context={'sort':sort,'total_score':total_score,'flag':flag[0],'q2':q2,'q1':q1,'q3':q3,'q4':q4,'q5':q5,'d1':d[0],'d2':d[1],'d3':d[2],'d4':d[3],'d5':d[4],'q6':q6,'q7':q7,'q8':q8,'q9':q9,'q10':q10,'d6':d[5],'d7':d[6],'d8':d[7],'d9':d[8],'d10':d[9]}

       return render(request,'randomq/reviewc.html',context)
    else:
        return render(request,'randomq/review.html',{'total_score':total_score,'sort':sort})


def mainquiz(request):
    if not request.user.is_authenticated():
        return render(request,'homepage/login.html')
    else:
        obj=Myusr.objects.get(user=request.user)
        c=obj.house
        if c=='0':
            f=1
            return render(request,'randomq/basic.html',{'f':f})
        else:
            l=la=lb=lc=0
            l1=obj.level1
            l2=obj.level2
            l3=obj.level3
            l4=obj.level4
            if l3==0:
                lb=1
            if l4==0:
                lc=1
            if l2==0:
                la=1
            if l1==0:
                l=1
            if l1==0 and l2==0 and l3==0 and l4==0:
                ob=Myusr.objects.get(user=request.user)
                if ob.bonfl==1:
                    fl=0
                    fd=1
                    context={'fl':fl,'fd':fd}
                if ob.bonfl==0:
                    fl=1
                    ob.bonfl=1
                    ob.save()
                    fd=0
                    cll=5
                    q1 = Quiz.objects.get(numberr=66)
                    q2 = Quiz.objects.get(numberr=67)
                    q3 = Quiz.objects.get(numberr=68)
                    q4 = Quiz.objects.get(numberr=69)
                    q5 = Quiz.objects.get(numberr=70)
                    context = {'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4, 'q5': q5, 'fd':fd,'cll': cll,'fl':fl}
                return render(request, 'randomq/bonus.html',context)
            else:
                f1=0
                #challenge
                f2=1
                #play
                context={'f1':f1,'la':la,'lb':lb,'lc':lc,'l':l,'f2':f2}
                return render(request, 'randomq/mainquiz.html',context)

def spells(request,idi):
    obj=Myusr.objects.get(user=request.user)
    d=obj.level1
    cll=1
    if idi=='0':
        if d==0:
            return redirect('randomq:mainquiz')
        if d==2:
            q1 = Quiz.objects.get(numberr=26)
            q2 = Quiz.objects.get(numberr=27)
            q3 = Quiz.objects.get(numberr=28)
            q4 = Quiz.objects.get(numberr=29)
            q5 = Quiz.objects.get(numberr=30)
            context={'q1':q1,'q2':q2,'q3':q3,'q4':q4,'q5':q5,'cll':cll}
            return render(request,'randomq/level.html',context)
        if d==1:
            c=1
            q1=Quiz.objects.get(numberr=21)
            q2=Quiz.objects.get(numberr=22)
            q3 = Quiz.objects.get(numberr=23)
            q4=Quiz.objects.get(numberr=24)
            q5=Quiz.objects.get(numberr=25)
            context={'c':c,'q1':q1,'q2':q2,'q3':q3,'q4':q4,'q5':q5}
            return render(request, 'randomq/spells.html',context)
        if d==3:
            q1=Quiz.objects.get(numberr=31)
            q2=Quiz.objects.get(numberr=32)
            q3 = Quiz.objects.get(numberr=33)
            q4=Quiz.objects.get(numberr=34)
            q5=Quiz.objects.get(numberr=35)
            context={'q1':q1,'q2':q2,'q3':q3,'q4':q4,'q5':q5,'cll':cll}
            return render(request, 'randomq/level.html',context)


def books(request,id2):
    obj=Myusr.objects.get(user=request.user)
    d=obj.level2
    cll=2
    if id2=='0':
        if d==0:
            return redirect('randomq:mainquiz')
        if d==1:
            c=2
            q1 = Quiz.objects.get(numberr=16)
            q2 = Quiz.objects.get(numberr=17)
            q3 = Quiz.objects.get(numberr=18)
            q4 = Quiz.objects.get(numberr=19)
            q5 = Quiz.objects.get(numberr=20)
            context={'c':c,'q1':q1,'q2':q2,'q3':q3,'q4':q4,'q5':q5}
            return render(request, 'randomq/spells.html',context)
        if d==2:
            q1 = Quiz.objects.get(numberr=46)
            q2 = Quiz.objects.get(numberr=47)
            q3 = Quiz.objects.get(numberr=48)
            q4 = Quiz.objects.get(numberr=49)
            q5 = Quiz.objects.get(numberr=50)
            context={'q1':q1,'q2':q2,'q3':q3,'q4':q4,'q5':q5,'cll':cll}
            return render(request, 'randomq/level.html',context)
        if d==3:
            q1 = Quiz.objects.get(numberr=51)
            q2 = Quiz.objects.get(numberr=52)
            q3 = Quiz.objects.get(numberr=53)
            q4 = Quiz.objects.get(numberr=54)
            q5 = Quiz.objects.get(numberr=55)
            context={'q1':q1,'q2':q2,'q3':q3,'q4':q4,'q5':q5,'cll':cll}
            return render(request, 'randomq/level.html',context)



def movies(request,id3):
    obj=Myusr.objects.get(user=request.user)
    d=obj.level3
    cll=3
    if id3=='0':
        if d==0:
            return redirect('randomq:mainquiz')
        if d==1:
            c=3
            q1 = Quiz.objects.get(numberr=11)
            q2 = Quiz.objects.get(numberr=12)
            q3 = Quiz.objects.get(numberr=13)
            q4 = Quiz.objects.get(numberr=14)
            q5 = Quiz.objects.get(numberr=15)
            context = {'c': c, 'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4, 'q5': q5}
            return render(request, 'randomq/spells.html',context)
        if d==2:
            q1 = Quiz.objects.get(numberr=56)
            q2 = Quiz.objects.get(numberr=57)
            q3 = Quiz.objects.get(numberr=58)
            q4 = Quiz.objects.get(numberr=59)
            q5 = Quiz.objects.get(numberr=60)
            context={'q1':q1,'q2':q2,'q3':q3,'q4':q4,'q5':q5,'cll':cll}
            return render(request, 'randomq/level.html',context)
        if d==3:
            q1 = Quiz.objects.get(numberr=61)
            q2 = Quiz.objects.get(numberr=62)
            q3 = Quiz.objects.get(numberr=63)
            q4 = Quiz.objects.get(numberr=64)
            q5 = Quiz.objects.get(numberr=65)
            context={'q1':q1,'q2':q2,'q3':q3,'q4':q4,'q5':q5,'cll':cll}
            return render(request, 'randomq/level.html',context)

def quotes(request,id4):
    obj=Myusr.objects.get(user=request.user)
    d=obj.level4
    cll=4
    if id4=='0':
        if d==0:

            return redirect('randomq:mainquiz')
        if d==1:
            c=4
            q1 = Quiz.objects.get(numberr=1)
            q2 = Quiz.objects.get(numberr=2)
            q3 = Quiz.objects.get(numberr=3)
            q4 = Quiz.objects.get(numberr=4)
            q5 = Quiz.objects.get(numberr=5)
            context={'c':c,'q1':q1,'q2':q2,'q3':q3,'q4':q4,'q5':q5}
            return render(request, 'randomq/spells.html',context)
        if d==3:
            q1 = Quiz.objects.get(numberr=41)
            q2 = Quiz.objects.get(numberr=42)
            q3 = Quiz.objects.get(numberr=43)
            q4 = Quiz.objects.get(numberr=44)
            q5 = Quiz.objects.get(numberr=45)
            context={'q1':q1,'q2':q2,'q3':q3,'q4':q4,'q5':q5,'cll':cll}
            return render(request, 'randomq/level.html',context)
        if d==2:
            q1 = Quiz.objects.get(numberr=36)
            q2 = Quiz.objects.get(numberr=37)
            q3 = Quiz.objects.get(numberr=38)
            q4 = Quiz.objects.get(numberr=39)
            q5 = Quiz.objects.get(numberr=40)
            context={'q1':q1,'q2':q2,'q3':q3,'q4':q4,'q5':q5,'cll':cll}
            return render(request, 'randomq/level.html',context)

def qcallead(request,category):
    total_score=0
    if category=='2':
        end2=0
        obj = Myusr.objects.get(user=request.user)
        l = obj.level2
        i = 0
        if l==1:
            j=16
        if l==2:
            j= 46
        if l==3:
            j=51
        choice = request.POST.getlist('option')
        for c in choice:
            if Quiz.objects.filter(answer=choice[i]).filter(numberr=j):
                total_score = total_score + 1
            i = i + 1
            j = j + 1
        cat=2
        if total_score >= 3:
            cl = Myusr.objects.get(user=request.user)
            cll = cl.level2
            if cll == 1:
                if total_score > cl.score2:
                    cl.score2 = total_score
                else:
                    cl.score2 = cl.score2 + total_score
            if cll == 2:
                if total_score > cl.score21:
                    cl.score21 = total_score
                else:
                    cl.score21 = cl.score21 + total_score
            if cll == 3:
                if total_score > cl.score22:
                    cl.score22 = total_score
                else:
                    cl.score22 = cl.score22 + total_score
            cl.totals2 = cl.score2 + cl.score21 + cl.score22
            cl.level2 = cl.level2 + 1
            lvl = 1
            if cl.level2 == 4:
                cl.level2 = 0
                end2 = 1
                lvl = 0

            cl.save()
            cll = cll + 1
            return render(request, 'randomq/display.html',
                          {'total_score': total_score, 'end2': end2, 'lvl': lvl, 'cll': cll, 'cat': cat})
        if total_score < 3:
            pl = 1
            cl = Myusr.objects.get(user=request.user)
            cll = cl.level2
            if cll == 1:
                cl.score2 = total_score
            if cll == 2:
                cl.score21 = total_score
            if cll == 3:
                cl.score22 = total_score
            cl.totals2 = cl.score2 + cl.score21 + cl.score22
            cl.save()
            return render(request, 'randomq/display.html', {'total_score': total_score, 'pl': pl, 'cll': cll, 'cat': cat})

    if category=='1':
        end1=0
        obj = Myusr.objects.get(user=request.user)
        l=obj.level1
        i=0
        if l==1:
            j=21
        if l==2:
            j=26
        if l==3:
            j=31
        choice = request.POST.getlist('option')
        for c in choice:
            if Quiz.objects.filter(answer=choice[i]).filter(numberr=j):
                total_score = total_score + 1
            i=i+1
            j=j+1
        cat=1
        if total_score>=3:
            cl=Myusr.objects.get(user=request.user)
            cll=cl.level1
            if cll==1:
                if total_score>cl.score1:
                    cl.score1=total_score
                else:
                    cl.score1 = cl.score1+total_score
            if cll==2:
                if total_score>cl.score11:
                    cl.score11=total_score
                else:
                    cl.score11 = cl.score11+total_score
            if cll==3:
                if total_score>cl.score12:
                    cl.score12=total_score
                else:
                    cl.score12 = cl.score12+total_score
            cl.totals = cl.score1 + cl.score11 + cl.score12
            cl.level1=cl.level1+1
            lvl=1
            if cl.level1==4:
                cl.level1=0
                end1=1
                lvl=0

            cl.save()
            return render(request,'randomq/display.html',{'total_score':total_score,'end1':end1,'lvl':lvl,'cll':cll,'cat':cat})
        if total_score<3:
            pl = 1
            cl=Myusr.objects.get(user=request.user)
            cll=cl.level1
            if cll==1:
                cl.score1=total_score
            if cll==2:
                cl.score11=total_score
            if cll==3:
                cl.score12=total_score
            cl.totals=cl.score1+cl.score11+cl.score12
            cl.save()
            return render(request,'randomq/display.html',{'total_score':total_score,'pl':pl,'cll':cll,'cat':cat})



    if category=='3':
        end3=0
        obj = Myusr.objects.get(user=request.user)
        l=obj.level3
        i=0
        if l==1:
            j=11
        if l==2:
            j=56
        if l==3:
            j=61
        choice = request.POST.getlist('option')
        for c in choice:
            if Quiz.objects.filter(answer=choice[i]).filter(numberr=j):
                total_score = total_score + 1
            i=i+1
            j=j+1
        cat=3
        if total_score>=3:
            cl=Myusr.objects.get(user=request.user)
            cll=cl.level3
            if cll==1:
                if total_score>cl.score3:
                    cl.score3=total_score
                else:
                    cl.score3 = cl.score3+total_score
            if cll==2:
                if total_score>cl.score31:
                    cl.score31=total_score
                else:
                    cl.score31 = cl.score31+total_score
            if cll==3:
                if total_score>cl.score32:
                    cl.score32=total_score
                else:
                    cl.score32 = cl.score32+total_score
            cl.totals3 = cl.score3 + cl.score31 + cl.score32
            cl.level3=cl.level3+1
            lvl=1
            if cl.level3==4:
                cl.level3=0
                end3=1
                lvl=0
            cl.save()
            cll=cll+1
            return render(request,'randomq/display.html',{'total_score':total_score,'end3':end3,'lvl':lvl,'cll':cll,'cat':cat})
        if total_score<3:
            pl = 1
            cl=Myusr.objects.get(user=request.user)
            cll=cl.level3
            if cll==1:
                cl.score3=total_score
            if cll==2:
                cl.score31=total_score
            if cll==3:
                cl.score32=total_score
            cl.totals3=cl.score3+cl.score31+cl.score32
            cl.save()
            return render(request,'randomq/display.html',{'total_score':total_score,'pl':pl,'cll':cll,'cat':cat})

    if category=='4':
        end4=0
        obj = Myusr.objects.get(user=request.user)
        l=obj.level4
        i=0
        if l==1:
            j=1
        if l==2:
            j=36
        if l==3:
            j=41
        choice = request.POST.getlist('option')
        for c in choice:
            if Quiz.objects.filter(answer=choice[i]).filter(numberr=j):
                total_score = total_score + 1
            i=i+1
            j=j+1
        cat=4
        if total_score>=3:
            cl=Myusr.objects.get(user=request.user)
            cll=cl.level4
            if cll==1:
                if total_score>cl.score4:
                    cl.score4=total_score
                else:
                    cl.score4 = cl.score4+total_score
            if cll==2:
                if total_score>cl.score41:
                    cl.score41=total_score
                else:
                    cl.score41 = cl.score41+total_score
            if cll==3:
                if total_score>cl.score42:
                    cl.score42=total_score
                else:
                    cl.score42 = cl.score42+total_score
            cl.totals4 = cl.score4 + cl.score41 + cl.score42
            cl.level4=cl.level4+1
            lvl=1
            if cl.level4==4:
                cl.level4=0
                end4=1
                lvl=0
            cl.save()
            cll=cll+1
            return render(request,'randomq/display.html',{'total_score':total_score,'end4':end4,'lvl':lvl,'cll':cll,'cat':cat})
        if total_score<3:
            pl=1
            cl=Myusr.objects.get(user=request.user)
            cll=cl.level4
            if cll==1:
                cl.score4=total_score
            if cll==2:
                cl.score41=total_score
            if cll==3:
                cl.score42=total_score
            cl.totals4=cl.score4+cl.score41+cl.score42
            cl.save()
            return render(request,'randomq/display.html',{'total_score':total_score,'pl':pl,'cll':cll,'cat':cat})

def letter(request):
    return render(request,'randomq/letter.html')
def bas(request):
    return render(request,'randomq/bas.html')
def leader(request):
    if not request.user.is_authenticated():
        return render(request,'homepage/login.html')
    else:
        ob=Myusr.objects.get(user=request.user)
        if ob.house=='0':
            f=1
            return render(request,'randomq/basic.html',{'f':f})
        else:
            choice=request.POST.get('option')
            r=0
            if choice=='4':
                b=0
                c=0
                d=0
                e=0
                a=1
                r=1
                ob=Myusr.objects.get(user=request.user)
                h=ob.house
                obje = Myusr.objects.filter(house=h).order_by('-totals4')
                for o in obje:
                    o.rank=r
                    o.save()
                    r=r+1
                context = {'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'obje': obje, 'r': r,'ob':ob}
                return render(request, 'randomq/leader.html', context)
            elif choice=='3':
                a=0
                c=0
                d=0
                e=0
                b=1
                r=1
                ob=Myusr.objects.get(user=request.user)
                h=ob.house
                obje = Myusr.objects.filter(house=h).order_by('-totals3')
                for o in obje:
                    o.rank=r
                    o.save()
                    r=r+1
                context = {'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'obje': obje, 'r': r,'ob':ob}
                return render(request, 'randomq/leader.html', context)

            elif choice=='2':
                a=0
                b=0
                d=0
                e=0
                c=1
                r=1
                ob=Myusr.objects.get(user=request.user)
                h=ob.house
                obje = Myusr.objects.filter(house=h).order_by('-totals2')
                for o in obje:
                    o.rank=r
                    o.save()
                    r=r+1
                context = {'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'obje': obje, 'r': r,'ob':ob}
                return render(request, 'randomq/leader.html', context)

            elif choice=='1':
                a=0
                b=0
                c=0
                e=0
                d=1
                r=1
                ob=Myusr.objects.get(user=request.user)
                h=ob.house
                obje = Myusr.objects.filter(house=h).order_by('-totals')
                for o in obje:
                    o.rank=r
                    o.save()
                    r=r+1
                context = {'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'obje': obje, 'r': r,'ob':ob}
                return render(request, 'randomq/leader.html', context)

            else:
                a=0
                b=0
                c=0
                d=0
                e=1
                r=1
                ob=Myusr.objects.get(user=request.user)
                h=ob.house
                obje = Myusr.objects.filter(house=ob.house)
                for g in obje:
                    g.grandtotal=g.totals3+g.totals4+g.totals2+g.totals
                    g.save()
                obje = Myusr.objects.filter(house=h).order_by('-grandtotal')
                for o in obje:
                    o.rank=r
                    o.save()
                    r=r+1
                context={'a':a,'b':b,'c':c,'d':d,'e':e,'obje':obje,'r':r,'ob':ob}
                return render(request,'randomq/leader.html',context)
def visitor(request):
    total_score=0
    choice = request.POST.getlist('option')
    k=0
    i=0
    j=71
    for c in choice:
        if c=='4':
            print("hey")
        else:
            if Quiz.objects.filter(answer=choice[i]).filter(numberr=j):
                total_score=total_score+1
        j=j+1
        i=i+1
    return render(request,'randomq/visit.html',{'total_score':total_score})
def visit(request):
    q1 = Quiz.objects.get(numberr=71)
    q2 = Quiz.objects.get(numberr=72)
    q3 = Quiz.objects.get(numberr=73)
    q4 = Quiz.objects.get(numberr=74)
    q5 = Quiz.objects.get(numberr=75)
    context={'q1':q1,'q2':q2,'q3':q3,'q4':q4,'q5':q5}
    return render(request,'randomq/visitor.html',context)
def level(request,cll):
    obj=Myusr.objects.get(user=request.user)
    print(obj)
    p=cll
    if p=='1':
        o = obj.level1
        if o==1:
            q1 = Quiz.objects.get(numberr=21)
            q2 = Quiz.objects.get(numberr=22)
            q3 = Quiz.objects.get(numberr=23)
            q4 = Quiz.objects.get(numberr=24)
            q5 = Quiz.objects.get(numberr=25)
            context = {'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4, 'q5': q5, 'cll': cll}
            return render(request, 'randomq/level.html', context)
        if o==2:
            q1 = Quiz.objects.get(numberr=26)
            q2 = Quiz.objects.get(numberr=27)
            q3 = Quiz.objects.get(numberr=28)
            q4 = Quiz.objects.get(numberr=29)
            q5 = Quiz.objects.get(numberr=30)
            context = {'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4, 'q5': q5, 'cll': cll}
            return render(request, 'randomq/level.html', context)
        if o==3:
            q1 = Quiz.objects.get(numberr=31)
            q2 = Quiz.objects.get(numberr=32)
            q3 = Quiz.objects.get(numberr=33)
            q4 = Quiz.objects.get(numberr=34)
            q5 = Quiz.objects.get(numberr=35)
            context = {'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4, 'q5': q5, 'cll': cll}
            return render(request, 'randomq/level.html', context)


    if p=='4':
        obj = Myusr.objects.get(user=request.user)
        cll=4
        o = obj.level4
        if o==1:
            q1 = Quiz.objects.get(numberr=1)
            q2 = Quiz.objects.get(numberr=2)
            q3 = Quiz.objects.get(numberr=3)
            q4 = Quiz.objects.get(numberr=4)
            q5 = Quiz.objects.get(numberr=5)
            context = {'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4, 'q5': q5, 'cll': cll}
            return render(request, 'randomq/level.html', context)

        if o==2:
            print ("lev1")
            q1 = Quiz.objects.get(numberr=36)
            q2 = Quiz.objects.get(numberr=37)
            q3 = Quiz.objects.get(numberr=38)
            q4 = Quiz.objects.get(numberr=39)
            q5 = Quiz.objects.get(numberr=40)
            context = {'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4, 'q5': q5, 'cll': cll}
            return render(request, 'randomq/level.html', context)
        if o==3:
            q1 = Quiz.objects.get(numberr=41)
            q2 = Quiz.objects.get(numberr=42)
            q3 = Quiz.objects.get(numberr=43)
            q4 = Quiz.objects.get(numberr=44)
            q5 = Quiz.objects.get(numberr=45)
            context = {'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4, 'q5': q5, 'cll': cll}
            return render(request, 'randomq/level.html', context)
    if p=='2':
        obj = Myusr.objects.get(user=request.user)
        cll=2
        o = obj.level2

        if o==1:
            q1 = Quiz.objects.get(numberr=16)
            q2 = Quiz.objects.get(numberr=17)
            q3 = Quiz.objects.get(numberr=18)
            q4 = Quiz.objects.get(numberr=19)
            q5 = Quiz.objects.get(numberr=20)
            context = {'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4, 'q5': q5, 'cll': cll}
            return render(request, 'randomq/level.html', context)

        if o==2:
            q1 = Quiz.objects.get(numberr=46)
            q2 = Quiz.objects.get(numberr=47)
            q3 = Quiz.objects.get(numberr=48)
            q4 = Quiz.objects.get(numberr=49)
            q5 = Quiz.objects.get(numberr=50)
            context = {'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4, 'q5': q5, 'cll': cll}
            return render(request, 'randomq/level.html', context)
        if o==3:
            q1 = Quiz.objects.get(numberr=51)
            q2 = Quiz.objects.get(numberr=52)
            q3 = Quiz.objects.get(numberr=53)
            q4 = Quiz.objects.get(numberr=54)
            q5 = Quiz.objects.get(numberr=55)
            context = {'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4, 'q5': q5, 'cll': cll}
            return render(request, 'randomq/level.html', context)
    if p=='3':
        obj = Myusr.objects.get(user=request.user)
        cll=3
        o = obj.level3

        if o==1:
            q1 = Quiz.objects.get(numberr=11)
            q2 = Quiz.objects.get(numberr=12)
            q3 = Quiz.objects.get(numberr=13)
            q4 = Quiz.objects.get(numberr=14)
            q5 = Quiz.objects.get(numberr=15)
            context = {'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4, 'q5': q5, 'cll': cll}
            return render(request, 'randomq/level.html', context)

        if o==2:
            q1 = Quiz.objects.get(numberr=56)
            q2 = Quiz.objects.get(numberr=57)
            q3 = Quiz.objects.get(numberr=58)
            q4 = Quiz.objects.get(numberr=59)
            q5 = Quiz.objects.get(numberr=60)
            context = {'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4, 'q5': q5, 'cll': cll}
            return render(request, 'randomq/level.html', context)
        if o==3:
            q1 = Quiz.objects.get(numberr=61)
            q2 = Quiz.objects.get(numberr=62)
            q3 = Quiz.objects.get(numberr=63)
            q4 = Quiz.objects.get(numberr=64)
            q5 = Quiz.objects.get(numberr=65)
            context = {'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4, 'q5': q5, 'cll': cll}
            return render(request, 'randomq/level.html', context)

def lcal(request,cll):
    if cll=='5':
        j=66
        i=0
        total_score = 0
        choice = request.POST.getlist('option')
        for c in choice:
            if c == '4':
                print("hey")
            else:
                if Quiz.objects.filter(answer=choice[i]).filter(numberr=j):
                    total_score = total_score + 1
            j = j + 1
            i = i + 1
            ob=Myusr.objects.get(user=request.user)
            ob.bonus=total_score
            ob.grandtotal=ob.grandtotal+ob.bonus
            ob.save()
        return render(request,'randomq/dis.html',{'total_score':total_score})




