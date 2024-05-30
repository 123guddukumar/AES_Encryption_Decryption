import streamlit as st

st.title("Developers")

# Define your HTML and CSS code
html_content = """
<div class="team-container">
    <div class="team-member">
        <img src="https://www.backblaze.com/blog/wp-content/uploads/2020/04/bb-bh-whitehat-hacker.jpg" alt="Developer 1" class="team-img">
        <h3>Guddu Kumar</h3>
        <p>Lead Developer</p>
    </div>
    <div class="team-member">
        <img src="https://www.backblaze.com/blog/wp-content/uploads/2020/04/bb-bh-whitehat-hacker.jpg" alt="Developer 2" class="team-img">
        <h3>Gursimran Singh</h3>
        <p>Frontend Developer</p>
    </div>
    <div class="team-member">
        <img src="https://www.backblaze.com/blog/wp-content/uploads/2020/04/bb-bh-whitehat-hacker.jpg" alt="Developer 3" class="team-img">
        <h3>Gurmanjot Singh</h3>
        <p>Backend Developer</p>
    </div>
    <div class="team-member">
        <img src="https://via.placeholder.com/150" alt="Developer 3" class="team-img">
        <h3>Gurmat Singh</h3>
        <p>Backend Developer</p>
    </div>
</div>
"""

css_styles = """
<style>
.team-container {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    margin-top: 20px;
    gap:50px;
}

.team-member {
    text-align: center;
    margin: 20px;
}

.team-img {
    border-radius: 50%;
    width: 200px;
    height: 200px;
}

.team-member h3 {
    margin-top: 10px;
    color: #333;
}

.team-member p {
    color: #666;
}
</style>
"""

# Render the HTML and CSS in the Streamlit app
st.markdown(css_styles, unsafe_allow_html=True)
st.markdown(html_content, unsafe_allow_html=True)
