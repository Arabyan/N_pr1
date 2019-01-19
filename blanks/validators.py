from django.core.exceptions import ValidationError


def validate_file_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]
    valid_extension = ['.doc','.docx']
    if not ext.lower() in valid_extension:
        raise ValidationError(u'Unsupported file extension')