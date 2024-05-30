from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from PIL import Image
import streamlit as st
import io
import os
from stegano import lsb

def encrypt_text(text, key):
    # Convert text to bytes
    text_bytes = text.encode()
    # Generate a random initialization vector (IV)
    iv = get_random_bytes(16)
    # Encrypt the text bytes
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    ct_bytes = cipher.encrypt(pad(text_bytes, AES.block_size))
    # Return encrypted text bytes and the initialization vector (IV)
    return iv + ct_bytes

def decrypt_text(ct_bytes, key):
    # Extract IV from the encrypted text bytes
    iv = ct_bytes[:16]
    ct_bytes = ct_bytes[16:]
    # Decrypt the text bytes
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    pt_bytes = unpad(cipher.decrypt(ct_bytes), AES.block_size)
    return pt_bytes.decode()

def get_user_key():
    # Prompt the user to enter an encryption/decryption key
    user_key = st.text_input("Enter the encryption/decryption key (9-digit integer):", type="password")
    if user_key and len(user_key) == 9 and user_key.isdigit():
        return user_key.zfill(16)[:16].encode()  # Zero-fill and truncate to 16 bytes
    else:
        st.warning("Please enter a valid 9-digit key.")
        return None

def hide_text_in_image(image, text, key):
    # Encrypt the text using the key
    encrypted_text = encrypt_text(text, key)
    # Convert encrypted text to hex string for hiding
    encrypted_text_hex = encrypted_text.hex()
    output_image_path = "output_image.png"
    # Hide the encrypted text in the image
    secret_image = lsb.hide(image, encrypted_text_hex)
    secret_image.save(output_image_path)
    return output_image_path

def retrieve_text_from_image(image, key):
    # Retrieve the hidden text (in hex format) from the image
    encrypted_text_hex = lsb.reveal(image)
    if encrypted_text_hex is None:
        return None
    # Convert hex string back to bytes
    encrypted_text = bytes.fromhex(encrypted_text_hex)
    try:
        # Decrypt the text using the key
        decrypted_text = decrypt_text(encrypted_text, key)
        return decrypted_text
    except Exception:
        return None


st.set_page_config(
    page_title="Security File",
    page_icon="🔐",
)
st.write("## Steganography (Hide Text in Images.)")

option = st.selectbox("Choose an option", ["Hide Text in Image", "Retrieve Text from Image"])
uploaded_file = st.file_uploader("Choose a file", type=None)
key = get_user_key()

if uploaded_file:
    file_name = uploaded_file.name


    if option == "Hide Text in Image":
        if uploaded_file.type.startswith("image/"):
            text_to_hide = st.text_area("Enter the text you want to hide in the image:")
            if text_to_hide and key:
                input_image = Image.open(uploaded_file)
                output_image_path = hide_text_in_image(input_image, text_to_hide, key)
                
                with open(output_image_path, "rb") as file:
                    st.download_button(
                        label="Download Image with Hidden Text",
                        data=file,
                        file_name="hidden_text_image.png"
                    )
                st.success("Text hidden in image successfully.")
            elif not key:
                st.warning("Please enter a valid encryption/decryption key.")
        else:
            st.warning("Please upload a valid image file.")

    elif option == "Retrieve Text from Image" and key:
        if uploaded_file.type.startswith("image/"):
            input_image = Image.open(uploaded_file)
            hidden_text = retrieve_text_from_image(input_image, key)
            if hidden_text:
                st.text_area("Retrieved Text:", hidden_text)
            else:
                st.error("Failed to retrieve text. Incorrect encryption key or no text found.")
        else:
            st.warning("Please upload a valid image file.")
    elif option == "Retrieve Text from Image" and not key:
        st.warning("Please enter a valid encryption/decryption key.")
