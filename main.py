import qrcode
import os

# Link to your application
app_link = "https://weatherdata-energy.streamlit.app/"

# Create qr code instance
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
    box_size=10,  # size of each box in the QR code
    border=4,  # thickness of the border
)

# Add data
qr.add_data(app_link)
qr.make(fit=True)

# Create an image
img = qr.make_image(fill_color="black", back_color="white")

# Save it
img.save("C:\\Users\\tatem\Desktop\\qrcode\\Generate_Codes\\weather_data_streamlit_app.png")
