from django.shortcuts import render,get_object_or_404
from django.http import request,HttpResponse
from django.views import generic
from .models import blog,Comments,Author_bio,User

# Create your views here.

class BlogListView(generic.ListView):

    model=blog

class BlogDetailView(generic.DetailView):
    model=blog

class BloggerListView(generic.ListView):
    model=Author_bio
    template_name="DBlog/author_list.html"

class BloggerDetailView(generic.DetailView):
    model=Author_bio    

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateComment
from django.http import HttpResponseRedirect
from django.urls import reverse

"""
class CommentsCreate(LoginRequiredMixin,CreateView):
    model=Comments
    fields=["user","blog","Comment"]
"""
def CommentsCreate(request,blogid):

    form=CreateComment(request.POST)
    comment=Comments()
    
    if (request.method == 'POST'):
        if(form.is_valid()):
            comment.Comment=form.cleaned_data['comment']
            comment.user=User.get_username()
            comment.blog=blogid
            comment.save()

            return HttpResponseRedirect(reverse('blogs') )


    else:
        form=CreateComment(initial={'comment':'',})


       
    return render(request,'DBlog/comments_form.html',{'form':form,'comment':comment})

    