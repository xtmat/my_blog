from django.urls import path,re_path
from blog.views import ( PostListView,PostDetailView,PostCreateView,
                         PostUpdateView,PostDeleteView,DraftListView,
                         add_comment_to_post,remove_comment,approve_comment,
                         AboutView,publish_post )

urlpatterns = [
                path('',PostListView.as_view(),name='posts_list'),
                re_path(r'^posts/(?P<pk>\d+)/$',PostDetailView.as_view(),name='post_detail'),
                path('post/new/',PostCreateView.as_view(),name='new_post'),
                re_path(r'^post/(?P<pk>\d+)/edit/$',PostUpdateView.as_view(),name='edit_post'),
                re_path(r'^post/(?P<pk>\d+)/delete/$',PostDeleteView.as_view(),name='delete_post'),

                path('drafts/',DraftListView.as_view(),name='drafts_list'),
                re_path(r'^drafts/(?P<pk>\d+)/publish/$',publish_post,name='publish_post'),

                re_path(r'^post/(?P<pk>\d+)/comment/$',add_comment_to_post,name='comment'),
                re_path(r'^comment/(?P<pk>\d+)/approve/$',approve_comment,name='approve_comment'),
                re_path(r'^comment/(?P<pk>\d+)/remove/$',remove_comment,name='remove_comment'),

                path('about/',AboutView.as_view(),name='about'),
                ]
