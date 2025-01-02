from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PostListCreateView,
    PostRetrieveUpdateDestroyView,
    CommentListCreateView,
    CommentRetrieveUpdateDestroyView,
    GroupListView,
    GroupDetailView,
    FollowView,
)

router = DefaultRouter()

urlpatterns = [
    path("posts/", PostListCreateView.as_view(), name="post-list"),
    path(
        "posts/<int:pk>/", 
        PostRetrieveUpdateDestroyView.as_view(), 
        name="post-detail"
    ),
    path(
        "posts/<int:post_id>/comments/",
        CommentListCreateView.as_view(),
        name="comment-list",
    ),
    path(
        "posts/<int:post_id>/comments/<int:pk>/",
        CommentRetrieveUpdateDestroyView.as_view(),
        name="comment-detail",
    ),
    path("groups/", GroupListView.as_view(), name="group-list"),
    path("groups/<int:pk>/", GroupDetailView.as_view(), name="group-detail"),
    path("follow/", FollowView.as_view(), name="follow-list"),
    path("jwt/", include("rest_framework.urls", namespace="rest_framework")),
]
