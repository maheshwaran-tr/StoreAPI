def single_serial(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "password": user["password"]
    }

def multi_serial(userList) -> list:
    return [single_serial(user) for user in userList]