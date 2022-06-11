from django.contrib import admin
from .models import Article,tags,MoringaMerch



class ArticleAdmin(admin.ModelAdmin):    
    filter_horizontal =('tags',)
    list_display = ('title', 'editor')

#add models to our Admin page

admin.site.register(tags)
admin.site.register(Article, ArticleAdmin)
admin.site.register(MoringaMerch)
admin.site.site_header='News Admin Area'
admin.site.site_title='CF'
admin.site.index_title='Welcome Chemu'
