# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
from blanks.validators import validate_file_extension

class DocFile(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/', validators=[validate_file_extension])

    # uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

    def delete(self, *args, **kwargs):
        self.document.delete()
        super().delete(*args, **kwargs)

    def edit_filez(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_document_url(self):
        if self.file:
            return '/documents/2017/ + self.document.name + ".txt" '
#
class DocFields(models.Model):
    doc_fields = models.CharField( max_length=50)