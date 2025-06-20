import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import folium
from streamlit_folium import st_folium


# === إعداد الصلاحيات لـ Google Sheets ===
SCOPES = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

# === إنشاء الـ Credentials من Secret ===
# استخدم القيم من st.secrets مباشرة دون json.loads
creds_dict = st.secrets["gcp_service_account"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(dict(creds_dict), SCOPES)

# === تفعيل gspread وقراءة الشيت ===
gc = gspread.authorize(creds)
SHEET_NAME = "Your_Google_Sheet_Name"  # غيّرها باسم الشيت عندك
sheet = gc.open(SHEET_NAME).sheet1

# === واجهة Streamlit ===
st.title("Truck Router Dashboard")

# جلب البيانات من الشيت إلى DataFrame
data = sheet.get_all_records()
df = pd.DataFrame(data)

st.subheader("بيانات الشيت")
st.dataframe(df)

# === خريطة السعودية الأساسية مع نقاط البيانات إن وجدت ===
sa_center = [23.8859, 45.0792]  # مركز السعودية
m = folium.Map(
    location=sa_center,
    zoom_start=5,
    tiles="OpenStreetMap"
)

# إذا فيه إحداثيات ارسمها، وإلا اعرض الخريطة الفارغة
if not df.empty and {"lat", "lon"}.issubset(df.columns):
    for _, row in df.iterrows():
        folium.CircleMarker(
            location=[row["lat"], row["lon"]],
            radius=4,
            popup=row.get("name", ""),
            fill=True
        ).add_to(m)
else:
    st.info("لا يوجد أعمدة lat و lon لرسم نقاط — تعرض الخريطة الأساسية للسعودية فقط.")

st.subheader("خريطة السعودية")
st_folium(m, width=700, height=500)





