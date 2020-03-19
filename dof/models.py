from django.db import models


class Diagnosis(models.Model):
    """
    FFS 診断の質問文リスト
    """
    qn = models.AutoField(verbose_name='質問番号', primary_key=True)
    factor = models.CharField(verbose_name='因子', max_length=5)
    sentence = models.CharField(verbose_name='質問文', max_length=250)

    def __str__(self):
        return self.sentence
