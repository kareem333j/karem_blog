from django.shortcuts import render
from .forms import CommentForm,EditForm,ReportForm
from .models import Comment,Admin,Edit,Report
# Create your views here.

def index(request):
    name = request.POST.get('name')
    image = request.FILES.get('image')
    comment = request.POST.get('comment')
    v_data = Comment(name=name, comment=comment,image=image)
    # check_comment = Comment.objects.all()
    if request.method == "POST":
        if Comment.objects.filter(comment=comment):
            print("error")
        else:
            v_data.save()

    photo_admin = Admin.objects.all()
    return render(request, 'html/index.html',{'comment':CommentForm, 'comments_models':Comment.objects.all(),'adminphoto':photo_admin,'report':ReportForm})



# for admin only

def edit_admin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if Edit.objects.filter(username=username) and Edit.objects.filter(password=password):
        user = True
    else:
        user = False

    x = {
        'edit':EditForm,
        'user':user
    }


    return render(request, 'html/admin.html',x)

def toedit(request):
    objects = Comment.objects.all()
    search = request.GET.get('search')
    activate = request.GET.get('check')
    g = Admin.objects.all()
    editcom = request.POST.get('edit-com')
    s_data= Comment(comment = editcom)
    if request.method == "POST":
        pass

    z = {
        'comments_models':Comment.objects.all(),
        'search':search,
        # 'delete':count
        'comment':CommentForm,
    }
    return render(request, 'html/edit.html',z)


def showComment(request, pk):
    edition = Comment.objects.get(id=pk)
    return render(request, 'html/comment-content.html', {'pk':edition})


# edit comment page

def edit_comment_page(request, pg):
    name = request.POST.get('name')
    comment = request.POST.get('comment')
    activate = request.POST.get('activation')
    time = request.POST.get('time')
    new_image = request.FILES.get('image')
    # image = request.POST.get('image')

    edit_page = Comment.objects.get(id=pg)
    if request.method == "POST":
        ss_data = Comment.objects.filter(id=pg).update(name=name,comment=comment,time=time)
        # s_image = Comment.objects.filter(id = pg).update(image=new_image)
        if activate == "True" or activate == "true":
            Comment.objects.filter(id=pg).delete()
    p = {
        'pg':edit_page,
        'comment':CommentForm
    }

    return render(request, 'html/edit-comment-page.html',p)


