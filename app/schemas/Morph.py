from pydantic import BaseModel


class MorphPayload(BaseModel):
    image1_path: str
    image2_path: str
    output_path: str
