from django.urls import path

from .views import creative_list_view

# from .views import user_detail_view
# from .views import user_redirect_view
# from .views import user_update_view

app_name = "creatives"

urlpatterns = [
    path("~list/", view=creative_list_view, name='list')
]