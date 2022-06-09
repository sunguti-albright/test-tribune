from django.contrib import admin
from .models import Article,tags, NewsLetterRecipients

# Register your models here.
# allows us to customize models on the admin page
class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(tags)
admin.site.register(NewsLetterRecipients)