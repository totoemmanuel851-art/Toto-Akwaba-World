import streamlit as st
from datetime import datetime
import requests

st.set_page_config(page_title="TOTO AKWABA", page_icon="👑", layout="wide")
st.markdown("<style>.stApp{background:#111b21;} h1,h2,h3,p,span,div{color:white!important;}</style>", unsafe_allow_html=True)

def get_meteo(ville="Abidjan"):
    try:
        r=requests.get(f"https://wttr.in/{ville}?format=j1", timeout=5).json()
        c=r['current_condition'][0]
        return f"{c['temp_C']}°C", c['weatherDesc'][0]['value'], c['humidity']
    except:
        return "28°C","Soleil Toumodi","75%"

def get_loc():
    try:
        r=requests.get("https://ipapi.co/json/", timeout=5).json()
        return r.get('city','Abidjan'), r.get('region','Toumodi'), r.get('latitude','5.36'), r.get('longitude','-4.0')
    except:
        return "Abidjan","Toumodi","5.36","-4.0"

ville, region, lat, lon = get_loc()
temp, desc, humid = get_meteo(ville)

st.title(f"👑 TOTO AKWABA WORLD V5 - {ville} {temp}")
st.caption(f"📍 {ville}, {region} | 🌤️ {temp} {desc} | 💧 {humid}%")
if st.button(f"📍 Partager ma position: {lat},{lon}"):
    st.success(f"Maps: https://maps.google.com/?q={lat},{lon}")
    st.map({"lat":[float(lat)], "lon":[float(lon)]})

if "chats" not in st.session_state:
    st.session_state.chats=[{"nom":"Maman Toumodi","msg":"Il pleut ici","ville":"Toumodi","photo":"👩🏾"},{"nom":"Groupe Yopougon","msg":"Maquis?","ville":"Yopougon","photo":"👥"}]
if "current_chat" not in st.session_state:
    st.session_state.current_chat=st.session_state.chats[0]
if "messages" not in st.session_state:
    st.session_state.messages=[{"qui":"autre","text":f"Wesh il fait {temp} à {ville}!"},{"qui":"moi","text":"Oui, on est dedans!"}]

col_g, col_d = st.columns([1,2])
with col_g:
    st.markdown(f"#### 💬 {ville}")
    st.info(f"🌤️ {temp} - {desc}")
    for chat in st.session_state.chats:
        if st.button(f"{chat['photo']} {chat['nom']}", key=chat['nom'], use_container_width=True):
            st.session_state.current_chat=chat
            st.rerun()
    if st.button("🌤️ Météo détaillée"):
        st.metric("Temp", temp)
        st.metric("Humidité", humid)

with col_d:
    st.markdown(f"### {st.session_state.current_chat['photo']} {st.session_state.current_chat['nom']} - 📍 {st.session_state.current_chat['ville']}")
    st.caption(f"📍 {ville} | 🌤️ {temp} | En ligne")
    for m in st.session_state.messages:
        if m['qui']=="moi":
            st.markdown(f"<div style='background:#005c4b; padding:10px; border-radius:10px; text-align:right; margin-left:30%;'>{m['text']}<br><small>✔️✔️ {temp}</small></div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='background:#202c33; padding:10px; border-radius:10px; margin-right:30%;'>{m['text']}</div>", unsafe_allow_html=True)
    new_msg=st.text_input("", placeholder=f"Message à {ville}...", label_visibility="collapsed")
    if st.button("Envoyer 📍+🌤️"):
        if new_msg:
            st.session_state.messages.append({"qui":"moi","text":f"{new_msg} 📍{ville} 🌤️{temp}"})
            st.rerun()

st.caption(f"TOTO AKWABA V5 | WhatsApp Killer avec Localisation + Météo {ville} {temp} 🇨🇮")
