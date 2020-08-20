
from django.urls import path
import hello.views
urlpatterns = [
     path('', hello.views.home, name='home'),
     path('new',hello.views.new, name="new"),
     path('postcreate',hello.views.postcreate,name="postcreate"),
     path('detail/<int:post_id>', hello.views.detail,name="detail"),
     path('edit/<int:post_id>',hello.views.postedit, name="postedit"),
     path('update/<int:post_id>',hello.views.postupdate,name="postupdate"),
     path('delete/<int:post_id>',hello.views.postdelete,name="postdelete"),
     path('commentcreate/<int:post_id>',hello.views.commentcreate,name="commentcreate"),
     path('commentdelete/<int:post_id>/<int:comment_id>', hello.views.commentdelete, name="commentdelete"),
]
