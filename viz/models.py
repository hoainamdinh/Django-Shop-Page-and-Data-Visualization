from django.db import models
import random, datetime
from django.utils import timezone
import pandas as pd
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

def generate_id(cls, field_name, prefix, num_length): 
    """Tạo ID tự động với prefix và độ dài cố định"""        
    while True:
        num_part = str(random.randint(0, 10**num_length - 1)).zfill(num_length)
        new_id = prefix + num_part
        if not cls.objects.filter(**{field_name: new_id}).exists():
            return new_id

class NhomHang(models.Model):
    ma_nhom_hang = models.CharField(primary_key=True, max_length=8, unique=True)
    ten_nhom_hang = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Nhóm hàng"

    def __str__(self):
        return f"{self.ma_nhom_hang}"    

class MatHang(models.Model):    
    ma_mat_hang = models.CharField(primary_key=True, max_length=8, unique=True)
    ten_mat_hang = models.CharField(max_length=100)
    ma_nhom_hang = models.ForeignKey(NhomHang, on_delete=models.CASCADE)
    don_gia = models.IntegerField()
    
    class Meta:
        verbose_name_plural = "Mặt hàng"                    
    
    def __str__(self):
        return self.ten_mat_hang     

class PhanKhucKhachHang(models.Model):
    ma_pkkh = models.CharField(primary_key=True, max_length=10, unique=True)
    mo_ta_pkkh = models.TextField()

    class Meta:
        verbose_name_plural = "Phân khúc khách hàng"

    def __str__(self):
        return self.ma_pkkh

class KhachHang(models.Model):
    ma_khach_hang = models.CharField(primary_key=True, max_length=8, unique=True)
    ten_khach_hang = models.CharField(max_length=100)
    phan_khuc = models.ForeignKey(PhanKhucKhachHang, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Khách hàng"
        
    def __str__(self):
        return self.ten_khach_hang
        
class DonHang(models.Model):
    id = models.AutoField(primary_key=True)
    thoi_gian_tao_don = models.DateTimeField(default=timezone.now)
    ma_don_hang = models.CharField(max_length=10)
    ma_khach_hang = models.CharField(max_length=9)
    khach_hang = models.TextField()
    ma_pkkh = models.CharField(max_length=3)
    mo_ta_pkkh = models.TextField()
    ma_nhom_hang = models.CharField(max_length=4)
    ten_nhom_hang = models.TextField()
    ma_mat_hang = models.CharField(max_length=8)
    ten_mat_hang  = models.TextField()
    don_gia = models.IntegerField()         
    so_luong = models.IntegerField()
    thanh_tien = models.IntegerField()
    class Meta:
        verbose_name_plural = "Đơn hàng"

    def save(self, *args, **kwargs):
        self.thanh_tien = self.so_luong * MatHang.objects.get(ma_mat_hang=self.ma_mat_hang).don_gia
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.ma_don_hang} - {self.ma_mat_hang} - SL: {self.so_luong} - Tổng: {self.thanh_tien}"
    

class Chat(models.Model):
    sender = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
