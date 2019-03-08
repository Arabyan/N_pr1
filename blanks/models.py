# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.files.storage import FileSystemStorage
from my_pdf.settings import PRIVATE_STORAGE_ROOT
# Create your models here.
from blanks.validators import validate_file_extension

from django.contrib.auth.models import User

class DocFile(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/', validators=[validate_file_extension])
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

    def delete(self, *args, **kwargs):
        self.document.delete()
        super().delete(*args, **kwargs)


class DocFields(models.Model):
    doc_fields = models.CharField( max_length=50)


fs_edited = FileSystemStorage(location=PRIVATE_STORAGE_ROOT)


class DocEdited(models.Model):
    edited_description = models.CharField(max_length=250, blank=True)
    document_edited = models.FileField(upload_to='documents_edited/',  storage=fs_edited)

    def __str__(self):
        return self.edited_description


class AuthorRecognition(models.Model):
    upload_author = models.ForeignKey(User, default=None, on_delete=models.CASCADE,)