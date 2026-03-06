from google import genai
from dotenv import load_dotenv
load_dotenv()

client = genai.Client()

response = client.models.generate_content(
    model="Gemini 3.1 Flash Lite",
    contents="What is the colour of italy flag? answer in one word",
)

print(response.text)