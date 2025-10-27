# Country Information API

This is a simple web application that provides a RESTful API to fetch the outline of a Wikipedia page for a given country.

## Setup

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the application:**
    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```

## API Endpoint

### `GET /api/outline`

-   **Query Parameter:** `country` (string, required) - The name of the country.

-   **Example:**
    ```bash
    curl "http://localhost:8000/api/outline?country=Vanuatu"
    ```

-   **Success Response:**
    -   **Code:** 200 OK
    -   **Content:**
        ```json
        {
          "outline": "# Vanuatu\n\n## Contents\n# Vanuatu\n## Etymology\n## History\n### Prehistory\n..."
        }
        ```

-   **Error Response:**
    -   **Code:** 404 Not Found
    -   **Content:**
        ```json
        {
          "detail": "Country not found or unable to fetch data: ..."
        }
        ```
    -   **Code:** 500 Internal Server Error
    -   **Content:**
        ```json
        {
          "detail": "..."
        }
        ```
