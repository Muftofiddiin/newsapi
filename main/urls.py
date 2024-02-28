from django.urls import path
from .views import *
urlpatterns = [
    path('login/', login_view, name='login'),
    path('get-category/',get_category_view),
    path('get-user/',get_user_view),
    path('get-post/',get_posts_view),
    path('get-topposts/',get_topposts_view),
    path('get-relatedposts/',get_relatedposts_view),
    path('get-video/', get_video_view),
    path('get-postdetail/', get_postdetail_view),
    path('get-psotcategory/', get_postcategory_view),
    path('get_aboutus/',get_aboutus_view),
    path('get_megainfo/',get_megainfo_view),
    path('get_megateam/',get_megateam_view),
    path('get_mega/',get_mega_view),
    path('get_comments/',get_comments_view),
    path('get_userposts/',get_userposts_view),
    path('send-post/', SendPost.as_view()),
    path('send-video/', SendVideo.as_view()),
]
