from django.urls import path, include
from webapp.views import *

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('photo/', include([
        path('<int:pk>/', include([
            path('', PhotoView.as_view(), name='photo_view'),
            path('update/', PhotoUpdateView.as_view(), name='photo_update'),
            path('delete/', PhotoDeleteView.as_view(), name='photo_delete'),
            path('comments/add/', PhotoCommentCreateView.as_view(),
                 name='photo_comment_add'),
            path('chose/', PhotoLikeView.as_view(), name='photo_chosen'),
            path('not_chosed/', PhotoNotChosenView.as_view(), name='photo_not_chosen'),
        ])),
        path('add/', PhotoCreateView.as_view(), name='photo_create'),
    ])),

    path('comment/', include([
        path('<int:pk>/', include([
            path('update/', CommentUpdateView.as_view(), name='comment_update'),
            path('delete/', CommentDeleteView.as_view(), name='comment_delete'),
        ]))
    ]))
]
