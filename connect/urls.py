from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$',
        views.RootRedirectionView.as_view(),
        name="root"),

    # Step by step
    url(r'^getting-started/$',
        views.GettingStartedView.as_view(),
        name="getting-started")
]
