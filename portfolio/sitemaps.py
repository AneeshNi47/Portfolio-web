from django.contrib.sitemaps import Sitemap
from blog.models import Blog
from jobs.models import Job
 
class PostSitemap(Sitemap):    
    changefreq = "weekly"
    priority = 0.9
 
    def items(self):
        return Blog.objects.all()
 
    def lastmod(self, obj):
        return obj.pub_date