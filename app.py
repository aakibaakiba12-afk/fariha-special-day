import streamlit as st
import time
from datetime import datetime

# Page Setup
st.set_page_config(page_title="HBD Fariha!", page_icon="🎂")

# Custom Design
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; } 
    .countdown-box {
        font-size: 25px; color: #d81b60; text-align: center;
        background: #f8f9fa; padding: 15px; border-radius: 15px;
        border: 2px dashed #d81b60; font-weight: bold;
    }
    .age-fact {
        font-size: 22px; color: #d81b60; text-align: center;
        margin-top: 15px; font-weight: bold;
    }
    .wish-text {
        font-size: 20px; color: #ff4081; font-weight: bold;
        text-align: center; line-height: 2.0;
        margin-bottom: 10px;
    }
    .cake-text {
        font-size: 24px; color: #d81b60; text-align: center; font-weight: bold;
        margin-top: 20px;
    }
    .special-wish {
        font-size: 20px; color: #1a237e; text-align: center; font-style: italic;
        background: #fce4ec; padding: 20px; border-radius: 10px; margin-top: 30px;
    }
    .footer {
        text-align: center; color: #880e4f; font-weight: bold;
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

# --- 3. MAGIC BALLOON BUTTON ---
if st.button("🎁 Click for Balloons! 🎈", use_container_width=True):
    st.balloons()

st.write("---")

# --- 4. 100 WISHES ---
st.markdown('<p style="text-align:center; font-size:25px; color:#d81b60;">✨ 100 Special Wishes for Fariha ✨</p>', unsafe_allow_html=True)
for i in range(1, 101):
    st.markdown(f'<p class="wish-text">{i}. Happy Birthday to you Fariha 🎂💖</p>', unsafe_allow_html=True)

st.write("---")

# --- 5. CAKE & SURPRISE ---
if "blown" not in st.session_state:
    st.session_state.blown = False
if "prank_step" not in st.session_state:
    st.session_state.prank_step = 0

cake_url = "https://giphy.com"
st.image(cake_url, use_container_width=True)

if not st.session_state.blown:
    st.markdown('<p class="cake-text">🕯️ Blow the candle to start the magic!</p>', unsafe_allow_html=True)
    if st.button("Blow the Candle! 💨", use_container_width=True):
        st.session_state.blown = True
        st.rerun()
else:
    # শব্দসহ আতশবাজি
    st.components.v1.html("""<iframe width="0" height="0" src="https://youtube.com" frameborder="0" allow="autoplay"></iframe>""", height=0)
    st.snow() 
    st.markdown('<p style="font-size: 40px; color: #ff1493; text-align: center; font-weight: bold;">✨ Make a Wish! ✨</p>', unsafe_allow_html=True)
    
    # আতশবাজি
    fireworks_url = "https://giphy.com"
    st.image(fireworks_url)
    
    st.write("---")
    st.markdown('<p class="cake-text">💨 Now listen to the truth... Click the button below!</p>', unsafe_allow_html=True)

    # এক এক ক্লিকে এক একটা মেসেজ আসার সিস্টেম
    if st.session_state.prank_step == 0:
        if st.button("Click for the first truth! 😂"):
            st.session_state.prank_step = 1
            st.rerun()
    
    if st.session_state.prank_step >= 1:
        st.error("তুই একটা কুত্তা! 🐶")
        if st.session_state.prank_step == 1:
            if st.button("Next truth? 😜"):
                st.session_state.prank_step = 2
                st.rerun()
    
    if st.session_state.prank_step >= 2:
        st.warning("তুই একটা ছাগল! 🐐")
        if st.session_state.prank_step == 2:
            if st.button("Final truth? 🤪"):
                st.session_state.prank_step = 3
                st.rerun()
    
    if st.session_state.prank_step >= 3:
        st.info("পাগললললললললললললললললললললললললললললললললললললল! 🤪")
        st.success("Happy Birthday Fariha! ❤️")
        st.markdown(f"""<div class="special-wish">"To the person who knows all my secrets and still likes me—Happy Birthday! I'm so lucky to have a best friend like you. Have the best day ever! 🎉"</div>""", unsafe_allow_html=True)
        if st.button("🔓 Click to reveal a secret message"):
            st.info("I hope our friendship lasts forever! ❤️ Besties for life!")

# --- 6. FOOTER ---
st.markdown('<div class="footer">Made with ❤️ by your bestfriend</div>', unsafe_allow_html=True)

# Background Music
st.components.v1.html("""<iframe src="https://youtube.com" width="0" height="0" allow="autoplay"></iframe>""", height=0)
