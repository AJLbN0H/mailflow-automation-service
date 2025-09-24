from django.db import models

from users.models import User


class MailingRecipient(models.Model):

    email = models.CharField(
        unique=True, max_length=150, verbose_name="Email", help_text="Введите email"
    )
    full_name = models.CharField(
        max_length=150, verbose_name="Ф.И.О", help_text="Введите Ф.И.О"
    )
    comment = models.TextField(
        verbose_name="Комментарий", help_text="Напишите комментарий"
    )
    owner = models.ForeignKey(
        User, verbose_name="Владелец", blank=True, null=True, on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.full_name}, {self.email}"

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        ordering = ["email", "full_name"]
        permissions = [
            ("can_view_mailing_recipient", "Can view mailing recipient"),
        ]


class Message(models.Model):

    topic = models.CharField(
        max_length=150, verbose_name="Тема письма", help_text="Введите тему письма"
    )
    content = models.TextField(
        verbose_name="Текст письма", help_text="Введите текст письма"
    )
    owner = models.ForeignKey(
        User, verbose_name="Владелец", blank=True, null=True, on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.topic}"

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ["topic"]
        permissions = [
            ("can_view_message", "Can view message"),
        ]


class Newsletter(models.Model):

    sending_date = models.DateTimeField(
        verbose_name="Дата и время первой отправки",
        help_text="Впишите дату и время первой отправки",
    )
    end_date_of_send = models.DateTimeField(
        verbose_name="Дата и время окончания отправки",
        help_text="Впишите дату и время окончания отправки",
    )
    status = models.CharField(max_length=9, verbose_name="Статус")
    message = models.ForeignKey(
        Message,
        verbose_name="Сообщение",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    recipients = models.ManyToManyField(MailingRecipient, verbose_name="Получатели")
    owner = models.ForeignKey(
        User, verbose_name="Владелец", blank=True, null=True, on_delete=models.CASCADE
    )
    newsletter_is_disabled = models.BooleanField(
        default=False, verbose_name="Рассылка отключена"
    )

    def __str__(self):
        return f"{self.status}, {self.message}, {self.recipients}"

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        ordering = ["sending_date", "end_date_of_send", "status"]
        permissions = [
            ("can_view_newsletter", "Can view newsletter"),
            ("can_newsletter_is_disabled", "Can newsletter is disabled"),
        ]


class AttemptToSend(models.Model):

    date_of_attempt = models.DateTimeField(
        verbose_name="Дата и время попытки", auto_now=True
    )
    status = models.CharField(max_length=10, verbose_name="Статус")
    mail_server_response = models.TextField(verbose_name="Ответ почтового сервера")
    newsletter = models.ForeignKey(
        Newsletter,
        verbose_name="Рассылка",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.status}, {self.date_of_attempt}"

    class Meta:
        verbose_name = "Попытка рассылки"
        verbose_name_plural = "Попытки рассылок"
        ordering = ["date_of_attempt", "status"]
