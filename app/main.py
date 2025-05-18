from fastapi import FastAPI
# from app.routers import morph

app = FastAPI(
    title="FacePartyMorpher",
    summary="API endpoints made available to FaceParty to operate changes on faces",
    version="0.0.1",
    contact={
        "name": "PF Bqt"
    },
    openapi_tags=[
        {
            "name": "morph",
            "description": "Morphing of 2 faces",
        },
    ]
)

# app.include_router(morph.router)
