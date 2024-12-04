from django.shortcuts import render

# Create your views here.
def CreateBlog(request):
    if request.method == 'POST':
        print(request.POST)
        title = request.POST['title']
        category = request.POST['category']
        description = request.POST['description']
        content = request.POST['content']
        image = request.FILES['image']
        print(title, category, description, content, image)
    return render(request, 'blogmanager/createBlog.html')

