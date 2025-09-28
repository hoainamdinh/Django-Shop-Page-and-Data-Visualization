from django.shortcuts import render, redirect, get_object_or_404
from . import models
from .models import MatHang, NhomHang, KhachHang, DonHang, PhanKhucKhachHang, generate_id 
import pandas as pd
from django.contrib import messages
from django.http import JsonResponse
import json

# Create your views here.
def index(request):
    return render(request, 'index.html')

def them_nhom_hang(request):
    if request.method == "POST":
        ma_nhom_hang = request.POST.get('ma_nhom_hang')
        ten_nhom_hang = request.POST.get('ten_nhom_hang')
        mo_ta = request.POST.get('mo_ta')
        # Tạo một đối tượng và lưu vào database
        NhomHang.objects.create(
            ma_nhom_hang = ma_nhom_hang,
            ten_nhom_hang = ten_nhom_hang,
            mo_ta = mo_ta
        )
        return redirect('viz:list_nhom_hang')  # Chuyển hướng sau khi lưu
    return render(request, 'shop/nhom_hang/them_nhom_hang.html')

def them_mat_hang(request):
    list_nhom_hang = NhomHang.objects.all()
    if request.method == "POST":
        ten_mat_hang = request.POST.get('ten_mat_hang')
        ma_nhom_hang = request.POST.get('ma_nhom_hang')
        don_gia = request.POST.get('don_gia')
        mo_ta = request.POST.get('mo_ta')
        ma_mat_hang = generate_id(MatHang, 'ma_mat_hang', ma_nhom_hang, 2)
        # Tạo một đối tượng và lưu vào database
        MatHang.objects.create(
            ma_mat_hang = ma_mat_hang,
            ten_mat_hang = ten_mat_hang,
            ma_nhom_hang = NhomHang.objects.get(ma_nhom_hang=ma_nhom_hang),
            don_gia = don_gia,
            mo_ta = mo_ta
        )
        return redirect('viz:list_mat_hang')
    return render(request, 'shop/mat_hang/them_mat_hang.html', {'list_nhom_hang': list_nhom_hang})

def update_nhom_hang(request, ma_nhom_hang):
        # Tìm nhóm hàng theo mã, nếu không có thì trả về 404
    nhom_hang = get_object_or_404(NhomHang, ma_nhom_hang=ma_nhom_hang)
    if request.method == "POST":
        ten_nhom_hang = request.POST.get('ten_nhom_hang')
        mo_ta = request.POST.get('mo_ta')
            # Cập nhật dữ liệu
        nhom_hang.ten_nhom_hang = ten_nhom_hang
        nhom_hang.mo_ta = mo_ta
        nhom_hang.save()
        return redirect('viz:list_nhom_hang') 
    return render(request, 'shop/nhom_hang/update_nhom_hang.html', {'nhom_hang': nhom_hang})

def update_mat_hang(request, ma_mat_hang):
    mat_hang = get_object_or_404(MatHang, ma_mat_hang=ma_mat_hang)
    nhom_hang = NhomHang.objects.all()
    if request.method == "POST":
        ten_mat_hang = request.POST.get('ten_mat_hang')
        ma_nhom_hang = request.POST.get('ma_nhom_hang')
        don_gia = request.POST.get('don_gia')
        mat_hang.ma_nhom_hang = NhomHang.objects.get(ma_nhom_hang=ma_nhom_hang)
        mat_hang.ten_mat_hang = ten_mat_hang
        if request.POST.get('don_gia'):
            mat_hang.don_gia = don_gia
        mat_hang.save()
        return redirect('viz:list_mat_hang')
    return render(request, 'shop/mat_hang/update_mat_hang.html', {'mat_hang': mat_hang, 'nhom_hang': nhom_hang}) 

def list_nhom_hang(request):
    list_nhom_hang = NhomHang.objects.all()
    return render(request, 'shop/nhom_hang/list_nhom_hang.html', {'list_nhom_hang': list_nhom_hang})

def list_mat_hang(request):
    list_mat_hang = MatHang.objects.all()
    return render(request, 'shop/mat_hang/list_mat_hang.html', {'list_mat_hang': list_mat_hang})

def delete_nhom_hang(request, ma_nhom_hang):
    nhom_hang = get_object_or_404(NhomHang, ma_nhom_hang=ma_nhom_hang)
    if request.method == "POST":
        nhom_hang = get_object_or_404(NhomHang, ma_nhom_hang=ma_nhom_hang)
        nhom_hang.delete()
        return redirect('viz:list_nhom_hang')
    return render(request, 'shop/nhom_hang/delete_nhom_hang.html', {'nhom_hang': nhom_hang})

def delete_mat_hang(request, ma_mat_hang):
    mat_hang = get_object_or_404(MatHang, ma_mat_hang=ma_mat_hang)
    if request.method == "POST":
        mat_hang.delete()
        return redirect('viz:list_mat_hang')
    return render(request, 'shop/mat_hang/delete_mat_hang.html', {'mat_hang': mat_hang})

def them_pkkh(request):
    if request.method == "POST":
        ma_pkkh = request.POST.get('ma_pkkh')
        mo_ta_pkkh = request.POST.get('mo_ta_pkkh')
        # Tạo một đối tượng và lưu vào database
        PhanKhucKhachHang.objects.create(
            ma_pkkh = ma_pkkh,
            mo_ta_pkkh = mo_ta_pkkh
        )
        return redirect('viz:list_pkkh')
    return render(request, 'shop/pkkh/them_pkkh.html')

def list_pkkh(request):
    list_pkkh = PhanKhucKhachHang.objects.all()
    return render(request, 'shop/pkkh/list_pkkh.html', {'list_pkkh': list_pkkh})

def update_pkkh(request, ma_pkkh):
    pkkh = get_object_or_404(PhanKhucKhachHang, ma_pkkh=ma_pkkh)
    if request.method == "POST":
        mo_ta_pkkh = request.POST.get('mo_ta_pkkh')
        pkkh.mo_ta_pkkh = mo_ta_pkkh
        pkkh.save()
        return redirect('viz:list_pkkh')
    return render(request, 'shop/pkkh/update_pkkh.html', {'pkkh': pkkh})

def delete_pkkh(request, ma_pkkh):
    pkkh = get_object_or_404(PhanKhucKhachHang, ma_pkkh=ma_pkkh)
    if request.method == "POST":
        pkkh.delete()
        return redirect('viz:list_pkkh')
    return render(request, 'shop/pkkh/delete_pkkh.html', {'pkkh': pkkh})

def them_khach_hang(request):
    list_pkkh = PhanKhucKhachHang.objects.all()
    if request.method == "POST":
        ma_khach_hang = generate_id(KhachHang, 'ma_khach_hang', 'CUZ', 5)
        ten_khach_hang = request.POST.get('ten_khach_hang')
        phan_khuc = request.POST.get('phan_khuc')
        # Tạo một đối tượng và lưu vào database
        KhachHang.objects.create(
            ma_khach_hang = ma_khach_hang,
            ten_khach_hang = ten_khach_hang,
            phan_khuc = PhanKhucKhachHang.objects.get(ma_pkkh=phan_khuc)
        )
        return redirect('viz:list_khach_hang')
    return render(request, 'shop/khach_hang/them_khach_hang.html', {'list_pkkh': list_pkkh})

def list_khach_hang(request):
    list_khach_hang = KhachHang.objects.all()
    return render(request, 'shop/khach_hang/list_khach_hang.html', {'list_khach_hang': list_khach_hang})

def update_khach_hang(request, ma_khach_hang):
    khach_hang = get_object_or_404(KhachHang, ma_khach_hang=ma_khach_hang)
    list_pkkh = PhanKhucKhachHang.objects.all()
    if request.method == "POST":
        ten_khach_hang = request.POST.get('ten_khach_hang')
        phan_khuc = request.POST.get('phan_khuc')
        khach_hang.ten_khach_hang = ten_khach_hang
        khach_hang.phan_khuc = PhanKhucKhachHang.objects.get(ma_pkkh=phan_khuc)
        khach_hang.save()
        return redirect('viz:list_khach_hang')
    return render(request, 'shop/khach_hang/update_khach_hang.html', {'khach_hang': khach_hang, 'list_pkkh': list_pkkh})

def delete_khach_hang(request, ma_khach_hang):
    khach_hang = get_object_or_404(KhachHang, ma_khach_hang=ma_khach_hang)
    if request.method == "POST":
        khach_hang.delete()
        return redirect('viz:list_khach_hang')
    return render(request, 'shop/khach_hang/delete_khach_hang.html', {'khach_hang': khach_hang})

# def them_don_hang(request):
#     list_khach_hang = KhachHang.objects.all()
#     list_mat_hang = MatHang.objects.all()
    
#     selected_khach_hang = None
#     selected_mat_hang = None

#     if request.method == "POST":
#         ma_khach_hang = request.POST.get('ma_khach_hang', '')
#         ma_mat_hang = request.POST.get('ma_mat_hang', '')
#         so_luong = request.POST.get('so_luong', '')

#         # Lấy thông tin khách hàng nếu đã chọn
#         if ma_khach_hang:
#             try:
#                 selected_khach_hang = KhachHang.objects.get(ma_khach_hang=ma_khach_hang)
#             except KhachHang.DoesNotExist:
#                 selected_khach_hang = None

#         # Lấy thông tin mặt hàng nếu đã chọn
#         if ma_mat_hang:
#             try:
#                 selected_mat_hang = MatHang.objects.get(ma_mat_hang=ma_mat_hang)
#             except MatHang.DoesNotExist:
#                 selected_mat_hang = None

#         # Nếu đủ thông tin, thêm đơn hàng vào database
#         if selected_khach_hang and selected_mat_hang and so_luong:
#             ma_don_hang = generate_id(DonHang, 'ma_don_hang', 'ORD', 5)
#             DonHang.objects.create(
#                 ma_don_hang=ma_don_hang,
#                 ma_khach_hang=selected_khach_hang.ma_khach_hang,
#                 khach_hang=selected_khach_hang.ten_khach_hang,
#                 ma_pkkh=selected_khach_hang.phan_khuc.ma_pkkh,
#                 mo_ta_pkkh=selected_khach_hang.phan_khuc.mo_ta_pkkh,
#                 ma_nhom_hang=selected_mat_hang.ma_nhom_hang.ma_nhom_hang,
#                 ten_nhom_hang=selected_mat_hang.ma_nhom_hang.ten_nhom_hang,
#                 ma_mat_hang=selected_mat_hang.ma_mat_hang,
#                 ten_mat_hang=selected_mat_hang.ten_mat_hang,
#                 don_gia=int(selected_mat_hang.don_gia),
#                 so_luong=int(so_luong),
#                 thanh_tien= int(selected_mat_hang.don_gia) * int(so_luong)
#             )
#             return redirect('viz:list_don_hang')

#     return render(request, 'shop/don_hang/them_don_hang.html', {
#         'list_khach_hang': list_khach_hang,
#         'list_mat_hang': list_mat_hang,
#         'selected_khach_hang': selected_khach_hang,
#         'selected_mat_hang': selected_mat_hang
#     })



# def list_don_hang(request):
#     list_don_hang = DonHang.objects.all()
#     return render(request, 'shop/don_hang/list_don_hang.html', {'list_don_hang': list_don_hang})

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Thêm import này vào đầu file

def list_don_hang(request):
    # Lấy tất cả đơn hàng và sắp xếp theo thời gian mới nhất
    all_don_hang = DonHang.objects.all().order_by('-thoi_gian_tao_don')
    
    # Pagination - 25 items per page
    paginator = Paginator(all_don_hang, 25)
    page_number = request.GET.get('page')
    
    try:
        list_don_hang = paginator.page(page_number)
    except PageNotAnInteger:
        # Nếu page không phải số, trả về trang đầu
        list_don_hang = paginator.page(1)
    except EmptyPage:
        # Nếu page vượt quá số trang, trả về trang cuối
        list_don_hang = paginator.page(paginator.num_pages)
    
    return render(request, 'shop/don_hang/list_don_hang.html', {
        'list_don_hang': list_don_hang
    })


def delete_don_hang(request, ma_don_hang):
    don_hang = get_object_or_404(DonHang, ma_don_hang=ma_don_hang)
    if request.method == "POST":
        don_hang.delete()
        return redirect('viz:list_don_hang')
    return render(request, 'shop/don_hang/delete_don_hang.html', {'don_hang': don_hang})

## file upload function
def upload_don_hang(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']  # Lấy file từ request
        try:
            # đọc file
            if file.name.endswith('.csv'):
                df = pd.read_csv(file)
            elif file.name.endswith('.xlsx'):
                df = pd.read_excel(file)
            else:
                messages.error(request, "Chỉ hỗ trợ file CSV hoặc Excel.")
                return render(request, 'file_upload.html')
            # 
            required_columns = {'Thời gian tạo đơn',
                                'Mã đơn hàng',	
                                'Mã khách hàng',
                                'Tên khách hàng',
                                'Mã PKKH',
                                'Mô tả Phân Khúc Khách hàng',
                                'Mã nhóm hàng',
                                'Tên nhóm hàng',	
                                'Mã mặt hàng',
                                'Tên mặt hàng',
                                'SL',	
                                'Đơn giá',
                                'Thành tiền',
                                }
            if not required_columns.issubset(df.columns):
                messages.error(request, "File không đủ cột yêu cầu.")
                return render(request, 'file_upload.html')

            df.dropna(inplace=True) 
            # bulk create
            orders = [
                DonHang(
                    thoi_gian_tao_don=row['Thời gian tạo đơn'],
                    ma_don_hang=row['Mã đơn hàng'],
                    ma_khach_hang=row['Mã khách hàng'],
                    khach_hang=row['Tên khách hàng'],
                    ma_pkkh=row['Mã PKKH'],
                    mo_ta_pkkh=row['Mô tả Phân Khúc Khách hàng'],
                    ma_nhom_hang=row['Mã nhóm hàng'],
                    ten_nhom_hang=row['Tên nhóm hàng'],
                    ma_mat_hang=row['Mã mặt hàng'],
                    ten_mat_hang=row['Tên mặt hàng'],
                    so_luong=row['SL'],
                    don_gia=row['Đơn giá'],
                    thanh_tien=row['Thành tiền']
                )
                for _, row in df.iterrows()
            ]

            DonHang.objects.bulk_create(orders)

            messages.success(request, "Upload và lưu dữ liệu thành công!")
        
        except Exception as e:
            messages.error(request, f"Lỗi: {str(e)}")

    return render(request, 'shop/file_upload.html')

def upload_nhom_hang(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']  # Lấy file từ request
        try:
            # đọc file
            if file.name.endswith('.csv'):
                df = pd.read_csv(file)
            elif file.name.endswith('.xlsx'):
                df = pd.read_excel(file)
            else:
                messages.error(request, "Chỉ hỗ trợ file CSV hoặc Excel.")
                return render(request, 'file_upload.html')
            # 
            required_columns = {'Mã nhóm hàng', 'Tên nhóm hàng',}
            if not required_columns.issubset(df.columns):
                messages.error(request, "File không đủ cột yêu cầu.")
                return render(request, 'upload_nhom_hang.html')

            df.dropna(inplace=True)
            df = df[['Mã nhóm hàng', 'Tên nhóm hàng']]
            df = df.drop_duplicates(subset=['Mã nhóm hàng'])
            # bulk create
            groups = [
                NhomHang(
                    ma_nhom_hang=row['Mã nhóm hàng'],
                    ten_nhom_hang=row['Tên nhóm hàng'],
                )
                for _, row in df.iterrows()
            ]

            NhomHang.objects.bulk_create(groups)

            messages.success(request, "Upload và lưu dữ liệu thành công!")
        
        except Exception as e:
            messages.error(request, f"Lỗi: {str(e)}")

    return render(request, 'shop/file_upload.html')
    
def upload_mat_hang(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        try:
            # đọc file
            if file.name.endswith('.csv'):
                df = pd.read_csv(file)
            elif file.name.endswith('.xlsx'):
                df = pd.read_excel(file)
            else:
                messages.error(request, "Chỉ hỗ trợ file CSV hoặc Excel.")
                return render(request, 'file_upload.html')
    
            required_columns = {
                                'Mã mặt hàng',
                                'Tên mặt hàng',       
                                'Mã nhóm hàng',
                                'Đơn giá',
                                }
            if not required_columns.issubset(df.columns):
                messages.error(request, "File không đủ cột yêu cầu.")
                return render(request, 'file_upload.html')
            
            df.dropna(inplace=True) 
            df = df[['Mã mặt hàng', 'Tên mặt hàng', 'Mã nhóm hàng', 'Đơn giá']]
            df = df.drop_duplicates(subset=['Mã mặt hàng'])

            # bulk create
            orders = [
                MatHang(
                    ma_mat_hang=row['Mã mặt hàng'],
                    ten_mat_hang=row['Tên mặt hàng'],
                    ma_nhom_hang=NhomHang.objects.get(ma_nhom_hang=row['Mã nhóm hàng']),
                    don_gia=row['Đơn giá'],
                )
                for _, row in df.iterrows()
            ]

            MatHang.objects.bulk_create(orders)

            messages.success(request, "Upload và lưu dữ liệu thành công!")
        
        except Exception as e:
            messages.error(request, f"Lỗi: {str(e)}")

    return render(request, 'shop/file_upload.html')

def upload_khach_hang(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        try:
            # đọc file
            if file.name.endswith('.csv'):
                df = pd.read_csv(file)
            elif file.name.endswith('.xlsx'):
                df = pd.read_excel(file)
            else:
                messages.error(request, "Chỉ hỗ trợ file CSV hoặc Excel.")
                return render(request, 'file_upload.html')
    
            required_columns = {
                                'Mã khách hàng',
                                'Tên khách hàng',       
                                'Mã PKKH',
                                }
            if not required_columns.issubset(df.columns):
                messages.error(request, "File không đủ cột yêu cầu.")
                return render(request, 'file_upload.html')
            
            df.dropna(inplace=True) 
            df = df[['Mã khách hàng', 'Tên khách hàng', 'Mã PKKH',]]
            df = df.drop_duplicates(subset=['Mã khách hàng'])

            # bulk create
            orders = [
                KhachHang(
                    ma_khach_hang=row['Mã khách hàng'],
                    ten_khach_hang=row['Tên khách hàng'],
                    phan_khuc=PhanKhucKhachHang.objects.get(ma_pkkh=row['Mã PKKH']),

                )
                for _, row in df.iterrows()
            ]

            KhachHang.objects.bulk_create(orders)

            messages.success(request, "Upload và lưu dữ liệu thành công!")
        
        except Exception as e:
            messages.error(request, f"Lỗi: {str(e)}")

    return render(request, 'shop/file_upload.html')

def upload_pkkh(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        try:
            # đọc file
            if file.name.endswith('.csv'):
                df = pd.read_csv(file)
            elif file.name.endswith('.xlsx'):
                df = pd.read_excel(file)
            else:
                messages.error(request, "Chỉ hỗ trợ file CSV hoặc Excel.")
                return render(request, 'file_upload.html')
    
            required_columns = {
                                'Mã PKKH',
                                'Mô tả Phân Khúc Khách hàng'
                                }
            if not required_columns.issubset(df.columns):
                messages.error(request, "File không đủ cột yêu cầu.")
                return render(request, 'file_upload.html')
            
            df.dropna(inplace=True) 
            df = df[['Mã PKKH','Mô tả Phân Khúc Khách hàng']]
            df = df.drop_duplicates(subset=['Mã PKKH'])

            # bulk create
            orders = [
                PhanKhucKhachHang(
                    ma_pkkh=row['Mã PKKH'],
                    mo_ta_pkkh=row['Mô tả Phân Khúc Khách hàng']
                )
                for _, row in df.iterrows()
            ]
    
            PhanKhucKhachHang.objects.bulk_create(orders)

            messages.success(request, "Upload và lưu dữ liệu thành công!")
        
        except Exception as e:
            messages.error(request, f"Lỗi: {str(e)}")

    return render(request, 'shop/file_upload.html')

def delete_all_don_hang(request):
        if request.method == "POST":
            DonHang.objects.all().delete()
            messages.success(request, "Đã xóa tất cả đơn hàng thành công!")
            return redirect('viz:list_don_hang')
        return render(request, 'shop/delete_all_don_hang.html')



def detail_khach_hang(request, ma_khach_hang):
    khach_hang = get_object_or_404(KhachHang, ma_khach_hang=ma_khach_hang)
    list_don_hang = DonHang.objects.filter(ma_khach_hang=ma_khach_hang)
    data = {
        'khach_hang': khach_hang,
        'list_don_hang': list_don_hang
    }
    return render(request, 'shop/thong_ke/detail_khach_hang.html', data)

def detail_mat_hang(request, ma_mat_hang):
    mat_hang = get_object_or_404(MatHang, ma_mat_hang=ma_mat_hang)
    list_don_hang = DonHang.objects.filter(ma_mat_hang=ma_mat_hang)
    data = {
        'mat_hang': mat_hang,
        'list_don_hang': list_don_hang
    }
    return render(request, 'shop/thong_ke/detail_mat_hang.html', data)


def them_don_hang(request):
    list_khach_hang = KhachHang.objects.all()
    list_mat_hang = MatHang.objects.all()
    if request.method == 'POST':
        ma_khach_hang = request.POST.get('ma_khach_hang')
        ma_mat_hang = request.POST.get('ma_mat_hang')
        so_luong = request.POST.get('so_luong')
        # Lấy thông tin khách hàng nếu đã chọn
        if ma_khach_hang:
            try:
                selected_khach_hang = KhachHang.objects.get(ma_khach_hang=ma_khach_hang)
            except KhachHang.DoesNotExist:
                selected_khach_hang = None

        # Lấy thông tin mặt hàng nếu đã chọn
        if ma_mat_hang:
            try:
                selected_mat_hang = MatHang.objects.get(ma_mat_hang=ma_mat_hang)
            except MatHang.DoesNotExist:
                selected_mat_hang = None

        # Nếu đủ thông tin, thêm đơn hàng vào database
        if selected_khach_hang and selected_mat_hang and so_luong:
            ma_don_hang = generate_id(DonHang, 'ma_don_hang', 'ORD', 5)
            DonHang.objects.create(
                ma_don_hang=ma_don_hang,
                ma_khach_hang=selected_khach_hang.ma_khach_hang,
                khach_hang=selected_khach_hang.ten_khach_hang,
                ma_pkkh=selected_khach_hang.phan_khuc.ma_pkkh,
                mo_ta_pkkh=selected_khach_hang.phan_khuc.mo_ta_pkkh,
                ma_nhom_hang=selected_mat_hang.ma_nhom_hang.ma_nhom_hang,
                ten_nhom_hang=selected_mat_hang.ma_nhom_hang.ten_nhom_hang,
                ma_mat_hang=selected_mat_hang.ma_mat_hang,
                ten_mat_hang=selected_mat_hang.ten_mat_hang,
                don_gia=int(selected_mat_hang.don_gia),
                so_luong=int(so_luong),
                thanh_tien= int(selected_mat_hang.don_gia) * int(so_luong)
            )
            return redirect('viz:list_don_hang')
    return render(request, 'shop/don_hang/them_don_hang.html', {
        'list_khach_hang': list_khach_hang,
        'list_mat_hang': list_mat_hang
    })

def get_khach_hang_info(request, ma_khach_hang):
    try:
        khach_hang = get_object_or_404(KhachHang, ma_khach_hang=ma_khach_hang)
        data = {
            'ten_khach_hang': khach_hang.ten_khach_hang,
            'ma_pkkh': khach_hang.phan_khuc.ma_pkkh,
            'mo_ta_pkkh': khach_hang.phan_khuc.mo_ta_pkkh,
        }
    except KhachHang.DoesNotExist:
        data = {}
    return JsonResponse(data)

def get_mat_hang_info(request, ma_mat_hang):
    try:
        mat_hang = get_object_or_404(MatHang, ma_mat_hang=ma_mat_hang)
        data = {
            'ten_mat_hang': mat_hang.ten_mat_hang,
            'don_gia': mat_hang.don_gia,
            'ma_nhom_hang': mat_hang.ma_nhom_hang.ma_nhom_hang,
            'ten_nhom_hang': mat_hang.ma_nhom_hang.ten_nhom_hang,
        }
    except MatHang.DoesNotExist:
        data = {}
    return JsonResponse(data)


def visualization(request):
    # Lấy dữ liệu từ database
    queryset = DonHang.objects.all().values(
        'thoi_gian_tao_don', 'ma_don_hang', 'ma_khach_hang', 'khach_hang',
        'ma_pkkh', 'mo_ta_pkkh', 'ma_nhom_hang', 'ten_nhom_hang',
        'ma_mat_hang', 'ten_mat_hang', 'don_gia', 'so_luong', 'thanh_tien'
    )
    
    # Convert QuerySet thành list và format dữ liệu
    data = []
    for item in queryset:
        # Convert datetime thành string để serialize JSON
        formatted_item = {
            'thoi_gian_tao_don': item['thoi_gian_tao_don'].strftime("%Y-%m-%d %H:%M:%S") if item['thoi_gian_tao_don'] else None,
            'ma_don_hang': item['ma_don_hang'],
            'ma_khach_hang': item['ma_khach_hang'],
            'khach_hang': item['khach_hang'],
            'ma_pkkh': item['ma_pkkh'],
            'mo_ta_pkkh': item['mo_ta_pkkh'],
            'ma_nhom_hang': item['ma_nhom_hang'],
            'ten_nhom_hang': item['ten_nhom_hang'],
            'ma_mat_hang': item['ma_mat_hang'],
            'ten_mat_hang': item['ten_mat_hang'],
            'don_gia': item['don_gia'],
            'so_luong': item['so_luong'],
            'thanh_tien': item['thanh_tien'],
            # Thêm các trường đã mapping
            'Thời gian tạo đơn': item['thoi_gian_tao_don'].strftime("%Y-%m-%d %H:%M:%S") if item['thoi_gian_tao_don'] else None,
            'Mã đơn hàng': item['ma_don_hang'],
            'Mã mặt hàng': item['ma_mat_hang'],
            'Tên mặt hàng': item['ten_mat_hang'],
            'Mã nhóm hàng': item['ma_nhom_hang'],
            'Tên nhóm hàng': item['ten_nhom_hang'],
            'SL': item['so_luong'],
            'Đơn giá': item['don_gia'],
            'Thành tiền': item['thanh_tien'],
            'Mã khách hàng': item['ma_khach_hang'],
            'Khách hàng': item['khach_hang']
        }
        data.append(formatted_item)
    
    return render(request, 'visualization.html', {
        'data': data  # Truyền list thay vì QuerySet
    })