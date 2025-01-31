# PointPlus-Rewards-web-App
PointPlus is a customer rewards system built with Streamlit and Firebase. It helps businesses track transactions, reward customers with points, and manage user accounts. Designed for my sister’s cookie business, it simplifies loyalty programs to boost customer engagement and retention.


🎯 Background Story

My sister runs a cookie company, and I wanted to help her build customer loyalty. This app was designed to allow small businesses like hers to reward their customers for repeat purchases and encourage engagement through a simple and effective points-based rewards system.

🚀 Features

User Authentication (Sign Up & Login using Firebase Authentication)

Points Management (Earn and track rewards points)

Customer Registration (Store customer details securely)

Transaction Logging (Monitor purchases and reward balances)

Admin & Settings Panel (Manage users and app settings)

🛠️ Setup & Installation

1️⃣ Clone the Repository

git clone https://github.com/yourusername/pointplus.git
cd pointplus

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Set Up Firebase

Go to Firebase Console.

Create a new project and enable Authentication & Realtime Database.

Obtain your Firebase config and store it in a .env file:

FIREBASE_API_KEY=your_api_key

FIREBASE_AUTH_DOMAIN=your_auth_domain

FIREBASE_DATABASE_URL=your_database_url

FIREBASE_STORAGE_BUCKET=your_storage_bucket

FIREBASE_MESSAGING_SENDER_ID=your_messaging_sender_id

FIREBASE_APP_ID=your_app_id

FIREBASE_MEASUREMENT_ID=your_measurement_id

Add the .env file to .gitignore to prevent exposing credentials.

4️⃣ Run the Application

streamlit run main.py

🔒 Security Best Practices

Never commit API keys to GitHub. Use .env files instead.

Set Firebase security rules to restrict unauthorized access:

{
  "rules": {
    "users": {
      "$uid": {
        ".read": "auth != null && auth.uid === $uid",
        ".write": "auth != null && auth.uid === $uid"
      }
    }
  }
}

🚧 Problems Faced

Firebase Authentication Issues: Encountered EMAIL_EXISTS and Permission Denied errors due to incorrect security rules and API misconfigurations.

Database Connection to Transactions Tab: The transactions tab is not yet connected to Firebase, preventing real-time tracking of purchases.

Updating Rewards Count: The logic for updating rewards balance based on transactions is not yet implemented.

Points Conversion to Store Credit: The feature to convert earned points into store credit has not been set up.

⏳ Things Not Yet Completed

Admin Panel Features: Implementing full admin control over users and transactions.

Rewards Redemption System: Allowing users to redeem points for discounts.

Enhanced Security Measures: Improving Firebase rules for better data protection.

Error Handling & UI Improvements: Enhancing user experience and handling more edge cases.

Database Integration for Transactions: Connecting the transactions tab with Firebase to store and retrieve data in real-time.

Reward Points Conversion Logic: Implementing a system that converts points into store credit with a configurable conversion rate.

📜 License

This project is licensed under the MIT License.

👨‍💻 Author

Developed by Sanele Mhlanga. Connect with me on GitHub.

Made with ❤️ using Streamlit & Firebase 🚀

