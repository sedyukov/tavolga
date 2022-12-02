from django.contrib import admin

from .models import Number, Authors, Material, News, Contacts


class AuthorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'soname', 'bio', 'link_draft')
    list_display_links = ('name', 'soname')
    search_fields = ('name', 'soname')


class NumberAdmin(admin.ModelAdmin):
    list_display = ('name', 'published', 'draft')
    list_display_links = ('name', 'published', 'draft')
    search_fields = ('name', )


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'auth', 'number', 'draft')
    list_display_links = ('name', 'auth', 'number', 'draft')
    search_fields = ('name', 'auth', 'number')


class NewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'published', 'draft')
    list_display_links = ('name', 'published', 'draft')
    search_fields = ('name', )


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('about', )
    list_display_links = ('about', )
    search_fields = ('about', )


admin.site.register(Number, NumberAdmin)
admin.site.register(Authors, AuthorsAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Contacts, ContactsAdmin)
