from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from blog.api_views import post_list , post_detail
# from blog.api_views import PostDetail

urlpatterns = [
    path("posts/", post_list, name="api_post_list"),
    path("posts/<int:pk>", post_detail, name="api_post_detail"),
    # path("posts/<int:pk>", PostDetail.as_view(), name="api_post_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
