from django.conf.urls import url, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'solution', views.SolutionViewSet, base_name='solutions')
router.register(r'notebooks', views.NotebookViewSet, base_name='notebooks')
router.register(r'categories', views.CategoryViewSet, base_name='categories')
router.register(r'prices', views.PriceViewSet, base_name='prices')
router.register(r'performances', views.PerformanceViewSet, base_name='performance')

# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^solution/library/(?P<category_id>[0-9]+)/$', views.SolutionLibraryView.as_view()),
    url(r'^categories/(?P<id>[0-9]+)/notebooks/$', views.CategoryNotebookView.as_view()),
    url(r'^categories/(?P<id>[0-9]+)/datasets/$', views.CategoryDatasetView.as_view()),
    url(r'^categories/(?P<id>[0-9]+)/solutions/$', views.CategorySolutionView.as_view()),
    url(r'^performance/(?P<notebook_id>[0-9]+)/(?P<user_id>[0-9]+)/notebooks/$', views.PerformanceNotebookView.as_view()),
    url(r'^anomaly/(?P<id>[0-9]+)/$', views.AnomalyView.as_view()),
    # url(r'^performance/(?P<id>[0-9]+)/solutions/$', views.CategorySolutionView2.as_view()),
    # url(r'^performance/solution/$', views.CategorySolutionView3.as_view()),

]
