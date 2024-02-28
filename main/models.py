from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    image =  models.ImageField()

class User(models.Model):
    photo = models.ImageField(blank=True , null=True)
    name =  models.CharField(max_length=255)
    date =  models.DateField(auto_now_add=True)


class Posts(models.Model):
    photo = models.ImageField(blank=True , null=True)
    title = models.CharField(max_length=255)
    text =  models.TextField()
    user =  models.ForeignKey(User , on_delete=models.CASCADE)
    date = models.DateTimeField()
    views = models.IntegerField()
    likes = models.IntegerField()
    comments = models.IntegerField()
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    rel_posts = models.ManyToManyField('Related_Posts')

class Related_Posts(models.Model):
    photo = models.ImageField()
    title = models.CharField(max_length=255)
    text =  models.TextField()
    user =  models.ForeignKey(User, on_delete=models.CASCADE)


class Video(models.Model):
    video = models.FileField()
    title = models.CharField(max_length=255)
    text =  models.TextField()


class Post_Detail(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    text = models.TextField()
    advertisement = models.ImageField()
    tags = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Post_Category(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)


class About_Us(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    video = models.URLField(blank=True , null=True)


class Mega_Info(models.Model):
    email = models.EmailField(blank=True , null=True)
    number = models.IntegerField()
    fax = models.IntegerField()
    address = models.CharField(max_length=255)
    map = models.URLField(blank=True, null=True)


class Mega_Team(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    occupation = models.CharField(max_length=50)


class Mega(models.Model):
    categories = models.ManyToManyField('Category')
    socials = models.URLField(blank=True , null=True)

class Comments(models.Model):
    username = models.CharField(max_length=255)
    comment = models.TextField()

class User_Posts(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    posts = models.ManyToManyField('Posts')


class User_SendPost(models.Model):
    title = models.CharField(max_length=255)
    tags = models.ForeignKey(Category , on_delete=models.CASCADE)
    explanation = models.TextField()
    image = models.FileField()


class User_SendVideo(models.Model):
    title = models.CharField(max_length=255)
    tags = models.ForeignKey(Category , on_delete=models.CASCADE)
    explanation = models.TextField()
    url = models.URLField(blank=True , null=True)
