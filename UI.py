import streamlit as st
import numpy as np
import pandas as pd
import Model as md
st.title("Tư vấn chọn ngành")
gioitinh=st.selectbox('Giới tính',['NAM','NỮ'])

nguyennhan=['HỌC ĐỂ HIỂU BIẾT','LỠ TAY CHỌN',
 'MỨC THU NHẬP CỦA GIA ĐÌNH','NGUYỆN VỌNG CỦA GIA ĐÌNH',
 'NHU CẦU CAO CỦA THỊ TRƯỜNG ĐỐI VỚI NGÀNH HỌC (KHẢ NĂNG TÌM VIỆC LÀM CAO)',
 'NĂNG LỰC BẢN THÂN','SỞ THÍCH','TƯ VẤN TỪ THẦY CÔ, BẠN BÈ',
 'YÊU THÍCH CÔNG NGHỆ VÀ ĐƯỢC TƯ VẤN TỪ NGƯỜI THÂN TRONG GIA ĐÌNH.',
 'ĐĂNG KÝ ĐẠI']
Diem=['DƯỚI 5', 'TỪ 5 - DƯỚI 6.5', 'TỪ 6.5 -  DƯỚI 8', 'TỪ 8 -  DƯỚI 9','TỪ 9 - 10']
Donoitieng=['không ảnh hưởng', 'ảnh hưởng ít','ảnh hưởng nhiều','ảnh hưởng rất nhiều',
           'chọn ngành hoàn toàn dựa theo độ nổi tiếng']
nn=st.selectbox('Nguyên nhân ảnh hưởng đến việc chọn ngành',nguyennhan)
toan=st.selectbox('Điểm trung bình môn Toán',Diem)
vatly=st.selectbox('Điểm trung bình môn Vật lý',Diem)
hoa=st.selectbox('Điểm trung bình môn Hóa học',Diem)
ta=st.selectbox('Điểm trung bình môn Tiếng anh',Diem)
nv=st.selectbox('Điểm trung bình môn Ngữ văn',Diem)
ls=st.selectbox('Điểm trung bình môn Lịch sử',Diem)
dl=st.selectbox('Điểm trung bình môn Địa lý',Diem)

nt=st.selectbox('Độ nổi tiếng của trường đại học có ảnh hưởng đến quết định chọn ngành của bạn',Donoitieng)
tg=st.selectbox('Thời gian bạn tìm hiểu trước khi chọn ngành(tuần)',[1,2,3,4,5])
st.text('Sở thích')

s1=st.checkbox('DU LỊCH',value=False)
s2=st.checkbox('HỘI HỌA - MỸ THUẬT',value=False)
s3=st.checkbox('THỂ THAO',value=False)
s4=st.checkbox('THỂ THAO ĐIỆN TỬ',value=False)
s5=st.checkbox('THỜI TRANG',value=False)
s6=st.checkbox('ÂM NHẠC',value=False)
s7=st.checkbox('ĐỌC SÁCH',value=False)
s8=st.checkbox('PHIM ẢNH',value=False)
s9=st.checkbox('KHÁC',value=False)

st.text('Nguồn thông tin bạn tìm hiểu')
t1=st.checkbox('INTERNET',value=False)
t2=st.checkbox('MẠNG XÃ HỘI',value=False)
t3=st.checkbox('THẦY CÔ - BẠN BÈ',value=False)
t4=st.checkbox('TÔI NHẬN ĐƯỢC THÔNG TIN TỪ CÁC ĐỢT TƯ VẤN TUYỂN SINH CỦA CÁC TRƯỜNG ĐH',value=False)
t5=st.checkbox('TÔI ĐẾN TẬN TRƯỜNG ĐH ĐỂ TÌM HIỂU THÔNG TIN',value=False)
t6=st.checkbox('GIA ĐÌNH',value=False)
#mã hóa dữ liệu vào
if gioitinh=='NAM':
    gioitinh=0
else:
    gioitinh=1
for i in range(0,len(nguyennhan)):
    if nn==nguyennhan[i]:
        nn=i
for i in range(0,len(Diem)):
    if toan==Diem[i]:
        toan=i
    if vatly==Diem[i]:
        vatly=i
    if hoa==Diem[i]:
        hoa=i
    if ta==Diem[i]:
        ta=i
    if nv==Diem[i]:
        nv=i
    if ls==Diem[i]:
        ls=i
    if dl==Diem[i]:
        dl=i
for i in range(0,len(Donoitieng)):
    if nt==Donoitieng[i]:
        nt=i


n=np.array([gioitinh,nn,toan,vatly,hoa,ta,nv,ls,dl,nt,tg,int(s1),int(s2),int(s3),int(s4),int(s5),int(s6),int(s7),int(s8),int(s9),int(t1),int(t2),int(t3),int(t4),int(t5),int(t6)]).reshape(1,-1)
y=md.RDF(n)
sub=st.button('Dự đoán')
if sub:
    st.write(y)
   
               




