from __future__ import unicode_literals
from django.contrib import admin


from .models import Detail,File,Template
admin.site.register(File)

admin.site.register(Detail)

admin.site.register(Template)
