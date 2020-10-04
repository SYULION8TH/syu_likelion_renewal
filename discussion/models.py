from django.db import models

# Create your models here.
class MainDiscussion(models.Model):
    dis_id = models.AutoField(primary_key=True)
    dis_title = models.CharField(max_length=45, blank=True, null=True)
    dis_desc = models.CharField(max_length=500, blank=True, null=True)
    dis_solved = models.CharField(max_length=500, blank=True, null=True)
    ip = models.ForeignKey('MainIp', models.DO_NOTHING, blank=True, null=True)
    wiki = models.ForeignKey('MainWiki', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_discussion'


class MainIp(models.Model):
    ip_id = models.AutoField(primary_key=True)
    ip = models.CharField(unique=True, max_length=45)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'main_ip'


class MainWiki(models.Model):
    wiki_id = models.AutoField(primary_key=True)
    wiki_img = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    wiki_desc = models.TextField(blank=True, null=True)
    wiki_title = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_wiki'



