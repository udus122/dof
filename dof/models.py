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


class DiagnosisResult(models.Model):
    """
        診断結果の表示用
    """
    ffs_type = models.CharField(verbose_name='91タイプ', max_length=5, blank=True, null=True)
    thinking_order = models.TextField(verbose_name='思考の順番')
    strength = models.TextField(verbose_name='強み', default='', null=True, blank=True)
    stressor = models.TextField(verbose_name='ストレス要因', default='', null=True, blank=True)
    weakness = models.TextField(verbose_name='弱み', default='', null=True, blank=True)
    advice = models.TextField(verbose_name='アドバイス', default='', null=True, blank=True)
