from django.db import models


class Shows(models.Model):
    class Meta:
        verbose_name = "Show"
        verbose_name_plural = "Shows"

    local = models.CharField('Local', max_length=200)
    endereco = models.CharField('Endereço', max_length=100)
    data = models.DateField()

    def __str__(self):  # adicionado
        return self.local  # adicionado
