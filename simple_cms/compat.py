import django

if django.VERSION < (1, 7):
    from django.db.models import loading
    get_model = loading.get_model

else:
    from django.apps import apps
    get_model = apps.get_model