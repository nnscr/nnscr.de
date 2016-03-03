from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin


class AdminSite(admin.AdminSite):
    def __init__(self, name="admin"):
        self.__contexts = {"index": {}}
        self.extra_urls = []
        super(AdminSite, self).__init__(name)

    def get_urls(self):
        urls = super(AdminSite, self).get_urls()
        urls += self.extra_urls
        return urls

    def index(self, request, extra_context=None):
        context = {}
        context.update(self.__contexts["index"])
        context.update(extra_context or {})
        return super(AdminSite, self).index(request, context)

    def add_context(self, page, key, value):
        self.__contexts[page][key] = value

site = AdminSite()
site.register(User, UserAdmin)
site.register(Group, GroupAdmin)
