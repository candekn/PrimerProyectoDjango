from django.contrib import admin
from .models import Post
#se utiliza para administrar los modelos que creamos (crear, editar borrar)
admin.site.register(Post)
