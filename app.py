import streamlit as st
import time
from datetime import datetime

# Page Setup
st.set_page_config(page_title="HBD Fariha!", page_icon="🕯️")

# Custom Design
st.markdown("""
    <style>
    .stApp { background-color: #e3f2fd; } 
    .countdown-box {
        font-size: 25px; color: #0d47a1; text-align: center;
        background: #ffffff; padding: 15px; border-radius: 15px;
        border: 2px dashed #2196f3; font-weight: bold;
    }
    .age-fact {
        font-size: 20px; color: #1565c0; text-align: center;
        margin-top: 15px; font-weight: bold;
        background: #e1f5fe; padding: 10px; border-radius: 10px;
    }
    .wish-scroll {
        font-size: 18px; color: #0d47a1; text-align: center;
        height: 150px; overflow-y: scroll; border: 2px solid #2196f3;
        padding: 10px; border-radius: 10px;
    }
    .cake-text {
        font-size: 24px; color: #d81b60; text-align: center; font-weight: bold;
        margin-top: 15px;
    }
    .cake-img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 80% !important; /* কেক বড় করার জন্য */
        border-radius: 20px;
    }
    .make-a-wish {
        font-size: 40px; color: #ff1493; text-align: center;
        font-weight: bold; animation: blinker 1s linear infinite;
    }
    @keyframes blinker { 50% { opacity: 0; } }
    .special-wish {
        font-size: 20px; color: #1a237e; text-align: center; font-style: italic;
        background: #bbdefb; padding: 20px; border-radius: 10px; margin-top: 30px;
    }
    .footer {
        text-align: center; color: #1976d2; font-weight: bold;
        font-size: 16px; margin-top: 40px; padding-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 1. COUNTDOWN ---
birth_date = datetime(2011, 5, 3) 
target_date = datetime(2026, 5, 3) 
now = datetime.now()
diff = target_date - now

if diff.total_seconds() > 0:
    days = diff.days
    hours, remainder = divmod(diff.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    st.markdown(f'<div class="countdown-box">⏳ Time remaining for Fariha\'s Birthday: <br> {days} Days, {hours} Hours, {minutes} Minutes </div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="countdown-box">🎉 Today is Fariha\'s Special Day! 🎉</div>', unsafe_allow_html=True)

# --- 2. AGE FUN FACT ---
days_alive = (now - birth_date).days
st.markdown(f'<div class="age-fact">🌟 Fariha, you have been awesome for {days_alive:,} days! 🌟</div>', unsafe_allow_html=True)

st.balloons()

# --- 3. 100 WISHES ---
st.markdown('<p style="text-align:center; font-size:22px; color:#0d47a1; margin-top:15px;">✨ 100 Special Wishes for Fariha ✨</p>', unsafe_allow_html=True)
wishes = "".join([f"{i}. Happy Birthday to you Fariha 🎂💖<br>" for i in range(1, 101)])
st.markdown(f'<div class="wish-scroll">{wishes}</div>', unsafe_allow_html=True)

st.write("---")

# --- 4. CAKE & SURPRISE ---
if "blown" not in st.session_state:
    st.session_state.blown = False

# বড় গোলাপি কেক
st.markdown('<img src="https://giphy.com" class="cake-img">', unsafe_allow_html=True)

if not st.session_state.blown:
    st.markdown('<p class="cake-text">🕯️ Blow the candle to start the surprise...</p>', unsafe_allow_html=True)
    if st.button("Blow the Candle! 💨", use_container_width=True):
        st.session_state.blown = True
        st.rerun()
else:
    st.snow() 
    st.markdown('<p class="make-a-wish">✨ Make a Wish! ✨</p>', unsafe_allow_html=True)
    
    st.markdown('<img src="https://giphy.com" style="display:block; margin:auto; width:100%;">', unsafe_allow_html=True)
    
    time.sleep(2)
    st.markdown('<p class="cake-text">💨 Now listen to the truth...</p>', unsafe_allow_html=True)
    
    with st.empty():
        for i in range(3): 
            st.balloons()
            time.sleep(1)

    # --- PRANK MESSAGES ---
    st.error("তুই একটা কুত্তা! 🐶")
    st.warning("তুই একটা ছাগল! 🐐")
    st.info("পাগললললললললললললললললললললললললললললললললললললল! 🤪")
    
    st.success("Happy Birthday Fariha! ❤️")

    # --- SPECIAL MESSAGE ---
    st.markdown("""
        <div class="special-wish">
        "To the person who knows all my secrets and still likes me—Happy Birthday! 
        I'm so lucky to have a best friend like you. Have the best day ever! 🎉"
        </div>
    """, unsafe_allow_html=True)

    # --- SECRET MESSAGE BUTTON ---
    if st.button("🔓 Click to reveal a secret message"):
        st.info("I hope our friendship lasts forever! ❤️ Besties for life!")

# --- 5. FOOTER ---
st.markdown('<div class="footer">Made with ❤️ by your bestfriend</div>', unsafe_allow_html=True)

# Music
st.components.v1.html(
    """<iframe src="https://youtube.com" width="0" height="0" allow="autoplay"></iframe>""",
    height=0,
)
