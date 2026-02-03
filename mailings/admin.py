from django.contrib import admin
from mailings.models import MailingRecipient, Message, Newsletter, AttemptToSend


@admin.register(MailingRecipient)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "full_name", "comment")
    list_filter = ("email",)
    search_fields = ("name", "description")


@admin.register(Message)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "topic")


@admin.register(Newsletter)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "status", "sending_date", "end_date_of_send")


@admin.register(AttemptToSend)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "status", "date_of_attempt")
