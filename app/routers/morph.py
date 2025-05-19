from fastapi import APIRouter
from app.schemas.Morph import MorphPayload
from app.services.facemorph import morph

router = APIRouter(prefix="/morph", tags=["morph"])


@router.post("/")
def morph_images(payload: MorphPayload):
    print(payload)
    """ Morphing 2 images, return resulting image path """
    morph(image1_path=payload.image1_path,
          image2_path=payload.image2_path,
          output_path=payload.output_path)

    return {
        "result": True,
        "output_path": payload.output_path
    }
