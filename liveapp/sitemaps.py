from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class StaticViewSitemap(Sitemap):
    priority = 1.0  # Home page is usually very important
    changefreq = 'monthly' # adjust as needed

    def items(self):
        return ['home'] # the name of your home view

    def location(self, item):
        return reverse(item)