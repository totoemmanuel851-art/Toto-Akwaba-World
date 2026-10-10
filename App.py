import streamlit.components.v1 as components
components.html("""<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4475933483972404" crossorigin="anonymous"></script>""", height=0)
import streamlit as st
from datetime import datetime
import json

st.set_page_config(page_title="TOTO AKWABA", page_icon="🏘️", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""
<style>
.stApp{background:#111b21;}
*{color:white!important;}
.msg{background:#202c33;padding:10px;border-radius:10px;margin:5px 0;}
.msg-mien{background:#00a884;margin-left:30px;}
.btn-install{background:#00a884;color:white;padding:15px;border-radius:10px;text-align:center;font-weight:bold;}
</style>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"nom":"Admin TOTO","msg":"Bienvenue à Toumodi! 👋 Ici on échange services, entraide, annonces. C'est gratuit!","heure":"10:00"},
        {"nom":"Koffi Moto","msg":"Salut, je cherche quelqu'un pour m'aider à charger mon champ demain","heure":"10:05"},
    ]
if "users" not in st.session_state: st.session_state.users = 127

# HEADER
st.markdown(f"### 🏘️ TOTO AKWABA - Toumodi | {st.session_state.users} membres en ligne")
st.markdown("Échangez, entraidez, vendez entre vous. 100% gratuit pour commencer.")

tab1, tab2, tab3 = st.tabs(["💬 Échanges", "📢 Annonces", "👤 Installer l'App"])

with tab1:
    st.markdown("#### Fil d'échange Toumodi")
    for m in st.session_state.messages[-20:]:
        css = "msg-mien" if m["nom"]=="Toi" else "msg"
        st.markdown(f'<div class="msg {css}"><b>{m["nom"]}</b> <small>{m["heure"]}</small><br>{m["msg"]}</div>', unsafe_allow_html=True)
    
    st.divider()
    col1,col2 = st.columns([3,1])
    with col1:
        new_msg = st.text_input("Ton message", placeholder="Ex: Je peux aider pour le champ demain", label_visibility="collapsed")
    with col2:
        if st.button("Envoyer", use_container_width=True):
            if new_msg:
                st.session_state.messages.append({"nom":"Toi","msg":new_msg,"heure":datetime.now().strftime("%H:%M")})
                st.rerun()

with tab2:
    st.markdown("#### Annonces du village - Gratuit")
    with st.form("annonce"):
        nom = st.text_input("Ton nom")
        type_annonce = st.selectbox("Type", ["Coup de main", "Moto/Transport", "Vente maison/terrain", "Cherche travail", "Autre"])
        detail = st.text_area("Détails")
        submit = st.form_submit_button("Publier gratuitement")
        if submit:
            st.session_state.messages.append({"nom":f"{nom} - {type_annonce}","msg":f"📢 {detail}","heure":datetime.now().strftime("%H:%M")})
            st.success("Annonce publiée! Tout Toumodi la voit.")

with tab3:
    st.markdown("### 📲 Comment installer TOTO AKWABA sur ton téléphone")
    st.markdown("""
    <div class="btn-install">INSTALLATION EN 5 SECONDES - GRATUIT - SANS PLAY STORE</div>
    """, unsafe_allow_html=True)
    st.markdown("""
    **Sur Android (Chrome):**
    1. Clique sur les 3 points en haut à droite ⋮
    2. Clique **"Installer l'application"** ou **"Ajouter à l'écran d'accueil"**
    3. L'app s'installe comme WhatsApp! L'icône apparaît!
    
    **Sur iPhone (Safari):**
    1. Clique sur le bouton Partage ⬆️
    2. Clique **"Sur l'écran d'accueil"**
    
    Après ça, tes amis n'ont plus besoin d'aller sur internet. Ils cliquent sur l'icône TOTO AKWABA!
    
    **C'est une PWA - C'est la méthode que Facebook a utilisé au début pour éviter Play Store!**
    """)
    st.link_button("📤 Partager le lien de l'app sur WhatsApp", "https://wa.me/?text=Installe%20TOTO%20AKWABA%20-%20L'app%20de%20Toumodi%20pour%20échanger:%20https://toto-akwaba-world.streamlit.app")
    st.metric("Membres", f"{st.session_state.users}", "+12 aujourd'hui")

st.caption("V9 Échange | Toumodi | Version installable - Sans argent, sans Play Store")
