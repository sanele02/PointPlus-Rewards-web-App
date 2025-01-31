from PIL import Image
import streamlit as st
import pyrebase
from datetime import datetime
import math  # For points calculation
from streamlit_option_menu import option_menu

# CONFIG KEY
firebaseConfig = {
    #FIREBASE_API_KEY=your_api_key
#FIREBASE_AUTH_DOMAIN=your_auth_domain
#FIREBASE_DATABASE_URL=your_database_url
#FIREBASE_STORAGE_BUCKET=your_storage_bucket
#FIREBASE_MESSAGING_SENDER_ID=your_messaging_sender_id
#FIREBASE_APP_ID=your_app_id
#FIREBASE_MEASUREMENT_ID=your_measurement_id
    
}

# Initializing Firebase
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()

# Initialize session state for navigation
 
if "page" not in st.session_state:
    st.session_state.page = "home"  # Start on the home page
# HOME PAGE
if st.session_state.page == "home":
    st.title("Welcome to POINTPLUS!")
    
    # Display the banner image
    try:
        image = Image.open(r"POINTPLUS.png")  # Adjust path as needed
        st.image(image)
    except FileNotFoundError:
        st.error("The image file was not found. Please check the file path.")
    
    # Authentication Options
    auth_options = st.selectbox("Select Login or Sign Up", ["Login", "Sign Up"])

    if auth_options == 'Sign Up':
        email = st.text_input("Email Address")
        password = st.text_input("Password", type="password")
        username = st.text_input("Username")
        Ts_and_Cs= st.markdown("I agree to the [Terms and Conditions](https://example.com/terms)", unsafe_allow_html=True)
        agree = st.checkbox("I agree to the Terms and Conditions")
        submit = st.button('Create Account')
        
        if submit:
            if agree == False:
                st.warning("You must agree to proceed.")

            try:
                   
                user = auth.create_user_with_email_and_password(email, password)
                
                    
                st.success('Account has been successfully created!')
                st.balloons()
                
                # Sign in automatically after account creation
                user = auth.sign_in_with_email_and_password(email, password)
                
                # Save user details in the database
                db.child("users").child(user['localId']).set({
                    "username": username,
                    "email": email,
                    "ID": user['localId']
                })
                
                # Save user in session state
                st.session_state.user = user
                st.session_state.page = "main"
                st.session_state.username = username  # Save username for personalization
            except Exception as e:
                st.error(f"Error: {str(e)}")
    
    if auth_options == 'Login':
        email = st.text_input("Email Address")
        password = st.text_input("Password", type="password")
        login_button = st.button('Login')
        
        if login_button:
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                #log_data= {"email": email,"username":username}
                #username = db.child("users").push(log_data)
                
                # Save user in session state
                #direct user to main page
                st.session_state.user = user
                st.session_state.page = "main"
                #st.session_state.username = username
            except Exception as e:
                st.error(f"Login failed: {str(e)}")
# MAIN APP
if st.session_state.page == "main":
    st.title("Welcome back, "+ st.session_state.get('username', username))
    #st.title("Welcome back, "+ st.session_state.get('username', 'User')+" !")
    st.write("Dashboard")

    # Sidebar navigation
   
    st.logo("pointpluss_logo.png")
    st.sidebar.title("Navigation")
    st.sidebar.button("Main")   
    st.sidebar.button("Admin")
    st.sidebar.button("Settings")

    

    # Tabs
    tab1, tab2, tab3 = st.tabs(['Points Management', 'Card Setup', 'Transactions'])

    # Points Management Tab
    with tab1:
        st.header("Points Management")
        phone = st.text_input("Phone Number (for customer lookup)")
        transaction_amount = st.number_input("Enter Transaction Amount", min_value=0.0)

        if st.button("Earn Points"):
            earned_points = math.floor(transaction_amount / 50)  # Points logic
            st.write(f"Points Earned: {earned_points}")

            # Mock database interaction
            current_points = 0  # Example: replace with actual data retrieval
            updated_points = current_points + earned_points
            st.write(f"Updated Points Balance: {updated_points}")
            st.success("Points updated successfully!")

    # Card Setup Tab
    with tab2:
        st.header("Card Setup")
        name1 = st.text_input('Name')
        surname1 = st.text_input('Surname')
        email1 = st.text_input('Email Address')
        phone_number1 = st.text_input('Phone Number')
        gender1 = st.radio("Gender", ['Male', 'Female', 'Other'])
        dob1 = st.date_input(
    'Date of Birth (YYYY-MM-DD)', 
    min_value=datetime(1900, 1, 1),  # Earliest allowable date
    max_value=datetime.now()  # Latest allowable date (current date)
)
        address1 = st.text_area("Address")
        promo_opt_in1 = st.checkbox("I agree to receive promotional updates.")

        if st.button("Generate Rewards Card"):
            st.success(f"Successfully created, Rewards card generated for {name1} {surname1}!")
            customer_data = {
            'name': name1, 
            'surname':surname1,
            'email':email1,
            'phone_number':phone_number1,
            'gender':gender1, 
            "Date of Birth": dob1.strftime("%Y-%m-%d"),
            'address': address1,
            "points": 0,
            "Rewards Balance":0,
            }
            user_id = st.session_state.user['localId']
            db.child("customers").child(user_id).push(customer_data)
                
                
                
            
            st.success(f"information has been stored !")
    # Transactions Tab
    with tab3:
        st.header("Transactions")
        st.info("This section is under development.")

    # Logout Button
    if st.sidebar.button("Logout"):
        st.session_state.page = "home"  # Return to home page
        st.session_state.username = None
        st.experimental_rerun()

#settings page

if st.session_state.page == "Settings":
    st.title("Settings!")

#admin page
if st.session_state.page == "Settings":
    st.title("Admin !")