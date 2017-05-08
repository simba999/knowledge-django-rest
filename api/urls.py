from django.conf.urls import url, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'categories', views.CategoriesViewSet, base_name='categories')

# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^category/(?P<pk>[0-9]+)/solutions$', views.CategoryDetailView.as_view()),
    url(r'^performance/(?P<notebook_id>[0-9]+)/(?P<user_id>)/notebooks$', views.PerformanceNotebooksView.as_view()),
    # url(r'^notebook')
]
