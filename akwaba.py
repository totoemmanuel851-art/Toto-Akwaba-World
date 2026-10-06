import streamlit as st, json, os, time, base64
from datetime import datetime, timedelta

st.set_page_config(page_title="TOTO AKWABA WORLD", page_icon="🌍", layout="wide")

# --- DOSSIERS ---
os.makedirs("uploads", exist_ok=True)

def charger():
    if os.path.exists("data.json"):
        try:
            with open("data.json","r",encoding="utf-8") as f: return json.load(f)
        except: return {"posts":[],"statuts":[]}
    return {"posts":[],"statuts":[]}

def sauver(d):
    with open("data.json","w",encoding="utf-8") as f: json.dump(d,f,ensure_ascii=False, indent=2)

def save_file(uploaded):
    if uploaded:
        path = f"uploads/{int(time.time())}_{uploaded.name}"
        with open(path,"wb") as f: f.write(uploaded.getbuffer())
        return path
    return None

data = charger()

# Nettoyer vieux statuts >24h
data["statuts"] = [s for s in data["statuts"] if datetime.now() - datetime.fromisoformat(s["time"]) < timedelta(hours=24)]

st.markdown("""
<style>
.stApp{background:#0f0f0f; color:white}
.header{background:linear-gradient(135deg,#FF8C00,#FFD700,#075E54);color:white;padding:20px;border-radius:20px;text-align:center}
.bubble{max-width:75%;padding:12px 16px;border-radius:18px;margin:8px 0;font-size:15px; color:#000}
.bubble-me{background:#DCF8C6;margin-left:auto;border-bottom-right-radius:4px}
.bubble-other{background:white;margin-right:auto;border-bottom-left-radius:4px}
.status-circle{width:60px;height:60px;border-radius:50%;border:3px solid #FF8C00;padding:2px;object-fit:cover}
</style>
<div class='header'>
<h2>🌍 TOTO AKWABA WORLD - PRO MAX 👑</h2>
<p>💬 Chat • 📸 Photos • 🎥 Vidéos • 🟢 Statuts • 🔒 Privé</p>
</div>
""", unsafe_allow_html=True)

# --- SIDEBAR LOGIN ---
with st.sidebar:
    st.markdown("### 🌍 AKWABA !")
    pseudo = st.text_input("Ton nom", placeholder="Toto")
    tel = st.text_input("WhatsApp", placeholder="07 XX XX XX XX")
    st.divider()
    if pseudo:
        st.success(f"Connecté: {pseudo} 🟢")
        st.markdown(f"**{len(data['posts'])}** messages | **{len(data['statuts'])}** statuts")

if not pseudo:
    st.info("👈 Clique sur >> et entre ton nom - AKWABA WORLD t'attend !")
    st.stop()

# --- TABS PRINCIPAUX ---
tab1, tab2, tab3 = st.tabs(["💬 CHAT MONDE", "🟢 STATUTS 24H", "🔒 DISCUSSION PRIVÉE"])

with tab1:
    st.markdown("#### 🌍 Tout le monde parle ici")
    # Afficher messages
    for p in data["posts"][-100:]:
        if p.get("prive"): continue # pas afficher privé ici
        cls = "bubble-me" if p["pseudo"]==pseudo else "bubble-other"
        media_html = ""
        if p.get("image"):
            if os.path.exists(p["image"]):
                st.markdown(f"<div class='bubble {cls}'><b>{p['pseudo']}</b><br>{p['texte']}", unsafe_allow_html=True)
                st.image(p["image"], width=300)
                st.markdown(f"<small>{p['heure']} ✓✓</small></div>", unsafe_allow_html=True)
                continue
        if p.get("video"):
            if os.path.exists(p["video"]):
                st.markdown(f"<div class='bubble {cls}'><b>{p['pseudo']}</b><br>{p['texte']}", unsafe_allow_html=True)
                st.video(p["video"])
                st.markdown(f"<small>{p['heure']} ✓✓</small></div>", unsafe_allow_html=True)
                continue
        
        st.markdown(f"<div class='bubble {cls}'><b>{p['pseudo']} {p.get('pays','')}</b><br>{p['texte']}<br><small>{p['heure']} ✓✓</small></div>", unsafe_allow_html=True)

    st.divider()
    c1,c2,c3 = st.columns([4,1,1])
    with c1: msg = st.text_input("msg", placeholder="Écris un message...", label_visibility="collapsed", key="world_msg")
    with c2: up = st.file_uploader("📸", type=["jpg","png","jpeg","mp4","mov"], label_visibility="collapsed", key="world_up")
    with c3: send = st.button("🚀 Envoyer", use_container_width=True, key="send_world")
    
    if send and (msg or up):
        path = save_file(up)
        new_post = {"pseudo":pseudo,"texte":msg,"heure":datetime.now().strftime("%H:%M"),"time":datetime.now().isoformat(),"id":time.time()}
        if path:
            if up.type.startswith("video"): new_post["video"]=path
            else: new_post["image"]=path
        data["posts"].append(new_post)
        sauver(data); st.rerun()

with tab2:
    st.markdown("#### 🟢 Statuts - Ils disparaissent après 24h comme WhatsApp")
    # Afficher statuts
    cols = st.columns(6)
    for i, s in enumerate(data["statuts"][-12:]):
        with cols[i % 6]:
            if s.get("image") and os.path.exists(s["image"]):
                st.image(s["image"], caption=f"{s['pseudo']} - {s['heure']}", use_container_width=True)
            if s.get("video") and os.path.exists(s["video"]):
                st.video(s["video"])
                st.caption(f"{s['pseudo']} - {s['heure']}")
            if s.get("texte") and not s.get("image"):
                st.markdown(f"**{s['pseudo']}**\n\n{s['texte']}\n\n*{s['heure']}*")

    st.divider()
    st.markdown("**Ajoute ton statut :**")
    s_text = st.text_input("Ton statut (texte)", placeholder="Je suis à San-Pedro... 🌴")
    s_file = st.file_uploader("Photo/Vidéo pour statut", type=["jpg","png","jpeg","mp4"], key="status_up")
    if st.button("🟢 Publier mon statut"):
        path = save_file(s_file)
        new_s = {"pseudo":pseudo,"texte":s_text,"heure":datetime.now().strftime("%H:%M"),"time":datetime.now().isoformat(),"id":time.time()}
        if path:
            if s_file.type.startswith("video"): new_s["video"]=path
            else: new_s["image"]=path
        data["statuts"].append(new_s)
        sauver(data); st.success("Statut publié ! 🟢"); st.rerun()

with tab3:
    st.markdown("#### 🔒 Discussion privée - Choisis quelqu'un")
    all_users = list(set([p["pseudo"] for p in data["posts"] if p["pseudo"]!=pseudo]))
    if not all_users:
        st.info("Personne n'a encore parlé. Invite tes amis !")
    else:
        destinataire = st.selectbox("Tu veux parler à qui en privé ?", all_users)
        # afficher conversation privée entre pseudo et destinataire
        conv = [p for p in data["posts"] if p.get("prive") and ((p["pseudo"]==pseudo and p["dest"]==destinataire) or (p["pseudo"]==destinataire and p["dest"]==pseudo))]
        for p in conv[-50:]:
            cls = "bubble-me" if p["pseudo"]==pseudo else "bubble-other"
            st.markdown(f"<div class='bubble {cls}'><b>{p['pseudo']}</b><br>{p['texte']}<br><small>{p['heure']} 🔒</small></div>", unsafe_allow_html=True)
        
        c1,c2 = st.columns([4,1])
        with c1: p_msg = st.text_input("priv", placeholder=f"Message privé à {destinataire}...", label_visibility="collapsed", key="priv_msg")
        with c2: p_send = st.button("🔒 Envoyer", key="send_priv")
        if p_send and p_msg:
            data["posts"].append({"pseudo":pseudo,"dest":destinataire,"texte":p_msg,"heure":datetime.now().strftime("%H:%M"),"time":datetime.now().isoformat(),"prive":True,"id":time.time()})
            sauver(data); st.rerun()
