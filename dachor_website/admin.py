from django.contrib import admin

from dachor_website.models import NewsItem


class NewsItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'start', 'end')


admin.site.register(NewsItem, NewsItemAdmin)
