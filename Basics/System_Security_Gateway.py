# SYSTEM SECURITY GATEWAY
user_profile = {
    "username": "John_son",
    "email": "johnson25@email.com",
    "account_balance": 700,
    "banned": False
}

# shows "insufficient balance" if "account balance": is below 500.
access_status = "Insufficient balance"

# check if "banned": is True or False.
if user_profile ["banned"] == True:
   access_status = "Denied Account"
   
# check if "account balance": is above or below 500.   
else:
    if user_profile ["account_balance"] >= 500:
       # shows "Granted Admin dashboard" if "account_balance": is 500 or above.
       access_status = "Granted Admin dashboard"
        
print("-------- SYSTEM SECURITY GATEWAY ------")    
print(f"\nUser: {user_profile['username']}")
print(f"\nEmail: {user_profile['email']}")
print(f"\nRESULT: {access_status}")
