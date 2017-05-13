from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken import views as auth_views
from . import views

router = routers.DefaultRouter()
router.register(r'solution', views.SolutionViewSet, base_name='solutions')
router.register(r'notebooks', views.NotebookViewSet, base_name='notebooks')
router.register(r'categories', views.CategoryViewSet, base_name='categories')
router.register(r'prices', views.PriceViewSet, base_name='prices')
router.register(r'datasets', views.DatasetViewSet, base_name='datasets')
router.register(r'users', views.UserViewSet, base_name='users')
router.register(r'performances', views.PerformanceViewSet, base_name='performance')
router.register(r'ensembles', views.EnsembleViewSet, base_name='ensembles')

# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-token/$', auth_views.obtain_auth_token),
    url(r'^auth/$', views.AuthenticationView.as_view()),
    url(r'^solution/library/(?P<category_id>[0-9]+)/$', views.SolutionLibraryView.as_view()),
    url(r'^solution/library/$', views.SolutionLibraryAddView.as_view()),
    url(r'^solution/customsolution/(?P<user_id>[0-9]+)/$', views.CustomSolutionViewByUser.as_view()),
    url(r'^solution/customsolution/group/(?P<group_id>[0-9]+)/$', views.CustomSolutionViewByGroup.as_view()),
    # url(r'^solution/customsolution/$', views.CustomSolutionAddView.as_view()),
    url(r'^solution/customsolution/$', views.CustomSolutionAddView),
    url(r'^solution/customsolution/parent/(?P<parent_id>[0-9]+)/$', views.CustomSolutionViewByParent.as_view()),
    url(r'^solution/ensembles/(?P<id>[0-9]+)/$', views.SolutionEnsembleView.as_view()),
    url(r'^solution/dataset/(?P<id>[0-9]+)/$', views.SolutionDataSetView.as_view()),
    url(r'^solution/metaensembles/(?P<id>[0-9]+)/$', views.SolutionMetaEnsemblesView.as_view()),
    url(r'^solution/category/(?P<id>[0-9]+)/$', views.SolutionCategoryView.as_view()),
    url(r'^solution/type/(?P<id>[0-9]+)/$', views.SolutionTypeView.as_view()),
    url(r'^solution/all/(?P<id>[0-9]+)/$', views.SolutionAllView.as_view()),
    url(r'^solution/(?P<id>[0-9]+)/childsolution/$', views.ChildSolutionView.as_view()),
    url(r'^solution/(?P<id>[0-9]+)/parentsolution/$', views.ParentSolutionView.as_view()),
    url(r'^search/solution/$', views.SearchSolutionView.as_view()),
    url(r'^categories/(?P<id>[0-9]+)/notebooks/$', views.CategoryNotebookView.as_view()),
    url(r'^categories/(?P<id>[0-9]+)/datasets/$', views.CategoryDatasetView.as_view()),
    url(r'^categories/(?P<id>[0-9]+)/solutions/$', views.CategorySolutionView.as_view()),
    url(r'^performance/(?P<notebook_id>[0-9]+)/(?P<user_id>[0-9]+)/notebooks/$', views.PerformanceNotebookView.as_view()),
    url(r'^performance/(?P<ensemble_id>[0-9]+)/(?P<user_id>[0-9]+)/ensembles/$', views.PerformanceEnsembleView.as_view()),
    url(r'^performance/(?P<solution_id>[0-9]+)/(?P<user_id>[0-9]+)/solutions/$', views.PerformanceSolutionView.as_view()),
    url(r'^anomaly/(?P<id>[0-9]+)/$', views.AnomalyView.as_view()),
    url(r'^users/(?P<user_id>[0-9]+)/(?P<type>\w+)$', views.UserViewTypesByUser.as_view()),
    url(r'^users/solution/library/(?P<solution_id>[0-9]+)/$', views.UserSolutionLibraryViewById.as_view()),
    url(r'^notebooks/(?P<notebook_id>[0-9]+)/(?P<type>\w+)$', views.NotebookViewTypesById.as_view()),
    url(r'^search/notebooks/$', views.SearchNotebookView.as_view()),
    url(r'^search/datasets/$', views.SearchDatasetView.as_view()),
    url(r'^search/ensembles/$', views.SearchEnsembleView.as_view()),
]
