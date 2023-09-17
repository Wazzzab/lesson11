from django.contrib import admin
from .models import Advertisement
import datetime


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'author', 'auction', 'price', 'get_updated_at_display']
    list_filter = ['author', 'title']
    actions = ['delete_description', 'make_auction_as_true']

    def get_updated_at_display(self, obj):
        if obj.update_at.date() == datetime.date.today():
            return f'<Сегодня в {obj.update_at.strftime("%H:%M")}>'
        else:
            return obj.update_at.strftime("%Y-%m-%d %H:%M")

    get_updated_at_display.short_description = 'Последнее обновление'
    get_updated_at_display.allow_tags = True

    @admin.action(description="Удалить описание выбранных объектов")
    def delete_description(self, request, queryset):
        queryset.update(text='')

    # noinspection PyMissingOrEmptyDocstring
    @admin.action(description="Включить возможность торга")
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)


admin.site.register(Advertisement, AdvertisementAdmin)
# Register your models here.
