from rest_framework.serializers import ModelSerializer
from .models import *


class CategorySerializer(ModelSerializer):
    class Meta :
        model = Category
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PostsSerializer(ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'


class RelatedPostsSerializer(ModelSerializer):
    class Meta:
        model = Related_Posts
        fields = '__all__'


class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post_Detail
        fields = '__all__'


class PostCategorySerializer(ModelSerializer):
    class Meta:
        model = Post_Category
        fields = '__all__'


class AboutUsSerializer(ModelSerializer):
    class Meta:
        model = About_Us
        fields = '__all__'


class MegaInfoSerializer(ModelSerializer):
    class Meta:
        model = Mega_Info
        fields = '__all__'


class MegaTeamSerializer(ModelSerializer):
    class Meta:
        model = Mega_Team
        fields = '__all__'


class MegaSerializer(ModelSerializer):
    class Meta:
        model = Mega
        fields = '__all__'


class CommentsSerializer(ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'


class UserPostsSerializer(ModelSerializer):
    class Meta:
        model = User_Posts
        fields = '__all__'


class UserSendPostSerializer(ModelSerializer):
    class Meta:
        model = User_SendPost
        fields = '__all__'


class UserSendVideoSerializer(ModelSerializer):
    class Meta:
        model = User_SendVideo
        fields = '__all__'









