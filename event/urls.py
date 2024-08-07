from django.urls import path
from event.views import index, RunnerListView

app_name = "event"

urlpatterns = [
    path("", index, name="index"),
    path('users/', RunnerListView.as_view(), name='runner-list'),
    # path('users/<int:pk>/', RunnerUserDetailView.as_view(), name='runneruser-detail'),
    # path('users/add/', RunnerUserCreateView.as_view(), name='runneruser-add'),
    # path('users/<int:pk>/edit/', RunnerUserUpdateView.as_view(), name='runneruser-edit'),
    # path('users/<int:pk>/delete/', RunnerUserDeleteView.as_view(), name='runneruser-delete'),

]