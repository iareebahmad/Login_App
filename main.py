import streamlit as st
import bcrypt

# --- Page Config ---
st.set_page_config(page_title="CereBro Login", page_icon="🧠", layout="centered")
st.logo("logo.png")
# --- Fake in-memory user database (with bcrypt-hashed passwords) ---
users = {
    "areeb": {
        "name": "Mohammad Areeb Ahmad",
        "password": b"$2b$12$SPu0VFUGNRvZEASi2ZZ3mO8gDZZ2PAHR.6JGOFxyB7bYLKMUPUG6m"
    },
    "ironman": {
        "name": "Tony Stark",
        "password": b"$2b$12$Q2q4KwviQoovssCb82E/d.iGDnxElTuQvq4rpErocCpbneuPqMUZa"
    }
}



# Heading
st.markdown("<h1>Welcome to CereBro AI</h1>", unsafe_allow_html=True)

# Login Box
with st.container():
    st.markdown('<div class="login-container">', unsafe_allow_html=True)
    username = st.text_input("Enter your username : ")
    password = st.text_input("Enter your password : ", type="password")
    login_btn = st.button("Login")
    st.markdown('</div>', unsafe_allow_html=True)

    # Authentication Logic
    if login_btn:
        if username in users and bcrypt.checkpw(password.encode(), users[username]["password"]):
            st.success(f"✅ Welcome, {users[username]['name']}!")
        else:
            st.error("❌ Incorrect username or password.")

# footer
st.markdown("---")
st.markdown(
    '<p style="text-align:center;">Secured Login System ● Made with ❤️ by Areeb</p>',
    unsafe_allow_html=True
)
