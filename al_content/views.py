from django.shortcuts import render, redirect
from . import forms
from . import models
from django.views import View
# Create your views here.
def createCatagory(request):
    if request.method == 'POST':
        form = forms.catagoryform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = forms.catagoryform()
    return render(request, 'catagory.html', {'form': form})

def createProject(request):
    if request.method == 'POST':
        form = forms.projectform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = forms.projectform()
    return render(request, 'project.html', {'form': form}) 

#upadate cv
def createskill(request):
    if request.method == 'POST':
        form = forms.sakillform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = forms.sakillform()
    return render(request, 'skill.html', {'form': form})
    
def createblog(request):
    if request.method == 'POST':
        form = forms.blogfrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = forms.blogfrom()
    return render(request, 'blog.html', {'form': form})
    
from django.views.generic import DetailView
# class detalils(DetailView):
#     model = models.Projects
#     pk_url_kwarg = 'id'
#     template_name = 'details.html'
#     context_object_name = 'detail'
#     def post(self, request, *args, **kwargs):
#         comment_form = forms.revewfrom(data=self.request.POST)
#         post = self.get_object()
#         if comment_form.is_valid():
#             new_comment = comment_form.save(commit=False)
#             new_comment.post = post
#             new_comment.save()
#         return self.get(request, *args, **kwargs)


#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         post = self.object # post model er abject ekhane store korlem\
#         comments = models.review.objects.all()
#         comment_form=forms.revewfrom()


#         context['comments'] = comments
#         context['comments_form'] = comment_form
#         return context

class detalils(DetailView):
    model = models.Projects
    pk_url_kwarg = 'id'
    template_name = 'details.html'
    context_object_name = 'detail'

    def post(self, request, *args, **kwargs):
        comment_form = forms.revewfrom(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            # Associate the comment with the project
            new_comment.project = post
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        # Fetch all comments related to the current project
        comments = models.review.objects.filter(project=post)
        comment_form = forms.revewfrom()
        context['comments'] = comments
        context['comments_form'] = comment_form
        return context

class CVview(View):
    template_name = 'cv.html'

    def get(self, request):
        form = forms.cvform(instance=request.user)
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        form = forms.cvform(request.POST, instance=request.user)
        if form.is_valid():

            form.save()
            return redirect('home')
        return render(request, self.template_name, {'form': form})

def showBlock(request):
    data = models.blog.objects.all()
    return render(request, 's_blog.html',{'data': data})

def contact(request):
    return render(request, 'contact.html')

def cvx(request):
    data = models.cv.objects.all()
    return render(request, 'myCv.html',{'data': data})

def skilx(request):
    data = models.SkillModel.objects.all()
    return render(request, 's_skil.html',{'data': data})