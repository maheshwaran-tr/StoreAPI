def single_serial(product) -> dict:
    return {
        "id": str(product["_id"]),
        "name": product["name"],
        "description": product["description"],
        "quantity": product["quantity"],
        "price": product["price"],
    }

def multi_serial(productList) -> list:
    return [single_serial(product) for product in productList]