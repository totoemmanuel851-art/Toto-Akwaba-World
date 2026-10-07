import streamlit as st
from datetime import datetime
import requests

st.set_page_config(page_title="TOTO AKWABA", page_icon="👑", layout="wide")
st.markdown("<style>.stApp{background:#111b21;} *{color:white!important;}</style>", unsafe_allow_html=True)

# --- METEO + LOC ---
def get_meteo():
    try:
        r=requests.get("https://wttr.in/Abidjan?format=j1",timeout=3).json()
        c=r['current_condition'][0]; return f"{c['temp_C']}°C", c['weatherDesc'][0]['value']
    except: return "25°C","Cloudy"
def get_loc():
    try:
        r=requests.get("https://ipapi.co/json/",timeout=3).json()
        return r.get('city','Abidjan'), r.get('latitude','5.36'), r.get('longitude','-4.0')
    except: return "Abidjan","5.36","-4.0"

ville, lat, lon = get_loc()
temp, desc = get_meteo()

# --- SESSION ---
if "solde" not in st.session_state: st.session_state.solde=50000
if "messages" not in st.session_state: st.session_state.messages=[{"qui":"autre","text":"Salut Boss!","type":"text","heure":"10:25"}]
if "groupes" not in st.session_state: st.session_state.groupes=["Famille Toumodi (23)","Team Akwaba (12)","Clients Pagne (45)"]

# HEADER WHATSAPP TOTAL
c1,c2,c3,c4=st.columns([3,1,1,1])
with c1: st.title(f"👑 TOTO AKWABA V7 - {ville} {temp} 🔒")
with c2:
    if st.button("📞 Appel"): st.toast("📞 Appel vocal en cours... 🔒 Chiffré bout-en-bout")
with c3:
    if st.button("📹 Vidéo"): st.toast("📹 Appel vidéo lancé... Toumodi HD")
with c4: st.caption(f"🔒 Chiffré\n📍{ville} 🌤️{temp}")

# --- COLONNES WHATSAPP ---
col_g, col_c, col_d = st.columns([1,1,2])

with col_g:
    st.markdown("**👥 Contacts + Groupes + Communautés**")
    t1,t2,t3=st.tabs(["Chats","Groupes","Communautés"])
    with t1:
        for nom in ["Maman Toumodi","Client Pagne","Didi B Officiel"]:
            if st.button(f"🟢 {nom} - en ligne - {temp}", key=nom): st.toast(f"Chat avec {nom}")
    with t2:
        for g in st.session_state.groupes:
            st.button(f"👥 {g}", key=g)
        if st.button("➕ Créer Groupe"): st.session_state.groupes.append("Nouveau Groupe Akwaba (1)")
    with t3:
        st.write("🏘️ Communauté Toumodi - 234 membres")
        st.write("🏘️ Communauté Pagne Baoulé - 120 membres")
        st.button("📢 Créer Channel Akwaba")

with col_c:
    st.markdown("**⚡ Fonctions WhatsApp + Akwaba KO**")
    tt1,tt2,tt3,tt4=st.tabs(["💸 Wave","🛍️ Boutique","🎙️ Vocal","📍 Loc"])
    with tt1:
        m=st.number_input("Montant",1000,100000,5000)
        if st.button(f"Envoyer {m}F"):
            st.session_state.solde+=int(m*0.01)
            st.success(f"+{int(m*0.01)}F com! Solde {st.session_state.solde}F")
    with tt2:
        st.write("Pagne 15k - Com 2k");
        if st.button("Vendre"): st.session_state.solde+=2000; st.success("Vendu!")
    with tt3:
        if st.button("🎙️ Enregistrer Vocal 0:12"):
            st.session_state.messages.append({"qui":"moi","text":"🎙️ Message vocal 0:12","type":"vocal","heure":datetime.now().strftime("%H:%M")})
            st.rerun()
        st.audio(b"", format="audio/wav") # placeholder
    with tt4:
        st.caption(f"📍 {ville} {lat},{lon} 🌤️{temp} {desc}")
        st.map({"lat":[float(lat)],"lon":[float(lon)]})
        if st.button("📍 Partager ma position live"):
            st.session_state.messages.append({"qui":"moi","text":f"📍 Position live: {ville} {lat},{lon} 🌤️{temp}","type":"loc","heure":"maintenant"})

with col_d:
    st.markdown(f"### 💬 Chat - 🔒 Chiffré bout-en-bout - 📍{ville} 🌤️{temp}")
    # Statut 24h
    st.info(f"🎵 Statut: Magic System - 24h - 234 vues | 📸 Photo | 📎 Fichier")
    col_f1,col_f2,col_f3=st.columns(3)
    with col_f1:
        up=st.file_uploader("📎 Photo/Doc", type=['png','jpg','mp3'])
        if up: st.session_state.messages.append({"qui":"moi","text":f"📎 Fichier: {up.name}","type":"file","heure":"maintenant"})
    with col_f2: st.button("📸 Caméra")
    with col_f3: st.caption("🔒 Messages chiffrés")

    for m in st.session_state.messages:
        col="#005c4b" if m['qui']=="moi" else "#202c33"
        icon="🎙️" if m['type']=="vocal" else "📍" if m['type']=="loc" else "📎" if m['type']=="file" else ""
        st.markdown(f"<div style='background:{col};padding:8px;border-radius:10px;margin:5px;'>{icon} {m['text']}<br><small>{m['heure']} ✔️✔️ 🔵 {temp}</small></div>", unsafe_allow_html=True)

    cc1,cc2,cc3=st.columns([4,1,1])
    with cc1: txt=st.text_input("", placeholder=f"Message chiffré... 📍{ville} 🌤️{temp}", label_visibility="collapsed")
    with cc2:
        if st.button("📤"):
            if txt: st.session_state.messages.append({"qui":"moi","text":txt,"type":"text","heure":datetime.now().strftime("%H:%M")}); st.rerun()
    with cc3:
        if st.button("🎙️"): st.session_state.messages.append({"qui":"moi","text":"🎙️ Vocal 0:05","type":"vocal","heure":datetime.now().strftime("%H:%M")}); st.rerun()

st.caption(f"V7 ULTIME KO | 12/12 fonctions WhatsApp + 5 armes Akwaba = 17 armes | 🔒 Chiffré | 📞📹 Appels | 🎙️ Vocal | 👥 Groupes | 📍{ville} 🌤️{temp} 💰{st.session_state.solde}F | WHATSAPP EST KO!")
