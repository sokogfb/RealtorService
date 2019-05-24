from django.contrib import admin

from .models import Listing
# Register your models here.

#for customizing admin area
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_publishd', 'price', 'list_date', 'realtor')
    # patern of desplaying

    list_display_links = ('id', 'title')
    # can go to special listing by clicking on [id, title]

    list_filter = ('realtor',)
    # filtering data by key => realtor

    list_editable = ('is_publishd',)
    # for changing some values by hand

    search_fields = ('title', 'price', 'zipcode', 'address', 'city', 'description')
    # can find fields by these keys

    list_per_page = 20
    # pagination

admin.site.register(Listing, ListingAdmin)
