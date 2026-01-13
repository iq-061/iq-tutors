# sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    protocol = "https"
    priority = 0.8
    changefreq = "weekly"

    def items(self):
        return ["home", "courses", "pricing", "about", "contact", "portal"]

    def location(self, item):
        return reverse(item)

    def get_urls(self, page=1, site=None, protocol=None):
        # Force the correct domain for production
        from django.contrib.sites.models import Site
        site = Site.objects.get(id=1)   # should be iq-tutors.co.uk
        return super().get_urls(page=page, site=site, protocol=self.protocol)