🔐 Password Strength Meter / Data Encryption App
A secure data encryption and decryption web application built with Streamlit and Fernet cryptography. This tool allows you to encrypt sensitive data using a custom passkey and retrieve it securely with the correct key. Great for personal security projects and learning encryption fundamentals.



🚀 Features
🔒 Encrypt Text using your own passkey.

📦 Store Encrypted Data locally in a JSON file.

🔍 Retrieve Decrypted Text using the same passkey.

🧠 Tracks failed attempts for added security.

💾 Local key management using Fernet.

🛠️ Technologies Used
Python 3

Streamlit

cryptography (Fernet)

hashlib

JSON file storage

📦 Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/encryption-app.git
cd encryption-app
Install required packages:

bash
Copy
Edit
pip install -r requirements.txt
If requirements.txt isn't available, install manually:

bash
Copy
Edit
pip install streamlit cryptography
Run the app:

bash
Copy
Edit
streamlit run app.py
🧪 How It Works
🔐 Home
Overview of how the app works.

Instructions and illustration.

📦 Store Data
Enter a message and your own passkey.

The message gets encrypted and stored with a hashed key.

You receive an encrypted string that can be saved.

🔍 Retrieve Data
Paste the previously saved encrypted text.

Enter the same passkey used to encrypt it.

The original message will be decrypted if the key matches.

🔐 Security Notes
Uses Fernet from the cryptography package for symmetric encryption.

Stores only encrypted data and hashed passkeys (not plain text).

Tracks failed decryption attempts to prevent brute-force access.

📁 Files
app.py — Main Streamlit app.

secret.key — Auto-generated encryption key.

stored_data.json — Local encrypted data storage.

secure.png — Optional app illustration image.
