import requests

# Replace with your actual Canva API Key
CANVA_API_KEY = "AAGdniGPkmk"
TEMPLATE_ID = "DAGdiKtwUsk"

url = f"https://api.canva.com/v1/designs/{TEMPLATE_ID}/elements"
headers = {"Authorization": f"Bearer {CANVA_API_KEY}"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Element IDs:", response.json())  # Lists all elements and their IDs
else:
    print("Error:", response.status_code, response.text)

