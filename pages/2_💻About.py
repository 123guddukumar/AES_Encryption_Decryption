import streamlit as st

# Set the title of the app
st.title("About")

# Define your HTML and CSS code
html_content = """
<div class="about-container">
    <h2>About This App</h2>
    <p>This app is designed to provide secure file encryption and decryption, along with steganography capabilities. Using advanced cryptographic techniques, users can protect their sensitive data from unauthorized access. Additionally, the app allows embedding hidden messages within images, ensuring confidential communication.</p>
    <div class="info">
        <h3>File Encryption/Decryption</h3>
        <p>The file encryption feature uses robust algorithms to encrypt your files, making them unreadable to anyone without the decryption key. You can easily encrypt and decrypt files to maintain the privacy and integrity of your data.</p>
        <h3>Steganography</h3>
        <p>Steganography is the practice of hiding secret messages within other non-secret messages or files. This app allows you to embed hidden messages within images, which can only be extracted using the correct key or method. This ensures secure and discreet communication.</p>
        <h3>Technologies Used</h3>
        <p><strong>Streamlit</strong>: An open-source app framework for creating data science and machine learning web applications.</p>
        <p><strong>Python Cryptography</strong>: A package designed to provide cryptographic recipes and primitives.</p>
        <p><strong>Steganography Libraries</strong>: Tools and libraries to embed and extract hidden messages within images.</p>
    </div>
</div>
"""

css_styles = """
<style>
.about-container {
    background-color: #f0f0f0;
    padding: 20px;
    border-radius: 10px;
}

.about-container h2 {
    color: #333;
}

.about-container p {
    color: #666;
}

.about-container .info {
    margin-top: 20px;
    padding: 20px;
    background-color: #e0e0e0;
    border-radius: 10px;
}

.about-container .info h3 {
    color: #333;
    margin-top: 10px;
}

.about-container .info p {
    color: #555;
    margin-top: 5px;
}
</style>
"""

# Render the HTML and CSS in the Streamlit app
st.markdown(css_styles, unsafe_allow_html=True)
st.markdown(html_content, unsafe_allow_html=True)
