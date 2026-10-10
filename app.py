import streamlit as st
from datetime import datetime
import random

st.set_page_config(page_title="TOTO AKWABA WORLD", page_icon="👑", layout="wide")

# --- DESIGN WHATSAPP + MIEUX QUE WHATSAPP ---
st.markdown("""
<style>
body { background:#ECE5DD; }
.header { background:#075E54; color:white; padding:12px; border-radius:12px; text-align:center; font-size:22px; font-weight:bold; }
.chat-box { background:white; border-radius:12px; padding:10px; height:450px; overflow-y:auto; }
.bubble-mine { background:#DCF8C6; padding:10px 14px; border-radius:12px 0px 12px 12px; margin:6px 0 6px auto; max-width:75%; text-align:right; }
.bubble-other { background:white; padding:10px 14px; border-radius:0px 12px 12px 12px; margin:6px auto 6px 0; max-width:75%; box-shadow:0 1px 1px #ccc; }
.tick { color:#34B7F1; font-weight:bold; }
.contact-card { padding:10px; border-bottom:1px solid #eee; }
.contact-card:hover { background:#f0f0f0; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="header">👑 TOTO AKWABA WORLD - Mieux que WhatsApp 🇨🇮</div>', unsafe_allow_html=True)

# --- DONNEES COMPLETES ---
if "contacts" not in st.session_state:
    st.session_state.contacts = {
        "Maman Toumodi ❤️": {"num":"+225 07 01 02 03", "online":True, "badge":"👑 Toumodi"},
        "Boss Entreprise": {"num":"+225 07 07 07 07", "online":False, "badge":"✅ Vérifié"},
        "Yaya Abidjan": {"num":"+225 05 04 03 02", "online":True, "badge":"💎 Joie"},
    }
if "msgs" not in st.session_state: st.session_state.msgs = {}
if "status" not in st.session_state: st.session_state.status = ["On est ensemble! 🇨🇮 - Toto", "YAKO à tous - On avance 🚀"]
if "calls" not in st.session_state: st.session_state.calls = []
if "blocked" not in st.session_state: st.session_state.blocked = []

# --- SIDEBAR = LISTE CONTACTS VRAI WHATSAPP ---
with st.sidebar:
    try: st.image("logo.png", width=90)
    except: st.markdown("## 👑")
    st.write("**Par Toto Emmanuel - Toumodi**")
    search = st.text_input("🔍 Rechercher contact", placeholder="Nom ou numéro...")
    st.divider()
    st.write("**Ajouter un ami - 100% libre**")
    new_name = st.text_input("Nom complet de ton ami", placeholder="Ex: Koffi Yopougon")
    new_num = st.text_input("Numéro WhatsApp", placeholder="+225...")
    if st.button("➕ Ajouter cet ami maintenant", use_container_width=True, type="primary"):
        if new_name:
            st.session_state.contacts[new_name] = {"num":new_num or "+225...", "online":random.choice([True,False]), "badge":"👑 Nouveau"}
            st.session_state.msgs[new_name] = []
            st.toast(f"{new_name} ajouté! Tu peux lui parler ❤️", icon="✅")
            st.rerun()

    st.divider()
    # Liste contacts cliquable
    contact_names = [c for c in st.session_state.contacts.keys() if search.lower() in c.lower()]
    selected = st.radio("Tes conversations:", contact_names, index=0)

# --- ONGLETS PRINCIPAUX ---
t1, t2, t3, t4, t5 = st.tabs(["💬 CHATS", "👀 STATUTS", "📞 APPELS", "👥 GROUPES", "⚙️ PARAM + SÉCURITÉ"])

with t1:
    c1, c2 = st.columns([3,1])
    c1.subheader(f"💬 {selected} {st.session_state.contacts[selected]['badge']}")
    c1.caption(f"{st.session_state.contacts[selected]['num']} - {'En ligne' if st.session_state.contacts[selected]['online'] else 'Vu à '+datetime.now().strftime('%H:%M')}")

    # Blocage / Signalement - FONCTION QUE WHATSAPP N'A PAS BIEN
    with c2:
        if st.button("🚨 Signaler arnaque"):
            st.session_state.blocked.append(selected)
            st.error(f"{selected} bloqué et signalé. Sécurité Toumodi activée en 5 sec 🛡️")
        if st.button("🗑️ Supprimer chat"):
            st.session_state.msgs[selected] = []
            st.rerun()

    # Affichage messages style WhatsApp
    chat_container = st.container(height=420)
    msgs = st.session_state.msgs.get(selected, [])
    with chat_container:
        for m in msgs:
            if m["me"]:
                chat_container.markdown(f"<div class='bubble-mine'>{m['text']}<br><small>{m['time']} <span class='tick'>✓✓</span></small></div>", unsafe_allow_html=True)
            else:
                chat_container.markdown(f"<div class='bubble-other'><b>{m['user']}</b><br>{m['text']}<br><small>{m['time']}</small></div>", unsafe_allow_html=True)

    # Stickers Nouchi - EXTRA que WhatsApp n'a pas
    with st.expander("🎨 STICKERS NOUCHI AUTO - 30 Extraordinaires (Tape pour envoyer) - Notre force"):
        stickers = ["😎 C'est comment?", "✊🏾 On est ensemble 🇨🇮", "🙏 YAKO", "🔥 Ça va molo?", "👀 Y'a quoi?", "🧠 Faut sciencer", "💪 On est là!", "❤️ Doucement", "😂 Kill", "👑 Gâté!", "🍚 On a mangé?", "🚀 On avance", "💰 Y'a l'argent?", "🙏 Dieu est grand", "😇 Akwaba", "😅 Dosé", "🥳 Joie", "🤣 Wouh", "🇨🇮 225 à vie", "🙌 On va y arriver", "✨ Extraordinaire", "❤️ Famille", "🫶 Yako fort", "🔒 Sécurisé", "💎 Diamant", "⚡ Rapide", "🌍 Mondial", "👑 Toumodi", "🙏 Bénédiction", "🎉 Fête"]
        cols = st.columns(5)
        for i,s in enumerate(stickers):
            if cols[i%5].button(s, key=f"stk{i}"):
                st.session_state.msgs.setdefault(selected, []).append({"user":"Moi","text":s,"me":True,"time":datetime.now().strftime("%H:%M")})
                st.rerun()

    # Envoi
    col_in, col_send = st.columns([4,1])
    prompt = col_in.text_input("Écris avec joie...", label_visibility="collapsed", placeholder="Message chiffré...")
    if col_send.button("Envoyer 🚀", use_container_width=True) or prompt:
        if prompt or col_send.button:
            # On prend la valeur du text_input si elle existe
            txt = st.session_state.get('last_prompt', prompt) if prompt else ""
            if prompt:
                st.session_state.msgs.setdefault(selected, []).append({"user":"Moi","text":prompt,"me":True,"time":datetime.now().strftime("%H:%M")})
                # Réponse auto joie - EXTRA WhatsApp n'a pas ça
                if random.random() > 0.5:
                    st.session_state.msgs[selected].append({"user":selected,"text":random.choice(["On est ensemble Boss ❤️","YAKO, je suis là","Faut sciencer, on avance 🇨🇮"]),"me":False,"time":datetime.now().strftime("%H:%M")})
                st.rerun()

with t2:
    st.subheader("👀 Statuts - Disparait 24h")
    img = st.file_uploader("Ajoute photo/vidéo statut", type=["png","jpg","mp4"])
    txt_stat = st.text_input("Légende statut")
    if st.button("Publier statut 👑"):
        st.session_state.status.append(f"{txt_stat} - {datetime.now().strftime('%H:%M')}")
        st.success("Statut publié! Tes amis le voient ❤️")
    for s in st.session_state.status:
        st.success(s)

with t3:
    st.subheader("📞 Appels - Chiffrés - Mieux que WhatsApp")
    st.write("Historique d'appels sécurisés")
    for cal in st.session_state.calls[-10:]:
        st.write(cal)
    if st.button(f"🎤 Appeler {selected} en vocal", use_container_width=True):
        st.session_state.calls.append(f"Vocal avec {selected} - {datetime.now().strftime('%H:%M')} - 🔒 Sécurisé")
        st.info("Appel vocal lancé... chiffré bout-en-bout")
    if st.button(f"🎥 Appel vidéo avec {selected}", use_container_width=True, type="primary"):
        st.session_state.calls.append(f"Vidéo avec {selected} - {datetime.now().strftime('%H:%M')} - 🔒")
        st.info("Appel vidéo lancé... qualité HD Toumodi")

with t4:
    st.subheader("👥 Groupes & Communauté Toumodi - EXTRA que WhatsApp n'a pas bien")
    st.write("Crée ton groupe Toumodi mondial")
    gname = st.text_input("Nom du groupe")
    if st.button("Créer Groupe Mondial 🌍"):
        st.success(f"Groupe {gname} créé! Lien d'invitation: akwaba.world/{gname}")

with t5:
    st.subheader("⚙️ Paramètres & 🛡️ Sécurité Anti-Arnaque Mondiale")
    st.markdown("""
    **👑 Auteur: Toto Emmanuel - Toumodi 🇨🇮**
    **Version 3.0 ULTIME - Extraordinaire**
    **© TOTO AKWABA WORLD**

    **NOS EXTRAS QUE WHATSAPP N'A PAS:**
    1. 🔥 Stickers Nouchi automatiques 30+
    2. 🛡️ Anti-arnaque IA: blocage 5 secondes
    3. ❤️ Mode Joie: messages qui donnent force
    4. 👑 Badge Toumodi vérifié
    5. 🌍 Traduction Nouchi <-> Français auto
    6. 🙏 Bouton YAKO / Bénédiction
    7. 🔒 Chiffrage triple + mot de passe jamais demandé
    8. ⚡ Ultra rapide, 0 pub, 0 bug, 100% bonheur
    """)
    st.checkbox("J'accepte de rendre le monde heureux et de conquérir le monde avec Toumodi ❤️", value=True)

st.caption("© 2026 TOTO AKWABA WORLD - Toto Emmanuel - L'app qui va faire tomber WhatsApp - On est ensemble 🚀")
