from django.conf.urls import url, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'solutions', views.SolutionViewSet, base_name='solutions')
router.register(r'notebooks', views.NotebookViewSet, base_name='notebooks')
router.register(r'categories', views.CategoryViewSet, base_name='categories')

# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^solutions/(?P<pid>[0-9]+)/$', views.SolutionDetailView.as_view()),
    url(r'^solution/library/(?P<category_id>[0-9]+)/$', views.SolutionLibraryView.as_view()),
    url(r'^categories/(?P<id>[0-9]+)/notebooks/$', views.CategoryDetailView.as_view()),
]
