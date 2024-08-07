from django.urls import path
from event.views import (
    index,
    RunnerListView,
    RunnerDetailView,
    RunnerCreateView,
)

app_name = "event"

urlpatterns = [
    path("", index, name="index"),
    path("events/<int:event_id>/runners/", RunnerListView.as_view(), name='runner-list'),
    path('users/<int:pk>/', RunnerDetailView.as_view(), name='runner-detail'),
    path('users/add/', RunnerCreateView.as_view(), name='runner-add'),
    # path('users/<int:pk>/edit/', RunnerUserUpdateView.as_view(), name='runneruser-edit'),
    # path('users/<int:pk>/delete/', RunnerUserDeleteView.as_view(), name='runneruser-delete'),

]