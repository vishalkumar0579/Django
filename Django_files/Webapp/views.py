from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Create your views here.
def FileUpload(request):
    if request.method == 'post' and request.FILES['myfile']:
        requested_file = request.FILES['myfile']
        print(requested_file.name)
        print(requested_file.size)
        fs=FileSystemStorage()
        fname=fs.save(requested_file.name,requested_file)
        uf=fs.url(fname)
        return render(request, 'files.html',{'uf':uf})
    return render(request, 'files.html')