FastAPI API Endpoint Reference

    1. /                - Shows all available commands
    2. /getSingleProduct/{product_id}
                       - Returns a single product by ID
    3. /getAll         - Returns all products in the database
    4. /addNew/{product_id}/{name}/{price}/{quantity}/{description}
                       - Adds a new product with given details
    5. /deleteOne/{product_id}
                       - Deletes product with specified ID
    6. /startsWith/{letter}
                       - Lists products starting with specified letter
    7. /panginate/{start_id}/{end_id}
                       - Returns products in a range
    8. /convert/{product_id}
                       - Converts price from USD to EUR

    ===========================================================
    FastAPI Documentation found at: https://fastapi.tiangolo.com