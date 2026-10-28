# SYSTEM SECURITY GATEWAY
user_profile = [
   {"username": "John_son",
    "email": "johnson25@email.com",
    "account_balance": 700,
    "banned": False},
   {"username": "Bernard_11",
    "email": "bernard56@email.com",
    "account_balance": 500,
    "banned": False},
   {"username": "Andy",
    "email": "andy7345@email.com",
    "account_balance": 200,
    "banned": False},
   {"username": "Parker_88",
    "email": "parker122@email.com",
    "account_balance": 800,
    "banned": True},
   {"username": "Jonathan_02",
    "email": "jonathan21@email.com",
    "account_balance": 100,
    "banned": False},
]

print("------- SYSTEM SECURITY GATEWAY ------")
for user in user_profile:
    # check if "banned": is True or False.
    if user ["banned"] == True:
     access_status = "Denied Account!"
  # check if "account balance": is above or below 500.
    else:
        if user ["account_balance"] >= 500:
         # shows "Granted Admin dashboard" if "account_balance": is 500 or above.
           access_status = "Granted Admin dashboard"
        else:
            # shows "Insufficient balance" if "account_balance": is below 500.
            access_status = "Insufficient balance!"   
    print("_______________________________________")     
    print(f"\nUser: {user['username']}")
    print(f"\nEmail: {user['email']}")
    print(f"\nRESULT: {access_status}")
print("_______________________________________") 
