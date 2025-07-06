import streamlit_authenticator as stauth

# Storing Passwords as List
passwords = ["areeb123","tony123"]

# Hashing the plain text password into has value
hashed_pass = stauth.Hasher(passwords).generate()

# Output the hashes
for hashed in hashed_pass:
    print(hashed)