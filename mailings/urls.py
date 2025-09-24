from django.urls import path

from mailings.views import (
    MessageListView,
    MessageDetailView,
    MessageCreateView,
    MessageDeleteView,
    MessageUpdateView,
    MailingRecipientListView,
    MailingRecipientCreateView,
    MailingRecipientDetailView,
    MailingRecipientUpdateView,
    MailingRecipientDeleteView,
    NewsletterListView,
    NewsletterCreateView,
    NewsletterDetailView,
    NewsletterUpdateView,
    NewsletterDeleteView,
    HomePageListView,
    AttemptToSendListView,
    NewsletterIsDisabledView,
)

app_name = "mailings"

urlpatterns = [
    path(
        "mailing_recipient_list/",
        MailingRecipientListView.as_view(),
        name="mailing_recipient_list",
    ),
    path(
        "mailing_recipient_create/",
        MailingRecipientCreateView.as_view(),
        name="mailing_recipient_create",
    ),
    path(
        "mailing_recipient_detail/<int:pk>/",
        MailingRecipientDetailView.as_view(),
        name="mailing_recipient_detail",
    ),
    path(
        "mailing_recipient_update/<int:pk>/",
        MailingRecipientUpdateView.as_view(),
        name="mailing_recipient_update",
    ),
    path(
        "mailing_recipient_delete/<int:pk>/",
        MailingRecipientDeleteView.as_view(),
        name="mailing_recipient_delete",
    ),
    path("message_list/", MessageListView.as_view(), name="message_list"),
    path("message_create/", MessageCreateView.as_view(), name="message_create"),
    path(
        "message_detail/<int:pk>/", MessageDetailView.as_view(), name="message_detail"
    ),
    path(
        "message_update/<int:pk>/", MessageUpdateView.as_view(), name="message_update"
    ),
    path(
        "message_delete/<int:pk>/", MessageDeleteView.as_view(), name="message_delete"
    ),
    path("newsletter_list/", NewsletterListView.as_view(), name="newsletter_list"),
    path(
        "newsletter_create/", NewsletterCreateView.as_view(), name="newsletter_create"
    ),
    path(
        "newsletter_detail/<int:pk>/",
        NewsletterDetailView.as_view(),
        name="newsletter_detail",
    ),
    path(
        "newsletter_update/<int:pk>/",
        NewsletterUpdateView.as_view(),
        name="newsletter_update",
    ),
    path(
        "newsletter_delete/<int:pk>/",
        NewsletterDeleteView.as_view(),
        name="newsletter_delete",
    ),
    path(
        "newsletter_is_disabled/<int:pk>/",
        NewsletterIsDisabledView.as_view(),
        name="newsletter_is_disabled",
    ),
    path("", HomePageListView.as_view(), name="home_page"),
    path("attempt_to_send/", AttemptToSendListView.as_view(), name="attempt_to_send"),
]
