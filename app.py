import streamlit as st
import hashlib
from cryptography.fernet import Fernet
import json
import os


st.set_page_config("Password Strength Meter", page_icon="🔐")



# data file 
DATA_FILE = "stored_data.json"

# load file 
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                data = json.load(f)
                return data if isinstance(data, list) else []
            except json.JSONDecodeError:
                return []
    return []



KEY_FILE = "secret.key"

def load_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as key_file:
            return key_file.read()
    else:
        new_key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(new_key)
        return new_key



# key generate from fernet 
key = load_key()
cipher = Fernet(key)



# save to file 
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

stored_data = load_data()


# ================== Data Encryption ========================== 
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

def encrypt_text(text):
    return cipher.encrypt(text.encode()).decode()
    
def decrypt_text(decrypt_text):
    return cipher.decrypt(decrypt_text.encode()).decode()

def reset_attempts():
    st.session_state["failed attempts"] = 0


# =============================== Pages ===================================== 

def home_page():
    st.markdown("## 🔐 **Secure Data Encryption System Using Streamlit**")
    st.write("Welcome to your personal encryption and decryption tool. "
             "This app allows you to securely store sensitive information using encryption, "
             "and retrieve it only with a correct passkey.")
    
    # Optional image or icon
    st.markdown("---")

    st.image("secure.png")  

    st.markdown("---")
    st.subheader("🛠️ How It Works")
    st.markdown("""
    1. Go to **Store Data** to encrypt your message with a custom passkey.
    2. Save the encrypted code safely.
    3. Go to **Retrieve Data** and paste the encrypted text to decrypt it using the same passkey.
    """)

    st.markdown("---")






def store_data_page():
    st.header("📦 Store Data")
    text = st.text_area("Enter Text To Store")
    passkey = st.text_input("Enter a passkey: ", type="password")

    if st.button("Store"):
        if text and passkey:
            encrypted = encrypt_text(text)
            hashed_key = hash_passkey(passkey)

            stored_data.append({
                "encrypted": encrypted,
                "hashed_key": hashed_key
            })

            save_data(stored_data) #--- save to json

            st.success("✅ Data Stored!")
            st.write("🔒 Save this encrypted text to retrieve later:")
            st.code(encrypted)
        else:
            st.error("Please enter both text and passkey.")




def retrived_data():
    st.header("🔍 Retrieve Data")
    encrypt_input = st.text_area("Paste encrypted data:")
    passkey_input = st.text_input("Enter passkey: ", type="password")

    if st.button("Decrypt"):
        if encrypt_input and passkey_input:
            hashed_input = hash_passkey(passkey_input)
            for item in stored_data:
                if item["encrypted"] == encrypt_input and item["hashed_key"] == hashed_input:
                    decrypted = decrypt_text(encrypt_input)
                    st.success(f"✅ Decrypted data:  {decrypted}")
                    reset_attempts()
                    return
            st.session_state["failed_attempts"] = st.session_state.get("failed_attempts", 0) + 1
            remaining = 3 - st.session_state["failed_attempts"]
            st.error(f"❌ Incorrect! Attempts left: {remaining}")
            if remaining <= 0:
                st.warning("🔒 Too many failed attempts. Please reauthorize.")
                st.session_state["failed_attempts"] = 0
        else:
            st.error("Please fill in all fields.")



# ================================= Navigation ================================== 
st.sidebar.title("Menu")
option = st.sidebar.radio("Go to", ["Home", "Store Data", "Retrieve Data"])

if option == "Home":
    home_page()
elif option == "Store Data":
    store_data_page()
elif option == "Retrieve Data":
    retrived_data()

