from django.urls import path, include
from . import views

app_name = 'viz'
## module san pham
urlpatterns = [
    path('', views.index, name='index'),
    path('them_nhom_hang/', views.them_nhom_hang, name='them_nhom_hang'),
    path('them_mat_hang/', views.them_mat_hang, name='them_mat_hang'),
    path('update_nhom_hang/<str:ma_nhom_hang>/', views.update_nhom_hang, name='update_nhom_hang'),
    path('update_mat_hang/<str:ma_mat_hang>', views.update_mat_hang, name='update_mat_hang'),
    path('list_nhom_hang/', views.list_nhom_hang, name='list_nhom_hang'),
    path('list_mat_hang/', views.list_mat_hang, name='list_mat_hang'),
    path('delete_nhom_hang/<str:ma_nhom_hang>/', views.delete_nhom_hang, name='delete_nhom_hang'),
    path('delete_mat_hang/<str:ma_mat_hang>/', views.delete_mat_hang, name='delete_mat_hang'),
]
## module khach hang
urlpatterns += [
    path('them_khach_hang/', views.them_khach_hang, name='them_khach_hang'),
    path('list_khach_hang/', views.list_khach_hang, name='list_khach_hang'),
    path('update_khach_hang/<str:ma_khach_hang>/', views.update_khach_hang, name='update_khach_hang'),
    path('delete_khach_hang/<str:ma_khach_hang>/', views.delete_khach_hang, name='delete_khach_hang'),
    path('them_pkkh/', views.them_pkkh, name='them_pkkh'),
    path('list_pkkh/', views.list_pkkh, name='list_pkkh'),
    path('update_pkkh/<str:ma_pkkh>/', views.update_pkkh, name='update_pkkh'),
    path('delete_pkkh/<str:ma_pkkh>/', views.delete_pkkh, name='delete_pkkh'),
]

## module don hang
urlpatterns += [
    path('them_don_hang/', views.them_don_hang, name='them_don_hang'),
    path('list_don_hang/', views.list_don_hang, name='list_don_hang'),
    # path('update_don_hang/<str:ma_don_hang>/', views.update_don_hang, name='update_don_hang'),
    path('delete_don_hang/<str:ma_don_hang>/', views.delete_don_hang, name='delete_don_hang'),
]

## file upload func
urlpatterns += [
    path('upload_don_hang/', views.upload_don_hang, name='upload_don_hang'),
    path('upload_nhom_hang/', views.upload_nhom_hang, name='upload_nhom_hang'),
    path('upload_mat_hang/', views.upload_mat_hang, name='upload_mat_hang'),
    path('upload_khach_hang/', views.upload_khach_hang, name='upload_khach_hang'),
    path('upload_pkkh/', views.upload_pkkh, name='upload_pkkh'),
]


## module thong ke 
urlpatterns += [
    path('detail_khach_hang/<str:ma_khach_hang>', views.detail_khach_hang, name='detail_khach_hang'),
    path('detail_mat_hang/<str:ma_mat_hang>', views.detail_mat_hang, name='detail_mat_hang'),
]
## tao don hang voi fetchapi
urlpatterns += [
    path('get_khach_hang_info/<str:ma_khach_hang>/', views.get_khach_hang_info, name='get_khach_hang_info'),
    path('get_mat_hang_info/<str:ma_mat_hang>/', views.get_mat_hang_info, name='get_mat_hang_info'),
]

## temp xóa đơn hàng :D
urlpatterns += [
    path('xoa_het/', views.delete_all_don_hang, name='xoa_het'),
]

## visualization page
urlpatterns += [
    path('visualization/', views.visualization, name='visualization')
]