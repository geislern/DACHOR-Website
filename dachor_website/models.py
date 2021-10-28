from django.db import models


class NewsItem(models.Model):
    title = models.CharField(max_length=256, verbose_name='Überschrift', help_text='Titel der Ankündigung')
    text = models.TextField(verbose_name='Ankündigungstext', help_text='Erläuterung der Ankündigung')
    start = models.DateTimeField(verbose_name='Startzeitpunkt',
                                 help_text='Zeitpunkt ab dem die Ankündigung angezeigt werden soll')
    end = models.DateTimeField(verbose_name='Endzeitpunkt',
                               help_text='Zeitpunkt bis zu dem die Ankündigung angezeigt werden soll')

    class Meta:
        verbose_name = 'Ankündigung'
        verbose_name_plural = 'Ankündigungen'

    def __str__(self):
        return f'{self.id}: {self.title}'
