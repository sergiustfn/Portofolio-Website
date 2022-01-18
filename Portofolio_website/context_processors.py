from projects.models import Project


def all_projects(request):
    projects = Project.objects.all()

    return {'projects': projects}
