
from django.urls import path

from .views import \
    home, profile, booking_list, booking_detail, booking_create, \
    booking_update, booking_delete, booking_track

urlpatterns = [
    # path('', home, name='site-home'),
    path('', booking_list, name='site-home'),
    path('create/', booking_create, name='site-create'),
    path('<int:id>', booking_detail, name='site-detail'),
    path('<int:id>/track/', booking_track, name='site-track'),
    path('<int:id>/update/', booking_update, name='site-update'),
    path('<int:id>/delete/', booking_delete, name='site-delete'),
    
]
