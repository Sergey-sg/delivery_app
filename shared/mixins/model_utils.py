from datetime import datetime

from django.db import models


class CreatedUpdateMixins(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ImageNameMixins:
    @staticmethod
    def get_image_name(name, filename):
        extension = filename.split('.')[-1]
        return f'{name}-{datetime.now()}.{extension}'

    def get_current_image_name(self, model):
        if self.pk is not None:
            orig = model.objects.get(pk=self.pk)
            if orig.image.name != self.image.name:
                if self.image:
                    name = self.get_image_name(name=self.name, filename=self.image.name)
                    return {'image_name': name, 'new': True}
            else:
                return {'new': False}
        else:
            name = self.get_image_name(name=self.name, filename=self.image.name)
            return {'image_name': name, 'new': True}


def get_image_name(name, filename):
    extension = filename.split('.')[-1]
    return f'{name}-{datetime.now()}.{extension}'
