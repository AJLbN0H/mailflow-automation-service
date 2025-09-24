from django import forms

from .models import Message, MailingRecipient, Newsletter


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = [
            "topic",
            "content",
        ]

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields["topic"].widget.attrs.update({"class": "form-control"})
        self.fields["content"].widget.attrs.update({"class": "form-control"})


class MailingRecipientForm(forms.ModelForm):

    class Meta:
        model = MailingRecipient
        fields = ["email", "full_name", "comment"]

    def __init__(self, *args, **kwargs):
        super(MailingRecipientForm, self).__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update({"class": "form-control"})
        self.fields["full_name"].widget.attrs.update({"class": "form-control"})
        self.fields["comment"].widget.attrs.update({"class": "form-control"})


class NewsletterForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = [
            "sending_date",
            "end_date_of_send",
            "message",
            "recipients",
        ]

    def __init__(self, *args, **kwargs):
        super(NewsletterForm, self).__init__(*args, **kwargs)
        self.fields["sending_date"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Год-месяц-День часы:минуты:секунды",
            }
        )
        self.fields["end_date_of_send"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Год-месяц-День часы:минуты:секунды",
            }
        )
        self.fields["message"].widget.attrs.update({"class": "form-control"})
        self.fields["recipients"].widget.attrs.update({"class": "form-control"})


class NewsletterIsDisabledForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = [
            "newsletter_is_disabled",
        ]

    def __init__(self, *args, **kwargs):
        super(NewsletterIsDisabledForm, self).__init__(*args, **kwargs)
        self.fields["newsletter_is_disabled"].widget.attrs.update(
            {"class": "form-check"}
        )
