from django.contrib import admin
from news.models import Article, Journalist

admin.site.register(Journalist)
admin.site.register(Article)