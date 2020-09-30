from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from message_ms.views.conversation_view import ConversationList
from message_ms.views.conversation_view import ConversationDetail
from message_ms.views.message_view import MessageList
from message_ms.views.message_view import MessageDetail

urlpatterns = [
    path('conversations/', ConversationList.as_view()),
    path('conversations/<int:id>', MessageList.as_view()),
    path('conversations/<int:id>/<int:id_>', MessageDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)