from __future__ import absolute_import
from __future__ import unicode_literals

from djongo import models
from django.conf import settings


class TimeStampedModel(models.Model):

    class Meta(object):
        abstract = True
    cdate = models.DateTimeField(auto_now_add=True)
    udate = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if kwargs and kwargs.get('update_fields'):
            if 'udate' not in kwargs['update_fields']:
                kwargs['update_fields'].append("udate")
        super(TimeStampedModel, self).save(*args, **kwargs)


class Todo(TimeStampedModel):
    DONE = "done"
    NEW = "new"
    STATUS_TYPE = (
        (DONE, "Task Done"),
        (NEW, "New Task")
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column='auth_user_id')
    status = models.CharField(max_length=64, choices=STATUS_TYPE, blank=True, null=True)
    content = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'todos'

    def __str__(self):
        """Visual identification"""
        return f'{self.user} - {self.status}'

