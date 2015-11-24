from django.db import models
# Create your models here.


class Server(models.Model):
    STATUS = (
        # 设定服务器的状态，在status_server字段中调用
        ('T', '正常'),
        ('F', '不通'),
    )
    ip_address_server = models.CharField('服务器IP地址', primary_key=True, max_length=32)
    status_server = models.CharField('服务器是否正常', max_length=1, choices=STATUS, default='T')
    comments_server = models.CharField('备注', blank=True, max_length=128)
    date_server = models.DateField('投运时间', auto_now_add=True)

    def __str__(self):
        return self.ip_address_server

    class Meta:
        verbose_name_plural = '服务器'    # 返回服务器表名
        db_table = 'list_server'


class Camera(models.Model):
    STATUS = (
        ('T', '正常'),
        ('F', '不通'),
    )
    BRAND = (
        ('H', '海康威视'),
        ('L', '南京吕诺'),
    )
    ip_address_camera = models.CharField('IP地址', primary_key=True, max_length=255)
    address_camera = models.CharField('相机位置', max_length=255)
    status_camera = models.CharField('状态', choices=STATUS, default='T', max_length=1)
    server_camera = models.ForeignKey(Server, verbose_name='相机所属服务器', blank=True)
    brand_camera = models.CharField('品牌', choices=BRAND, default='L', max_length=1)
    date_camera = models.DateField('投运时间', auto_now_add=True)

    def __str__(self):
        return self.address_camera

    class Meta:
        verbose_name_plural = '摄像机'
        db_table = 'list_camera'
