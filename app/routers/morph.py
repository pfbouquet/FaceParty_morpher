from fastapi import APIRouter, UploadFile, File
from app.schemas.Morph import MorphPayload
from app.services.facemorph import morph
from app.services.cloudinary_service import upload_image_to_cloudinary

from fastapi.responses import JSONResponse
import shutil
import os

import uuid

TMP_DIR = "app/tmp"
os.makedirs(TMP_DIR, exist_ok=True)

router = APIRouter(prefix="/morph", tags=["morph"])


@router.post("/test")
def morph_local_images(payload: MorphPayload):
    """ Morphing 2 images, return resulting image path """
    morph(image1_path="app/test/BradPitt.jpg",
          image2_path="app/test/DwayneJohnson.jpg",
          output_path="app/tmp/test_result.png")

    return {
        "result": True,
        "output_path": payload.output_path
    }


@router.post("/")
async def morph_images(
        image1: UploadFile = File(...),
        image2: UploadFile = File(...)):

    # Save images in TMP_DIR
    image1_path = os.path.join(TMP_DIR, image1.filename)
    image2_path = os.path.join(TMP_DIR, image2.filename)

    with open(image1_path, "wb") as f1:
        shutil.copyfileobj(image1.file, f1)
    with open(image2_path, "wb") as f2:
        shutil.copyfileobj(image2.file, f2)

    try:
        # Prepare unique output filename
        unique_suffix = str(uuid.uuid4())
        public_id = f"Morph_{unique_suffix}"
        output_filename = f"{public_id}.png"
        output_path = os.path.join(TMP_DIR, output_filename)

        # Morph the images
        morph(
            image1_path=image1_path,
            image2_path=image2_path,
            output_path=output_path)

        # Upload to Cloudinary
        upload_result = await upload_image_to_cloudinary(
            image_path=output_path,
            public_id=public_id
        )
        morph_url = upload_result.get("secure_url")

        return {
            "result": True,
            "morph_url": morph_url,
            "morph_local_path": output_path
        }

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
