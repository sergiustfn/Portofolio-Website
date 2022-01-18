from django.contrib import admin


from projects.models import Project, ProjectTag, Review, FilesAdmin

admin.site.register(Project)
admin.site.register(ProjectTag)
admin.site.register(Review)
admin.site.register(FilesAdmin)

