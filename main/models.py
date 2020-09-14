from django.db import models

# Create your models here.

class lesson(models.Model):
    lesson_id = models.AutoField(primary_key=True)
    lesson_desc = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class rel_member_service(models.Model):
    id = models.AutoField(primary_key=True)
    member = models.ForeignKey('member', on_delete=models.CASCADE)
    service = models.ForeignKey('service', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rank = models.CharField(max_length=45, null=True)

class wiki(models.Model):
    wiki_id = models.AutoField(primary_key=True)
    wiki_img = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    wiki_desc = models.TextField(null=True)
    wiki_title = models.CharField(max_length=45, null=True)


class discussion(models.Model):
    dis_id = models.AutoField(primary_key=True)
    dis_title = models.CharField(max_length=45, null=True)
    dis_desc = models.CharField(max_length=500, null=True)
    dis_solved = models.CharField(max_length=500, null=True)
    wiki = models.ForeignKey(wiki, on_delete=models.CASCADE, null=True)
    ip = models.ForeignKey('ip', on_delete=models.CASCADE, null=True)



class member(models.Model):
    mem_id = models.AutoField(primary_key=True)
    mem_name = models.CharField(max_length=45)
    mem_email = models.CharField(max_length=45)
    mem_profile = models.ImageField(null=True)
    mem_number = models.CharField(max_length=45, null=True)
    joined_at = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    mem_rank = models.CharField(max_length=45)
    github_url = models.CharField(max_length=1000, null=True)

class service(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=45)
    service_desc = models.CharField(max_length=45)
    service_img = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    made_at = models.DateTimeField()
    skill_stack = models.CharField(max_length=300, null=True)

class rel_wiki_hashtag(models.Model):
    id = models.AutoField(primary_key=True)
    wiki = models.ForeignKey(wiki, on_delete=models.CASCADE, null=True)
    hashtag = models.ForeignKey('hashtag', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class rel_wiki_ip(models.Model):
    id = models.AutoField(primary_key=True)
    wiki = models.ForeignKey(wiki, on_delete=models.CASCADE)
    ip = models.ForeignKey('ip', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class rel_mem_sns(models.Model):
    id = models.AutoField(primary_key=True)
    member = models.ForeignKey('member', on_delete=models.CASCADE)
    sns = models.ForeignKey('sns', on_delete=models.CASCADE)
    sns_url = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class rel_mem_timeline(models.Model):
    id = models.AutoField(primary_key=True)
    time_line = models.ForeignKey('time_line', on_delete=models.CASCADE, null=True)
    member = models.ForeignKey('member', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    start_act = models.DateTimeField(null=True)


class hashtag(models.Model):
    ht_id = models.AutoField(primary_key=True)
    ht_name = models.CharField(max_length=45, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class ip(models.Model):
    ip_id = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=45, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class sns(models.Model):
    sns_id = models.AutoField(primary_key=True)
    sns_name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sns_img = models.ImageField(null=True)


class time_line(models.Model):
    tl_id = models.AutoField(primary_key=True)
    tl_img = models.ImageField(null=True)
    tl_name = models.CharField(max_length=45)
    tl_desc = models.TextField()
    tl_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class opinion(models.Model):
    op_id = models.AutoField(primary_key=True)
    op_body = models.CharField(max_length=45, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ip = models.ForeignKey(ip, on_delete=models.CASCADE, null=True)









