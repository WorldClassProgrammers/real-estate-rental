from django.contrib import admin

from .models import Condo, Room, Owner


class RoomInline(admin.TabularInline):
    model = Room
    extra = 1


class CondoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [
                'name',
                'description',
                'number_of_floors',
            ]
        }),
        ('Admin only', {
            'fields': [
                'juristic_persons_number',
                'common_fee_account',
            ],
        }),
        ('amenities information', {
            'fields': [
                'elevator',
                'parking_lot',
                'cctv',
                'security',
                'wifi',
                'swimming_pool',
                'sauna',
                'garden',
                'playground',
                'gym',
                'shop_on_premise',
                'restaurant_on_premise',
            ],
        }),
    ]
    inlines = [RoomInline]
    list_display = (
        'name',
        'juristic_persons_number',
        'common_fee_account',
    )
    search_fields = ['name']


class RoomAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [
                'condo',
                'owner',
                'title',
                'description',
                'still_on_contract',
                'price_for_rent',
                'price_for_sell',

            ]
        }),
        ('Room information', {
            'fields': [
                'number',
                'floor_number',
                'number_of_bedroom',
                'number_of_bathroom',
                'area',
            ],
        }),
    ]
    list_display = (
        'condo',
        'number',
        'still_on_contract',
        # 'contract_over',
    )
    list_filter = ['still_on_contract']
    search_fields = ['condo',
                     'title',
                     'number',
                     'area',
                     ]


class OwnerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [
                'name',
                'email',
                'line_id',
                'phone_number',
            ]
        }),
    ]
    list_display = (
        'name',
        'email',
        'phone_number',
    )
    search_fields = ['name']


admin.site.register(Condo, CondoAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Owner, OwnerAdmin)
