from django.urls import path ,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# register it to urls
router.register('items',views.viewsets_items)

urlpatterns = [
    # CBV
    path('rest/get/', views.get_add_items.as_view(), name='get'),
    path('rest/get/<int:pk>', views.get_update_del.as_view(), name='pk_item'),

    # mixins
    path('rest/mixins/', views.mixins_list.as_view(), name='mixins_get'),
    path('rest/mixins/<int:pk>', views.mixins_pk.as_view(), name='mixins_pk'),

    # generics
    path('rest/generics/', views.generics_list.as_view(), name='generics_get'),
    path('rest/generics/<int:pk>', views.generics_pk.as_view(), name='generics_pk'),

    # Search and filter in here
    # ViewSets
    path('rest/viewsets/', include(router.urls)),

    # FBV to get all items of certain user
    path('allitems/<int:pk>',views.all_items_for_user),
]