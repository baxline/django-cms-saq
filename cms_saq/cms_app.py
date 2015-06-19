from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class SaqApphook(CMSApp):
    name =_("SAQ")
    urls = ["cms_saq.urls"]
    
apphook_pool.register(SaqApphook)