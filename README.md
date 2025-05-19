# Objectves

- [x] Install facemorpher
- [x] Run a local morph
- [x] Expose morphing through a route call on local images
  - [] Dockerise
- [] Publish images on a CDN (Content Delivery Network)
  - [] Dockerise
- [] Make it possible to send images along the route
  - [] Dockerise
- [] Make it async ready, callback to client when morph is ready
  - [] Dockerise

# Routes:

- POST http://127.0.0.1:8000/morph provided with {image1_path, image2_path, output_path}
  Morph 2 images and place result in output_path

Automatic API documentation

- http://127.0.0.1:8000/docs → Swagger UI automatique !
- http://127.0.0.1:8000/redoc → other doc format (also automatic)

# Run the app

## (local) Install requirements

Install dependencies (mac)
`brew update`
`brew install pkg-config opencv cmake`

Add to local env variable
`export OPENCV_PREFIX=$(brew --prefix opencv)`
`export PKG_CONFIG_PATH="$OPENCV_PREFIX/lib/pkgconfig"`
`export LDFLAGS="-L$OPENCV_PREFIX/lib"`
`export CPPFLAGS="-I$OPENCV_PREFIX/include/opencv4"`

Prepare pip and wheel
`pip install --upgrade pip setuptools wheel`

Install requirements from requirements.txt
`pip install -r requirements.txt`

## (local) run command line

- Running the server:
  `uvicorn app.main:app`
- Running the server when developping:
  `uvicorn app.main:app --reload`
  (the --reload wil reload the server on file change)
