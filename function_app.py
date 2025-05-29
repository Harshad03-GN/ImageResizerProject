from azure.storage.blob import BlobServiceClient
from PIL import Image
from io import BytesIO
import os

connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
if not connection_string:
    raise Exception("AZURE_STORAGE_CONNECTION_STRING environment variable not set")

container_name = "input-images"
output_container_name = "output-images"

blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service_client.get_container_client(container_name)
output_container_client = blob_service_client.get_container_client(output_container_name)

def resize_image(blob_name):
    # Download image from Blob Storage
    blob_client = container_client.get_blob_client(blob_name)
    blob_data = blob_client.download_blob()
    image = Image.open(BytesIO(blob_data.readall()))

    image = image.resize((800, 600))  # Example size

    output = BytesIO()
    image.save(output, format="JPEG")
    output.seek(0)

    output_blob_name = f"resized_{blob_name}"
    output_blob_client = output_container_client.get_blob_client(output_blob_name)
    output_blob_client.upload_blob(output, overwrite=True)

    print(f"Resized image uploaded as {output_blob_name}")

# Example usage
resize_image("example.jpg")
