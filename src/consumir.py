import requests
import base64

# Define los datos para enviar al endpoint
data = {
    "title": "Título del post",
    "content": "Contenido del post",
    "image": "roni.jpg"  # Cambia esto por la ruta de tu imagen
}

# Lee la imagen como bytes y conviértela a base64
with open(data["image"], "rb") as file:
    image_bytes = file.read()
    image_base64 = base64.b64encode(image_bytes).decode('utf-8')

# Actualiza el campo de la imagen con su representación en base64
data["image"] = image_base64

# URL del endpoint
url = "http://127.0.0.1:9998/v1/post/"

# Realiza la solicitud POST al endpoint
response = requests.post(url, json=data)

# Verifica si la solicitud fue exitosa
if response.status_code == 201:
    print("¡La publicación se creó exitosamente!")
    print("ID de la publicación:", response.json()["data"]["id"])
    print("URL de la imagen:", response.json()["data"]["image_url"])
else:
    print("Error al crear la publicación:", response.text)
