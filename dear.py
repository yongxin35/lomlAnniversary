import streamlit as st
from PIL import Image
import base64
from io import BytesIO


# Function to convert the image to base64
def image_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str


# Title of the app
st.markdown("<h1 style='text-align: center; color: Black;'>Happy 1st Anniversary Dear! ❤️</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: Black;'>Our Special Moments Together 💞</h3>", unsafe_allow_html=True)

# Sidebar with centered text, animated heart emoji, font size adjustments, and green box
st.sidebar.markdown("""
    <style>
    .sidebar-text {
        text-align: center;
        font-size: 22px;
        color: Black;
    }
    .bold-text {
        font-weight: bold;
    }
    .spaced-text {
        margin-bottom: 15px; /* Adjust the value as needed */
    }
    .edition-text {
        font-size: 22px; /* Adjust the font size as needed */
        position: relative;
    }
    .time-text {
        font-size: 17px; /* Adjust the font size as needed */
    }
    .heart-container {
        text-align: center; /* Centers the heart within the container */
        margin-bottom: 15px;
    }
    .heart {
        display: block;
        font-size: 35px;
        animation: beat 2s infinite;
        margin: 0 auto; /* Centers the heart horizontally */
    }
    .green-box {
        border: 3px solid #4CAF50; /* Green border color */
        border-radius: 10px; /* Rounded corners */
        padding: 10px; /* Space inside the box */
        background-color: #c8e6c9; /* Light green background */
        margin-bottom: 15px; /* Space below the box */
    }
    @keyframes beat {
        0%, 100% {
            transform: scale(1);
        }
        50% {
            transform: scale(1.2);
        }
    }
    </style>
    <div class="sidebar-text">
        <div class="bold-text">Anniversary Date Plan!</div>
        <div class="bold-text">7th September 2024</div>
        <div class="bold-text edition-text">(NS Edition🫡)</div>
    </div>
    <div class="heart-container">
        <div class="heart">❤️</div>
    </div>
    <div class="green-box">
        <div class="time-text">0630hrs - Reveille</div>
        <div class="time-text">0730hrs - Be seated at OTH</div>
        <div class="time-text">0800hrs - Graduation Parade</div>
        <div class="time-text">0930hrs - POP LO!</div>
        <div class="time-text">1200hrs - Lunch with Family</div>
        <div class="time-text">1400hrs - Switch Game Time</div>
        <div class="time-text">1700hrs - Cake Baking Date</div>
        <div class="time-text">1930hrs - Dinner Date</div>
        <div class="time-text">2100hrs - Date Night Walk </div>
        <div class="time-text">2230hrs - Lights Out</div>
    </div>
""", unsafe_allow_html=True,)

# Adding radio buttons below the green box
options = ["Yes", "No"]
selected_option = st.sidebar.radio("Routine Order (RO) / Date Approved?", options, index=None)

if selected_option == "Yes":
    st.sidebar.write("YAY, muah I LOVE YOU!")
    st.sidebar.write("See you dear, looking forward to our first anniversary!")

elif selected_option == "No":
    st.sidebar.write("Pretty Please? I planned so hard leh :(")


# Load the images
image1 = Image.open('image 1.jpg')
image4 = Image.open('image 4.jpg')
image3 = Image.open('image 3.jpg')
image5 = Image.open('image 5.jpg')
image6 = Image.open('image 6.jpg')
image7 = Image.open('image 7.jpg')
image8 = Image.open('image 8.jpg')

# Resize the images
resized_image1 = image1.resize((480, 350))
rotated_image4 = image4.rotate(-90, expand=True)
resized_image4 = rotated_image4.resize((500, 650))
resized_image3 = image3.resize((500, 730))
resized_image5 = image5.resize((500, 650))
resized_image6 = image6.resize((480, 350))
rotated_image7 = image7.rotate(90, expand=True)
resized_image7 = rotated_image7.resize((290, 190))
resized_image8 = image8.resize((500, 730))

# Convert images to base64
image1_base64 = image_to_base64(resized_image1)
image4_base64 = image_to_base64(resized_image4)
image3_base64 = image_to_base64(resized_image3)
image5_base64 = image_to_base64(resized_image5)
image6_base64 = image_to_base64(resized_image6)
image7_base64 = image_to_base64(resized_image7)
image8_base64 = image_to_base64(resized_image8)

# CSS for the image borders
image_style = """
<style>
.border-image {
    border: 10px solid #FFFFFF;  /* White border */
    border-radius: 10px;  /* Rounded corners */
    box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.2);  /* Shadow for a 3D effect */
    margin-bottom: 20px;
}
</style>
"""
st.markdown(image_style, unsafe_allow_html=True)

# Display images with borders using HTML
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown(
        f"""
        <div class="border-image">
            <img src="data:image/png;base64,{image1_base64}" style="width:100%;">
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div class="border-image">
            <img src="data:image/png;base64,{image6_base64}" style="width:100%;">
        </div>
        """,
        unsafe_allow_html=True
    )

# Display images in the second row
col3, col4, col5 = st.columns([1, 2, 1])

with col3:
    st.markdown(
        f"""
        <div class="border-image">
            <img src="data:image/png;base64,{image3_base64}" style="width:100%;">
        </div>
        """,
        unsafe_allow_html=True
    )

with col4:
    st.markdown(
        f"""
        <div class="border-image">
            <img src="data:image/png;base64,{image7_base64}" style="width:100%;">
        </div>
        """,
        unsafe_allow_html=True
    )

with col5:
    st.markdown(
        f"""
        <div class="border-image">
            <img src="data:image/png;base64,{image8_base64}" style="width:100%;">
        </div>
        """,
        unsafe_allow_html=True
    )

# Display images in the third row
col6, col7 = st.columns([1, 1])

with col6:
    st.markdown(
        f"""
        <div class="border-image">
            <img src="data:image/png;base64,{image5_base64}" style="width:100%;">
        </div>
        """,
        unsafe_allow_html=True
    )

with col7:
    st.markdown(
        f"""
        <div class="border-image">
            <img src="data:image/png;base64,{image4_base64}" style="width:100%;">
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<h5 style='text-align: center; color: Black;'>Quote of the Day: One year down, forever to go. Happy first anniversary to the love of my life!</h3>", unsafe_allow_html=True)
