from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(BlogPost)

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'timestamp')
    readonly_fields = ('name', 'email', 'subject', 'message', 'timestamp')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        custom_urls = [
            path('delete_all/', self.admin_site.admin_view(self.delete_all_messages), name='delete_all_messages'),
        ]
        return custom_urls + urls

    def delete_all_messages(self, request):
        if request.method == 'POST':
            ContactMessage.objects.all().delete()
            self.message_user(request, "All contact messages have been deleted.", level='SUCCESS')
            return redirect('admin:liveapp_contactmessage_changelist') #replace liveapp with your app name

        return render(request, 'admin/delete_all_messages.html')

admin.site.register(ContactMessage, ContactMessageAdmin)