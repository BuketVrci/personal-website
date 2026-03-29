

def save_email(client, email):
   
   db = client["mydatabase"]
   collection = db["email"]
   collection.insert_one({"email": email})

