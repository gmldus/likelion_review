from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from .models import Post
# Create your views here.
def main(request):
    posts = Post.objects
    return render(request, 'main.html', {'posts': posts})

def show(request, post_id):
    post = get_object_or_404(Post, pk = post_id )
    return render(request, 'show.html', {'post': post})

def new(request):
    return render(request, 'new.html')

def postcreate(request):
    if request.method =='POST': # POST 방식으로 요청이 들어왔을 때
        form = PostForm(request.POST, request.FILES) 
        if form.is_valid(): 
            post = form.save(commit=False) 
            post.save() 
            return redirect('main') #새글 등록한 후 메인화면으로 돌아옴 
    else: # GET 방식으로 요청이 들어왔을 때
        form = PostForm()
        return render(request,'new.html', {'form': form})

'''def upload_pic(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            m = ExampleModel.objects.get(pk=course_id)
            m.model_pic = form.cleaned_data['image']
            m.save()
            return HttpResponse('image upload success')
    return HttpResponseForbidden('allowed only via POST')'''
