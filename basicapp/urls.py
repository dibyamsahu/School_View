from django.conf.urls import url
from basicapp import views

app_name = "basicapp"

urlpatterns = [
    url(r"^$", views.SchoolListView.as_view(), name="list"),
    url(r"^(?P<pk>\d+)/$", views.SchoolDetailView.as_view(), name="detail"),
    url(r"^create/$", views.CreateSchool.as_view(), name="create"),
    url(r"^update/(?P<pk>\d+)/$", views.UpdateSchool.as_view(), name="update"),
    url(r"^delete/(?P<pk>\d+)/$", views.DeleteSchool.as_view(), name="delete"),
]
