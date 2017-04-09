from django.http import Http404, HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404,redirect
from django.views import generic

from . models import ForumDB, ThreadDB,Mypost,Report
from homepage.models import Myusr

from . forms import ForumDBForm, ThreadDBForm

def index(request):
    if not request.user.is_authenticated():
        return render(request, 'homepage/login.html')
    else:

        h=Myusr.objects.get(user=request.user)
        home=h.house
        forums = ForumDB.objects.filter(house=home)
        query = request.GET.get("q")
        threads = ThreadDB.objects.all()
        for f in forums:
            th=ThreadDB.objects.filter(forum_no=f)
            counter = 0
            for i in th:
                if i.flag == 0:
                    counter = counter + 1
            f.count=counter
            f.save()
        return render(request, 'forums/index.html', {'forums': forums, 'threads': threads})


def detail(request, forum_id):
    if not request.user.is_authenticated():
        return render(request, 'homepage/login.html')
    else:

        forum = get_object_or_404(ForumDB, pk=forum_id)
        thread = ThreadDB.objects.filter(forum_no=forum)

        count = 0
        for i in thread:
            if i.flag==0:
                count = count + 1

        forum.count = count
        forum.save()
        return render(request, 'forums/detail.html', {'forum': forum, 'counter': count})


def create_forum(request):

    if not request.user.is_authenticated():
        return render(request, 'homepage/login.html')
    else:
        ob=Myusr.objects.get(user=request.user)
        if ob.house=='0':
            f1=1
            return render(request,'randomq/basic.html',{'f1':f1})

        else:

            form = ForumDBForm(request.POST or None, request.FILES or None)
            cf=0
            t=ForumDB.objects.all()
            for f in t:
                cf=cf+1
            if form.is_valid():
                us=Myusr.objects.get(user=request.user)
                forum = form.save(commit=False)
                current_user = request.user
                forum.user_name = current_user
                forum.fid=cf
                forum.house=us.house
                forum.save()
                return render(request, 'forums/detail.html', {'forum': forum})
            context = {
                "form": form,
            }
            return render(request, 'forums/create_forum.html', context)


def create_post(request, forum_id):

    if not request.user.is_authenticated():
        return render(request, 'homepage/login.html')
    else:

        form = ThreadDBForm(request.POST or None, request.FILES or None)
        forum = get_object_or_404(ForumDB, pk=forum_id)
        co=forum.fid

        thread = ThreadDB.objects.filter(forum_no=forum)
        cf=0
        t=ThreadDB.objects.all()
        for f in t:
            cf=cf+1
        counter = 0
        for i in thread:
            counter = counter + 1
        if form.is_valid():
            forum_posts = forum.threaddb_set.all()

            po = form.save(commit=False)
            po.forum_no = forum
            current_user = request.user

            po.user_name = current_user
            po.foid=co
            po.count = (int)(po.count + 1)
            counter = counter + 1
            cf=cf+1
            po.postid=cf
            po.save()
            return render(request, 'forums/detail.html', {'forum': forum, 'counter': counter})
        context = {
            'forum': forum,
            'form': form,
            "counter": counter,
        }
        return render(request, 'forums/create_post.html', context)


def posts(request, filter_by):

    if not request.user.is_authenticated():
        return render(request, 'homepage/login.html')
    else:

        try:
            post_ids = []
            for forum in ForumDB.objects.filter(user=request.user):
                for post in forum.threaddb_set.all():
                    post_ids.append(post.pk)
            users_posts = ThreadDB.objects.filter(pk__in=post_ids)

        except ForumDB.DoesNotExist:
            users_posts = []
        return render(request, 'forums/posts.html', {
            'post_list': users_posts,
            'filter_by': filter_by,
        })
def delet(request,ide):
    d=ide
    ob=ThreadDB.objects.get(postid=ide)
    idf=ob.foid
    forum=ForumDB.objects.get(fid=idf)
    thread = ThreadDB.objects.filter(forum_no=forum)
    count = 0
    for i in thread:
        count = count + 1
    u=Report.objects.filter(rid=d).filter(user=request.user)
    c=0
    cd=0
    for ids in u:
        c=c+1
    if c==0:
        u = Report()
        u.user = request.user
        u.rid=d
        u.save()
        ob.dislike = ob.dislike + 1
        ob.save()
        cd = ob.dislike
    if cd==5:
        ob.flag=1
        ob.save()
    context = {'counter': count, 'forum': forum}
    return render(request, 'forums/detail.html', context)

def like(request,idy):
    d=idy
    ob=ThreadDB.objects.get(postid=d)
    idf=ob.foid
    forum=ForumDB.objects.get(fid=idf)
    thread = ThreadDB.objects.filter(forum_no=forum)
    count = 0
    for i in thread:
        count = count + 1
    #forum=ForumDB.objects.get(user_name=request.user)
    u=Mypost.objects.filter(pid=d).filter(user=request.user)
    c=0
    for ids in u:
        c=c+1
    if c==0:
        u = Mypost()
        u.user = request.user
        u.pid=d
        u.save()
        ob.like = ob.like + 1
        ob.save()
    context={'counter':count,'forum':forum}
    return render(request,'forums/detail.html',context)

def delete(request,idee):
    idea=idee
    c=0
    ob=ThreadDB.objects.filter(postid=idea).filter(user_name=request.user)
    """idf=ob.foid
    forum=ForumDB.objects.filter(fid=idf)
    thread = ThreadDB.objects.filter(forum_no=forum)
    count = 0
    for i in thread:
        count = count + 1
"""
    for o in ob:
        c=c+1
        idf=o.foid
        o.delflag=1
        o.flag=1
        o.save()
        forum=ForumDB.objects.get(fid=idf)
        thread = ThreadDB.objects.filter(forum_no=forum)
        count = 0
        for i in thread:
            count = count + 1

        context = {'counter': count, 'forum': forum}
        return render(request, 'forums/detail.html', context)
    ob = ThreadDB.objects.get(postid=idee)
    idf = ob.foid
    forum = ForumDB.objects.get(fid=idf)
    thread = ThreadDB.objects.filter(forum_no=forum)
    count = 0
    for i in thread:
        count = count + 1
    context = {'counter': count, 'forum': forum}
    return render(request, 'forums/detail.html', context)

    #return HttpResponse("h")


