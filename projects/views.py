import os.path

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from projects.models import Project, FilesAdmin, Images
from django.http import HttpResponse, Http404


def homepage(request):
    if request.method == "POST":
        name = request.POST['Name']
        email = request.POST['Email']
        subject = request.POST['Subject']
        message = f" Name: {name} \n \n Email: {email}" + '\n' + '\n' + request.POST['message']

        send_mail(
            subject,
            message,
            'helpasoul24@gmail.com',
            ['m.sergiu01@gmail.com'],
        )
        return render(request, 'index.html', {'subject': subject})

    context = {'file': FilesAdmin.objects.all()}

    return render(request, 'index.html', context)


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='application/adminupload')
            response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response
    raise Http404


def project_detail(request, pk):
    project = Project.objects.get(id=pk)
    images = Images.objects.filter(project_id=pk)

    context = {'project': project, 'images': images}
    return render(request, 'single-blog.html', context)


def project_list(request):
    projects = Project.objects.all()
    context = {'projects': projects}

    return render(request, 'blog.html', context)
