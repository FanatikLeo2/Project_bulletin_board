from django.urls import path

from .views import PostList, PostCreate, ReplyCreate, PostUpdate, PostDelete, ReplyList, confirm_reply, reject_reply
from .views import index

urlpatterns = [
   path('', PostList.as_view(), name='post_list'),
   path('create/', PostCreate.as_view(), name='create_post'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('<int:pk>/create_reply', ReplyCreate.as_view(), name='reply_create'),
   path('replies/', ReplyList.as_view(), name='reply_list'),
   path('replies/<int:pk>/confirm', confirm_reply, name='confirm_reply'),
   path('replies/<int:pk>/reject', reject_reply, name='reject_reply'),
   path('index/', index),
]