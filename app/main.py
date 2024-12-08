import openai
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Verificar si la clave de la API está disponible
api_key = os.getenv("OPENAI_API_KEY")
