from django.contrib import admin
from real_estate_web_application.common.models import CommentModel


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'date', 'property', 'user')
    list_filter = ('property', 'user')
    date_hierarchy = 'date'
    search_fields = ('user',)
    search_help_text = 'Search comment by user.'
    ordering = ('pk',)



