import json
import hashlib
import os

DB_FILE = "users_data.json"

def hash_pw(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_storage():
    if not os.path.exists(DB_FILE):
        return {"users": {}, "status": "inactive", "current_user": None}
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_storage(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

def run_app():
    data = load_storage()
    if not data["users"]:
        print("--- First Time Setup ---")
        u = input("Create Username: ")
        p = input("Create Password: ")
        data["users"][u] = hash_pw(p)
        data["height"] = int(input("Enter Height (cm): "))
        data["weight"] = int(input("Enter Weight (kg): "))
        data["BP"] = input("Enter Blood Pressure (e.g., 120/80): ")
        save_storage(data)
        print("Registration complete! Restart to login.\n")
        return

    if data["status"] == "active":
        print(f"--- Welcome back, {data['current_user']} (Auto-Logged In) ---")
        
    else:
        print("--- Please Login ---")
        u_input = input("Username: ")
        p_input = input("Password: ")

        if u_input in data["users"] and data["users"][u_input] == hash_pw(p_input):
            print("Login successful!")
            data["status"] = "active"
            data["current_user"] = u_input
            save_storage(data)
        else:
            print("Invalid credentials.")
            return
        if data["BP"] == None:
            data["BP"] = input("Enter Blood Pressure (e.g., 120/80): ")
            save_storage(data)
    print("\n[ APP MENU ]")
    print("1. View Secret Data")
    print("2. Logout (Requires password next time)")
    choice = input("Select: ")

    if choice == "2":
        data["status"] = "inactive"
        data["current_user"] = None
        save_storage(data)
        print("Logged out successfully.")

if __name__ == "__main__":
    run_app()