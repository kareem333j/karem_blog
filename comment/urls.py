from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
# start my project

urlpatterns = [
    path('', views.index, name='index'),
    path('edit_admin/',views.edit_admin,name='edit_admin'),
    path('toedit/',views.toedit,name='toedit'),
    path('comment-content/<str:pk>', views.showComment,name='showComment'),
    path('edit_comment_page/<str:pg>',views.edit_comment_page,name='edit_comment_page'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
