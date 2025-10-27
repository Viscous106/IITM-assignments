from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
from bs4 import BeautifulSoup
import re

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/api/outline")
def get_country_outline(country: str):
    try:
        # Fetch Wikipedia page
        url = f"https://en.wikipedia.org/wiki/{country.replace(' ', '_')}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parse HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract headings
        headings = soup.find_all(re.compile('^h[1-6]$'))

        # Generate Markdown outline
        outline = ""
        for heading in headings:
            level = int(heading.name[1])
            title = heading.get_text(strip=True).replace('[edit]', '')
            outline += f"{'#' * level} {title}\n"

        return {"outline": outline}

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=404, detail=f"Country not found or unable to fetch data: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
