from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ( TemplateView,ListView,
                                    DetailView,CreateView,
                                    UpdateView,DeleteView,
                                     )
from blog.forms import PostForm,CommentForm
from blog.models import Post,Comment
from django.contrib.messages import constants as message_constants
from django.contrib import messages


# MESSAGE_LEVEL = message_constants.SUCCESS

# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.localtime()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'post_detail.html'

##########################
    form_class = PostForm
    model = Post
############################

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = '/post_detail.html'
    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('posts_list')

class DraftListView(LoginRequiredMixin,ListView):
    ############################
    login_url='/login/'
    redirect_field_name = '/draf_list.html'
    ################################
    model = Post
    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')


#############################################################################################################################################
#############################################################################################################################################

@login_required
def publish_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    post.save()
    return redirect('home')

def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)

    if request.method=='POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post= post
            comment.save()
            messages.warning(request,'Comment Posted successfully !')
            return redirect('post_detail',pk=post.pk)
        else:
            messages.warning(request,'Looks Not Everything Perfect, Please Check !')  #,extra_tags='alert'
    else :
        form = CommentForm()
        return render(request,'comment_form.html',{'form':form})

@login_required
def approve_comment(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

@login_required
def remove_comment(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)
