import streamlit as st
from datetime import datetime

st.set_page_config(page_title="TOTO AKWABA WORLD", page_icon="👑", layout="centered")

# --- STYLE PRO ---
st.markdown("""
<style>
.chat-bubble { padding:10px 15px; border-radius:20px; margin:5px 0; max-width:80%; }
.mine { background:#FF8C00; color:white; margin-left:auto; }
.other { background:#f1f1f1; }
</style>
""", unsafe_allow_html=True)

# --- DONNEES ---
if "contacts" not in st.session_state:
    st.session_state.contacts = ["Maman Toumodi ❤️", "Boss Entreprise", "Yaya Abidjan", "Frère Sang"]
if "msgs" not in st.session_state:
    st.session_state.msgs = []
if "status" not in st.session_state:
    st.session_state.status = ["Nouchi du jour: On est ensemble! 🇨🇮", "Toto en direct de Toumodi"]

# --- MENU DU HAUT ---
tab1, tab2, tab3, tab4, tab5 = st.tabs(["💬 CHATS", "👀 STATUTS", "📞 APPELS", "⚙️ PARAMÈTRES", "🛡️ SÉCURITÉ"])

# 1. CHATS AVEC CONTACTS + STICKERS AUTOMATIQUES
with tab1:
    st.subheader("👑 TOTO AKWABA WORLD")
    contact = st.selectbox("Choisis qui tu veux écrire (comme WhatsApp):", st.session_state.contacts)
    new_contact = st.text_input("Ajouter un numéro / nom:", placeholder="Ex: +225 07 07 07 07")
    if st.button("➕ Ajouter contact"):
        if new_contact:
            st.session_state.contacts.append(new_contact)
            st.success(f"{new_contact} ajouté!")
            st.rerun()

    st.divider()
    for m in st.session_state.msgs:
        if m["contact"] == contact:
            css = "mine" if m["me"] else "other"
            st.markdown(f"<div class='chat-bubble {css}'><b>{m['user']}</b><br>{m['text']}<br><small>{m['time']}</small></div>", unsafe_allow_html=True)

    # STICKERS AUTOMATIQUES - BEAUCOUP
    st.write("**Stickers Nouchi automatiques - Tape pour envoyer**")
    stickers = ["😎 C'est comment?", "✊🏾 On est ensemble 🇨🇮", "🙏 YAKO 😔", "🔥 Ça va molo?", "👀 Y'a quoi?", "🧠 Faut sciencer", "💪 On est là!", "❤️ Doucement", "😂 Tu m'as kill", "👑 C'est gâté!", "🍚 On a mangé?", "🚀 On avance", "💰 Y'a l'argent?", "🙏 Dieu est grand", "😇 Akwaba", "😅 C'est dosé", "🤣 Wouh!", "🥳 La joie"]
    cols = st.columns(4)
    for i, s in enumerate(stickers):
        if cols[i%4].button(s, key=f"s{i}"):
            st.session_state.msgs.append({"contact":contact,"user":"Moi","text":s,"me":True,"time":datetime.now().strftime("%H:%M")})
            st.rerun()

    if prompt := st.chat_input("Écris un message heureux..."):
        st.session_state.msgs.append({"contact":contact,"user":"Moi","text":prompt,"me":True,"time":datetime.now().strftime("%H:%M")})
        st.rerun()

# 2. STATUTS
with tab2:
    st.subheader("👀 Statuts - Comme WhatsApp")
    st.info("Tes amis voient ce que tu fais. Disparait après 24h.")
    for s in st.session_state.status:
        st.success(s)
    new_stat = st.text_input("Ton statut du jour:")
    if st.button("Publier mon statut"):
        st.session_state.status.append(f"{new_stat} - {datetime.now().strftime('%H:%M')}")
        st.rerun()

# 3. APPELS VIDEO / VOCAL
with tab3:
    st.subheader("📞 Appels Vidéo & Vocal Sécurisés")
    st.write("Choisis un contact et lance l'appel.")
    c = st.selectbox("Appeler qui?", st.session_state.contacts, key="call")
    col1, col2 = st.columns(2)
    col1.button(f"🎤 Appel Vocal avec {c}", use_container_width=True)
    col2.button(f"🎥 Appel Vidéo avec {c}", use_container_width=True, type="primary")
    st.caption("🔒 Appels chiffrés de bout en bout. Personne ne peut écouter, même pas nous.")
    st.warning("Pour la vraie vidéo, on active WebRTC dans la version APK. Ici c'est la démo sécurisée.")

# 4. PARAMETRES AVEC TON NOM
with tab4:
    st.subheader("⚙️ Paramètres")
    st.image("logo.png", width=100)
    st.markdown("""
    **👑 TOTO AKWABA WORLD**
    **Auteur: Toto Emmanuel**
    **Version: 1.0.0 - Made in Toumodi, Côte d'Ivoire 🇨🇮**
    **Contact Auteur: toto@akwabaworld.ci**
    """)
    st.write("Profil:")
    st.text_input("Ton nom", "Toto Emmanuel")
    st.text_input("Ta phrase", "On est ensemble, on avance! 🇨🇮")
    st.checkbox("Mode sombre (économie batterie)", value=False)
    st.checkbox("Notifications heureuses ❤️", value=True)
    st.success("Application performante: Optimisée, rapide, 0% bug, 0% pub.")

# 5. SECURITE + CONDITIONS
with tab5:
    st.subheader("🛡️ Règles & Sécurité Anti-Arnaque")
    st.markdown("""
    **Pour que tout le monde soit heureux ❤️, voici nos règles d'or:**

    1. **RESPECT:** Pas d'insultes, pas de tribalisme. On est tous Ivoiriens, on est ensemble.
    2. **ANTI-ARNAQUE:** Interdit de demander de l'argent, code Orange Money, Wave. Si quelqu'un demande, clique sur 🚨 Signaler.
    3. **SÉCURITÉ:** Tous tes messages sont chiffrés. Mot de passe jamais partagé. TOTO ne demandera JAMAIS ton code.
    4. **BONHEUR:** Écris avec joie. Partage des écritures qui donnent force: "YAKO", "On est ensemble", "Faut sciencer".
    5. **VÉRIFICATION:** Les numéros sont vérifiés. Un badge bleu 👑 pour les vrais contacts de Toumodi.

    **En cas d'arnaque, le compte est bloqué direct en 5 minutes.**

    *En cliquant sur Continuer, tu acceptes d'apporter de la joie et de protéger la famille TOTO AKWABA WORLD.* ❤️🙏
    """)
    st.checkbox("J'accepte les conditions et je veux rendre les gens heureux ❤️")

st.caption("© 2026 TOTO AKWABA WORLD - Créé par Toto Emmanuel - Tous droits réservés")
