import streamlit as st
import requests

# The URL for your Flask app. Update if it's hosted somewhere else.
BASE_URL = "http://127.0.0.1:5000"

def register_user():
    st.subheader("Register")
    
    # Collect user inputs
    username = st.text_input("Username", "")
    health_issues = st.text_input("Health Issues", "")
    dietary_restrictions = st.text_input("Dietary Restrictions", "")
    personal_preferences = st.text_input("Personal Preferences", "")

    # Send data to Flask backend when button is clicked
    if st.button("Register"):
        response = requests.post(f"{BASE_URL}/register", json={
            "username": username,
            "health_issues": health_issues,
            "dietary_restrictions": dietary_restrictions,
            "personal_preferences": personal_preferences
        })

        # Display response from the backend
        if response.status_code == 201:
            st.success("Registered successfully!")
        else:
            st.error("Registration failed. Please try again.")

def fetch_recipes():
    st.subheader("Get Recipes")
    user_id = st.text_input("Enter User ID", "")
    
    if st.button("Fetch Recipes"):
        response = requests.get(f"{BASE_URL}/recipes", params={"user_id": user_id})
        if response.status_code == 200:
            recipes = response.json().get("recipes", [])
            for recipe in recipes:
                st.write(recipe["name"])
        else:
            st.error("Failed to fetch recipes.")

def main():
    st.title("Personal Health Profile App")
    menu = ["Home", "Register", "Get Recipes"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.write("Welcome to the Personal Health Profile app!")
    elif choice == "Register":
        register_user()
    elif choice == "Get Recipes":
        fetch_recipes()

if __name__ == "__main__":
    main()
