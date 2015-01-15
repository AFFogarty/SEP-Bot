from django.contrib import admin
from sep_search.models.article import Article
from sep_search.models.author import Author


def reindex_in_solr(modeladmin, request, queryset):
    for item in queryset:
        item.save()

reindex_in_solr.short_description = "ReIndex in Solr"


class AuthorAdmin(admin.ModelAdmin):
    actions = [reindex_in_solr]


class ArticleAdmin(admin.ModelAdmin):
    actions = [reindex_in_solr]


admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
