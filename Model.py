import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

df=pd.read_csv('khaosat.csv',delimiter=';')
#Tạo từ điển chứa tên các ngành học 
c,u=np.unique(df.nganh,return_counts=True)
dic={}
for i in range(0,len(c)):
  dic[i]=c[i]

#chuẩn hóa cột dữ liệu nguyennhan với các cột là từng nguyên nhân riêng biệtbiệt
nn=[]
n1='INTERNET' 
n2='MẠNG XÃ HỘI'
n3='THẦY CÔ - BẠN BÈ' 
n4='TÔI NHẬN ĐƯỢC THÔNG TIN TỪ CÁC ĐỢT TƯ VẤN TUYỂN SINH CỦA CÁC TRƯỜNG ĐH'
n5='TÔI ĐẾN TẬN TRƯỜNG ĐH ĐỂ TÌM HIỂU THÔNG TIN' 
n6='GIA ĐÌNH'
for i in range(0,len(df.nguonthongtin)):
  N1=N2=N3=N4=N5=N6=0
  n=df.iloc[i,11]
  if n1 in n:
    N1=1
  if n2 in n:
    N2=1
  if n3 in n:
    N3=1
  if n4 in n:
    N4=1   
  if n5 in n:
    N5=1     
  if n6 in n:
    N6=1
  nn.append([N1,N2,N3,N4,N5,N6])
na=[n1,n2,n3,n4,n5,n6]
nn=pd.DataFrame(nn,columns=na)

#Chuẩn hóa cột dữ liệu sothich thành khung dữ liệu với các cột là từng sở thích riêng biệtbiệt
a='DU LỊCH'
b='HỘI HỌA - MỸ THUẬT'
c='THỂ THAO'
d='THỂ THAO ĐIỆN TỬ'
e='THỜI TRANG'
f='ÂM NHẠC'
g='ĐỌC SÁCH'
h='PHIM ẢNH'
k1='GAME'
k2='CHỤP ẢNH'
k3='DANCING'
k4='BIÊN TẬP VIÊN'
k5='PHÓNG VIÊN'
k6='KIẾN TRÚC'
k7='VIẾT'
k8='MOTO'
k9='UỐNG TRÀ'

st=[]
for i in range(0,len(df.sothich)):
  A=B=C=D=E=F=G=H=K=0
  t=df.iloc[i,1]
  if a in t:
    A=1
  if b in t:
    B=1
  if c in t:
    C=1
  if d in t:
    D=1
  if e in t:
    E=1
  if f in t:
    F=1
  if g in t:
    G=1
  if h in t:
    H=1  
  if k1 in t or k2 in t or k3 in t or k4 in t or k5 in t or k6 in t or k7 in t or k8 in t or k9 in t:
    K=1 
  st.append([A,B,C,D,E,F,G,H,K])
k='KHÁC'
name=[a,b,c,d,e,f,g,h,k]
st=pd.DataFrame(st,columns=name)
#Mã hóa khung dữ liệu 
df=df.apply(LabelEncoder().fit_transform)
#nối khung dữ liệu df với khung nguyennhan và sothich
df=pd.concat([df,st,nn],axis=1)

#tạo mẫu giả 
c,u=np.unique(df.nganh,return_counts=True)
t=[]
for i in range(0,len(u)):
  if u[i]==1:
    t.append(c[i])

def taomaugia(dt):
  
  if dt.gioitinh==0:
    dt.__setitem__('gioitinh',1)
  else:
     dt.__setitem__('gioitinh',0)
  return dt

ele=[]
for i in range(0,len(df)):
  dt=df.iloc[i,:]
  if dt.nganh in t:
    m=taomaugia(dt)
    ele.append(m)

d=pd.DataFrame(ele)
df=pd.concat([df,d])

#Lấy X,y
X=df.iloc[:,[0,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]]
y=df.nganh

#Tăng số mẫu dữ liệu thiểu số
from imblearn.over_sampling import SMOTE
smote = SMOTE(k_neighbors=1, random_state=0)
X, y = smote.fit_resample(X,y)


#Huấn luyện mô hình RandomForest
rdf=RandomForestClassifier(n_estimators=100)
rdf.fit(X,y)
def RDF(n):
   yd=int(rdf.predict(n))
   y=dic[yd]
   return y










