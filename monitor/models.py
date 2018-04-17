# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Diskstat(models.Model):
    id = models.IntegerField(db_column='Id')  # Field name made lowercase.
    time = models.CharField(primary_key=True, max_length=255)
    disk1 = models.CharField(max_length=255, blank=True, null=True)
    disk2 = models.CharField(max_length=255, blank=True, null=True)
    disk3 = models.CharField(max_length=255, blank=True, null=True)
    disk4 = models.CharField(max_length=255, blank=True, null=True)
    disk5 = models.CharField(max_length=255, blank=True, null=True)
    disk6 = models.CharField(max_length=255, blank=True, null=True)
    disk7 = models.CharField(max_length=255, blank=True, null=True)
    disk8 = models.CharField(max_length=255, blank=True, null=True)
    disk9 = models.CharField(max_length=255, blank=True, null=True)
    disk10 = models.CharField(max_length=255, blank=True, null=True)
    disk11 = models.CharField(max_length=255, blank=True, null=True)
    disk12 = models.CharField(max_length=255, blank=True, null=True)
    disk13 = models.CharField(max_length=255, blank=True, null=True)
    disk14 = models.CharField(max_length=255, blank=True, null=True)
    disk15 = models.CharField(max_length=255, blank=True, null=True)
    disk16 = models.CharField(max_length=255, blank=True, null=True)
    disk17 = models.CharField(max_length=255, blank=True, null=True)
    disk18 = models.CharField(max_length=255, blank=True, null=True)
    disk19 = models.CharField(max_length=255, blank=True, null=True)
    disk20 = models.CharField(max_length=255, blank=True, null=True)
    disk21 = models.CharField(max_length=255, blank=True, null=True)
    disk22 = models.CharField(max_length=255, blank=True, null=True)
    disk23 = models.CharField(max_length=255, blank=True, null=True)
    disk24 = models.CharField(max_length=255, blank=True, null=True)
    disk25 = models.CharField(max_length=255, blank=True, null=True)
    disk26 = models.CharField(max_length=255, blank=True, null=True)
    disk27 = models.CharField(max_length=255, blank=True, null=True)
    disk28 = models.CharField(max_length=255, blank=True, null=True)
    disk29 = models.CharField(max_length=255, blank=True, null=True)
    disk30 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diskstat'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Hostlist(models.Model):
    id = models.IntegerField(db_column='Id')  # Field name made lowercase.
    ip = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'hostlist'


class Netstat(models.Model):
    id = models.IntegerField(db_column='Id')  # Field name made lowercase.
    time = models.CharField(primary_key=True, max_length=255)
    net1 = models.CharField(max_length=255, blank=True, null=True)
    net2 = models.CharField(max_length=255, blank=True, null=True)
    net3 = models.CharField(max_length=255, blank=True, null=True)
    net4 = models.CharField(max_length=255, blank=True, null=True)
    net5 = models.CharField(max_length=255, blank=True, null=True)
    net6 = models.CharField(max_length=255, blank=True, null=True)
    net7 = models.CharField(max_length=255, blank=True, null=True)
    net8 = models.CharField(max_length=255, blank=True, null=True)
    net9 = models.CharField(max_length=255, blank=True, null=True)
    net10 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'netstat'


class Sysstat(models.Model):
    id = models.IntegerField(db_column='Id')  # Field name made lowercase.
    loadaverage = models.CharField(max_length=255, blank=True, null=True)
    uptime = models.CharField(max_length=255, blank=True, null=True)
    totaltask = models.CharField(max_length=255, blank=True, null=True)
    running = models.CharField(max_length=255, blank=True, null=True)
    sleeping = models.CharField(max_length=255, blank=True, null=True)
    stopped = models.CharField(max_length=255, blank=True, null=True)
    zombie = models.CharField(max_length=255, blank=True, null=True)
    cpuus = models.CharField(max_length=255, blank=True, null=True)
    cpusy = models.CharField(max_length=255, blank=True, null=True)
    cpyni = models.CharField(max_length=255, blank=True, null=True)
    cpuid = models.CharField(max_length=255, blank=True, null=True)
    cpuwa = models.CharField(max_length=255, blank=True, null=True)
    cpuhi = models.CharField(max_length=255, blank=True, null=True)
    cpusi = models.CharField(max_length=255, blank=True, null=True)
    cpust = models.CharField(max_length=255, blank=True, null=True)
    memtotal = models.CharField(max_length=255, blank=True, null=True)
    memfree = models.CharField(max_length=255, blank=True, null=True)
    memused = models.CharField(max_length=255, blank=True, null=True)
    memcache = models.CharField(max_length=255, blank=True, null=True)
    swaptotal = models.CharField(max_length=255, blank=True, null=True)
    swapfree = models.CharField(max_length=255, blank=True, null=True)
    swapused = models.CharField(max_length=255, blank=True, null=True)
    swapcache = models.CharField(max_length=255, blank=True, null=True)
    hostname = models.CharField(max_length=255, blank=True, null=True)
    cpu_pcount = models.CharField(max_length=255, blank=True, null=True)
    cpu_lcount = models.CharField(max_length=255, blank=True, null=True)
    version = models.CharField(max_length=255, blank=True, null=True)
    now_time = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'sysstat'