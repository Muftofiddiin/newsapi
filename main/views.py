from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from .models import *
from rest_framework.response import Response
from .serializer import *
from rest_framework.generics import CreateAPIView , ListCreateAPIView , UpdateAPIView


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                error_message = "Invalid username or password. Please try again."
                return render(request,  {'error_message': error_message})
        else:
            error_message = "Invalid username or password. Please try again."
            return render(request,  {'error_message': error_message})
    else:
        form = AuthenticationForm()
        return render(request, {'form': form})


@api_view(['GET'])
def get_category_view(request):
    category = Category.objects.all
    serialized_data = CategorySerializer(category , many= True).data
    return Response(serialized_data)

@api_view(['GET'])
def get_user_view(request):
    user = User.objects.all()
    serialized_data = UserSerializer(user , many= True).data

    return Response(serialized_data)

@api_view(['GET'])
def get_posts_view(request):
    posts = Posts.objects.all()
    serialized_data = PostsSerializer(posts , many= True).data
    return Response(serialized_data)

@api_view(['GET'])
def get_topposts_view(request):
    posts = Posts.objects.all().order_by('-views')
    serialized_data = PostsSerializer(posts , many= True).data
    return Response(serialized_data)


@api_view(['GET'])
def get_relatedposts_view(request):
    relatedposts = Related_Posts.objects.all()
    serialized_data = RelatedPostsSerializer(relatedposts , many= True).data
    return Response(serialized_data)

@api_view(['GET'])
def get_video_view(request):
    video = Video.objects.all()
    serialized_data = VideoSerializer(video , many= True).data
    return Response(serialized_data)

@api_view(['GET'])
def get_postdetail_view(request):
    pdetail = Post_Detail.objects.all()
    serialized_data = PostDetailSerializer(pdetail , many= True).data
    return Response(serialized_data)

@api_view(['GET'])
def get_postcategory_view(request):
    pcat = Post_Category.objects.all()
    serialized_data = PostCategorySerializer(pcat , many= True).data
    return Response(serialized_data)


@api_view(['GET'])
def get_aboutus_view(request):
    aboutus = About_Us.objects.last()
    serialized_data = AboutUsSerializer(aboutus)
    return Response(serialized_data)

@api_view(['GET'])
def get_megainfo_view(request):
    megainfo = Mega_Info.objects.last()
    serialized_data = MegaInfoSerializer(megainfo)
    return Response(serialized_data)

@api_view(['GET'])
def get_megateam_view(request):
    megateam = Mega_Team.objects.all()
    serialized_data = MegaTeamSerializer(megateam , many=True)
    return Response(serialized_data)

@api_view(['GET'])
def get_mega_view(request):
    mega = Mega.objects.all()
    serialized_data = MegaSerializer(mega ,many=True)
    return Response(serialized_data)


@api_view(['GET'])
def get_comments_view(request):
    comments = Comments.objects.all()
    serialized_data = CommentsSerializer(comments, many=True)
    return Response(serialized_data)


@api_view(['GET'])
def get_userposts_view(request):
    uposts = User_Posts.objects.all()
    serialized_data = UserPostsSerializer(uposts, many=True)
    return Response(serialized_data)


class SendPost(CreateAPIView):
    spost = User_SendPost.objects.all()
    serializer_class = UserSendPostSerializer

class SendVideo(CreateAPIView):
    svideo = User_SendVideo.objects.all()
    serializer_class = UserSendVideoSerializer




# @api_view(['POST'])
# def get_usersendpost_view(request):
#
#
#
# @api_view(['POST'])
# def get_usersendvideo_view(request):




