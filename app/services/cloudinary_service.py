import os
import cloudinary
import cloudinary.uploader
from dotenv import load_dotenv

load_dotenv()

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)


async def upload_image_to_cloudinary(image_path: str, public_id: str = None):
    try:
        response = cloudinary.uploader.upload(
            image_path,
            upload_preset="FaceParty",
            public_id=public_id
        )
        return response
    except Exception as e:
        raise RuntimeError(f"Cloudinary upload failed: {str(e)}")
