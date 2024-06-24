from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

######################## User ###########################
@admin.register(ArchimatchUser)
class ArchimatchUserAdmin(UserAdmin):
    list_display = [field.name for field in ArchimatchUser._meta.fields]
    sortable_by = ('id')

@admin.register(Architect)
class ArchitectAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Architect._meta.fields]
    sortable_by = ('id')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Client._meta.fields]
    sortable_by = ('id')

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Admin._meta.fields]
    sortable_by = ('id')

######################## utils ###########################
@admin.register(ArchitectType)
class ArchitectTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ArchitectType._meta.fields]
    sortable_by = ('id')

@admin.register(Need)
class NeedAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Need._meta.fields]
    sortable_by = ('id')

@admin.register(Right)
class RightAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Right._meta.fields]
    sortable_by = ('id')

@admin.register(Subscription)
class Subscription(admin.ModelAdmin):
    list_display = [field.name for field in Subscription._meta.fields]
    sortable_by = ('id')

@admin.register(SubscriptionRequest)
class SubscriptionsRequest(admin.ModelAdmin):
    list_display = [field.name for field in SubscriptionRequest._meta.fields]
    sortable_by = ('id')

@admin.register(ArchiServicetype)
class ArchiServicetype(admin.ModelAdmin):
    list_display = [field.name for field in ArchiServicetype._meta.fields]
    sortable_by = ('id')

@admin.register(ArchiSubscription)
class ArchiSubscription(admin.ModelAdmin):
    list_display = [field.name for field in ArchiSubscription._meta.fields]
    sortable_by = ('id')

@admin.register(BankCard)
class BankCard(admin.ModelAdmin):
    list_display = [field.name for field in BankCard._meta.fields]
    sortable_by = ('id')

@admin.register(Preference)
class Preference(admin.ModelAdmin):
    list_display = [field.name for field in Preference._meta.fields]
    sortable_by = ('id')

@admin.register(Worktype)
class Worktype(admin.ModelAdmin):
    list_display = [field.name for field in Worktype._meta.fields]
    sortable_by = ('id')

@admin.register(Worksurface)
class Worksurface(admin.ModelAdmin):
    list_display = [field.name for field in Worksurface._meta.fields]
    sortable_by = ('id')

@admin.register(Location)
class Location(admin.ModelAdmin):
    list_display = [field.name for field in Location._meta.fields]
    sortable_by = ('id')

@admin.register(Services)
class Services(admin.ModelAdmin):
    list_display = [field.name for field in Services._meta.fields]
    sortable_by = ('id')

@admin.register(Goodtype)
class Goodtype(admin.ModelAdmin):
    list_display = [field.name for field in Goodtype._meta.fields]
    sortable_by = ('id')

@admin.register(Projectbudget)
class Projectbudget(admin.ModelAdmin):
    list_display = [field.name for field in Projectbudget._meta.fields]
    sortable_by = ('id')

@admin.register(Receipt)
class Receipt(admin.ModelAdmin):
    list_display = [field.name for field in Receipt._meta.fields]
    sortable_by = ('id')

@admin.register(Realization)
class Realization(admin.ModelAdmin):
    list_display = [field.name for field in Realization._meta.fields]
    sortable_by = ('id')

@admin.register(RealizationImage)
class RealizationImage(admin.ModelAdmin):
    list_display = [field.name for field in RealizationImage._meta.fields]
    sortable_by = ('id')
    
@admin.register(Otp)
class Otp(admin.ModelAdmin):
    list_display = [field.name for field in Otp._meta.fields]
    sortable_by = ('id')

@admin.register(NeedPieces)
class NeedPieces(admin.ModelAdmin):
    list_display = [field.name for field in NeedPieces._meta.fields]
    sortable_by = ('id')
@admin.register(Devis)
class Devis(admin.ModelAdmin):
    list_display = [field.name for field in Devis._meta.fields]
    sortable_by = ('id')
@admin.register(Selection)
class Selection(admin.ModelAdmin):
    list_display = [field.name for field in Selection._meta.fields]
    sortable_by = ('id')
@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]
    sortable_by = ('id')
@admin.register(SubCategory)
class SubCategory(admin.ModelAdmin):
    list_display = [field.name for field in SubCategory._meta.fields]
    sortable_by = ('id')
@admin.register(Report)
class Report(admin.ModelAdmin):
    list_display = [field.name for field in Report._meta.fields]
    sortable_by = ('id')
@admin.register(ArchiReport)
class ArchiReport(admin.ModelAdmin):
    list_display = [field.name for field in ArchiReport._meta.fields]
    sortable_by = ('id')
@admin.register(ClientReport)
class ClientReport(admin.ModelAdmin):
    list_display = [field.name for field in ClientReport._meta.fields]
    sortable_by = ('id')

@admin.register(CommentReport)
class CommentReport(admin.ModelAdmin):
    list_display = [field.name for field in CommentReport._meta.fields]
    sortable_by = ('id')

@admin.register(Invitation)
class Invitation(admin.ModelAdmin):
    list_display = [field.name for field in Invitation._meta.fields]
    sortable_by = ('id')

@admin.register(Supplier)
class Supplier(admin.ModelAdmin):
    list_display = [field.name for field in Supplier._meta.fields]
    sortable_by = ('id')
@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_display = [field.name for field in Comment._meta.fields]
    sortable_by = ('id')
######################## shared ###########################
@admin.register(ArchitectRequest)
class ArchitectRequestAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name',
                    'phone_number', 'status')

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('id', 'adresse', 'town',
                    'house_type')
    search_fields = ('id', 'adress', 'town')
    sortable_by = ('id', 'adress', 'town')