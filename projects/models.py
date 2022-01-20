from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField()
    date = models.DateTimeField(auto_now_add=True)
    project_tags = models.ManyToManyField('ProjectTag')
    project_link = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title


class ProjectTag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Images(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image_1 = models.ImageField()
    image_2 = models.ImageField()
    Image_3 = models.ImageField()

    def __str__(self):
        return self.project.title


class Review(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    name = models.TextField(max_length=100, null=True, blank=True)
    body = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project.title


class FilesAdmin(models.Model):
    admin_upload = models.FileField(upload_to='media')
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
