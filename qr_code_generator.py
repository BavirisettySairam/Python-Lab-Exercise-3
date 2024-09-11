# Installing required libraries
import pyqrcode
from PIL import Image
from pyzbar.pyzbar import decode

# Implementing the SmartScanner operation

# function for creating the qr code scanner
def smartScan_generation(user, index):
    name = user['full_name']
    email = user['email']

    qr_data = "{},{}".format(name, email)
    create_qr = pyqrcode.create(qr_data)

    # Create a unique filename for each QR code
    imagepath = f"user_{index + 1}.png"
    create_qr.png(imagepath, scale=5)

    print(f"QR code for {name} saved as {imagepath}")


users = [
    {
        "full_name": "Amit Sharma",
        "email": "amit.sharma@example.com"
    },
    {
        "full_name": "Priya Patel",
        "email": "priya.patel@example.com"
    },
    {
        "full_name": "Ravi Kumar",
        "email": "ravi.kumar@example.com"
    },
    {
        "full_name": "Sneha Reddy",
        "email": "sneha.reddy@example.com"
    },
    {
        "full_name": "Rajesh Singh",
        "email": "rajesh.singh@example.com"
    },
    {
        "full_name": "Anjali Gupta",
        "email": "anjali.gupta@example.com"
    },
    {
        "full_name": "Arjun Nair",
        "email": "arjun.nair@example.com"
    },
    {
        "full_name": "Meera Menon",
        "email": "meera.menon@example.com"
    },
    {
        "full_name": "Suresh Kumar",
        "email": "suresh.kumar@example.com"
    },
    {
        "full_name": "Neha Sharma",
        "email": "neha.sharma@example.com"
    }
]

for index, user in enumerate(users):
    smartScan_generation(user, index)


def reading_smartScan(image_path):
    from PIL import Image
    image = Image.open(image_path)
    decoded_data = decode(image)
    if not decoded_data:
        return "NO qr code found"
    return decoded_data[0].data.decode("utf-8")