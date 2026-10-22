from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="AutoQuote API")

# Regole di sicurezza corrette per il CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RichiestaPreventivo(BaseModel):
    targa: str
    intervento: str

@app.get("/")
def leggi_radice():
    return {"messaggio": "Il server di AutoQuote è attivo! 🚀"}

@app.post("/preventivi")
def calcola_preventivo(richiesta: RichiestaPreventivo):
    
    prezzo_base = 150
    if "frizione" in richiesta.intervento:
        prezzo_base = 650
    elif "tagliando" in richiesta.intervento:
        prezzo_base = 220
    elif "freni" in richiesta.intervento:
        prezzo_base = 110

    return {
        "targa_ricevuta": richiesta.targa.upper(),
        "intervento_richiesto": richiesta.intervento,
        "risultati": [
            {
                "nome": "Autofficina Rossi", 
                "prezzo": prezzo_base, 
                "badge": "Miglior Prezzo", 
                "km": "2.5", 
                "rating": "4.8", 
                "note": "✓ Ricambi garantiti", 
                "color": "blue"
            },
            {
                "nome": "Garage Moderna", 
                "prezzo": prezzo_base + 40, 
                "badge": "Premium", 
                "km": "4.1", 
                "rating": "4.5", 
                "note": "+ Auto di cortesia inclusa", 
                "color": "slate"
            }
        ]
    }
