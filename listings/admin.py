from django.contrib import admin

from .models import Listing

#here we can add variables/properties that relates how things are displayed. Here you just define
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id','title')
    #when we use parenteses '' and its only one value then we need to put commer 
    list_filter=('realtor',)
    list_editable=('is_published',)
    search_fields=('title', 'description','address','city','state','zipcode','price')
    list_per_page=25
    
#above you define and bellow you add ,ListingAdmin in order for above to work 
admin.site.register(Listing, ListingAdmin)
