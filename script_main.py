from register_user import RegisterUserFromSmartScan
from smartscan_registration_module import fetch_user_data

def main():
    # Specify the path to the QR code images
    image_paths = [
        "user_1.png",
        "user_2.png",
        "user_3.png",
        "user_4.png",
        "user_5.png",
        "user_6.png",
        "user_7.png",
        "user_8.png",
        "user_9.png",
        "user_10.png",
    ]

    for image_path in image_paths:
        try:
            RegisterUserFromSmartScan(image_path)
        except Exception as e:
            print(f"Error registering user from {image_path}: {str(e)}")

    print("Registered users:")
    for user in fetch_user_data():
        print(f"Name: {user['full_name']}")
        print(f"Email: {user['email']}")
        print("=" * 15)

if __name__ == "__main__":
    main()