from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:subjects_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:subjects_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:subjects_id>/vote/', views.vote, name='vote'),
]