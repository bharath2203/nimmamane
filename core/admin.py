from django.contrib import admin
from .models import (
    House,
    Person,
    Lease,
    Rent,
    Sale
)

admin.site.register(House)
admin.site.register(Person)
admin.site.register(Lease)
admin.site.register(Rent)
admin.site.register(Sale)

