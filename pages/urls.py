from pages.views import home_page_view, HomePageView, AboutPageView
from django.urls import path


urlpatterns = [
    # path("", home_page_view, name='home'),
    path("", HomePageView.as_view(), name='home'),
    path("about/", AboutPageView.as_view(), name='about'),




]