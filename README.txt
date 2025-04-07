API ENDPOINTS DOCUMENTATION
==============================
Generated on: 2025-04-06 23:28:16

ENDPOINTS:

• GET /
  Summary: Read Root

• GET /getSingleProduct/{product_id}
  Summary: Getsingleproduct
  Parameters:
  - product_id (path): string (required)
  - q (query):  

• GET /getAll
  Summary: Getall

• GET /addNew/{product_id}/{name}/{price}/{quantity}/{description}
  Summary: Addnew
  Parameters:
  - product_id (path): string (required)
  - name (path): string (required)
  - price (path): number (required)
  - quantity (path): integer (required)
  - description (path): string (required)

• GET /deleteOne/{product_id}
  Summary: Deleteone
  Parameters:
  - product_id (path): string (required)

• GET /startsWith/{letter}
  Summary: Startswith
  Parameters:
  - letter (path): string (required)

• GET /panginate/{start_id}/{end_id}
  Summary: Paginate
  Parameters:
  - start_id (path): string (required)
  - end_id (path): string (required)

• GET /convert/{product_id}
  Summary: Convert
  Parameters:
  - product_id (path): string (required)


API DOCUMENTATION:
==============================
For interactive API documentation, visit:
1. FastAPI Docs: http://127.0.0.1:8000/docs
2. ReDoc: http://127.0.0.1:8000/redoc

For the OpenAPI schema: http://127.0.0.1:8000/openapi.json