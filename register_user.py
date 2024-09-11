from qr_code_generator import reading_smartScan
from smartscan_registration_module import create_user, insert_user, fetch_user_data

# Implementing User Registration Function:

# Validating the presence of correct data 
def extract_user_data(decoded_data):
    if decoded_data and "," in decoded_data:
        segment = decoded_data.split(",")
        if len(segment) == 2:
            name, email = segment
            if name and email:
                return name, email
            else:
                return None, None
        else:
            return None, None
    else:
        return None, None


# Implementing the register_from_smart_scan
def RegisterUserFromSmartScan(image_path):
    # (i) extracting the data from scanning function
    extracted_data = reading_smartScan(image_path)

    name, email = extract_user_data(extracted_data)

    if name and email:
        # (ii) using the lambda functions
        creating_user_record = create_user(full_name=name, email=email)
        insert_user(creating_user_record)
    else:
        print("Error: Invalid or incomplete user data.")