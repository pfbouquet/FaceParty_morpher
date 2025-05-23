# Objectves

- [x] Install facemorpher
- [x] Run a local morph
- [x] Expose morphing through a route call on local images
  - [x] Dockerise
  - [x] Dockerise multiplatform ready (arm64 & amd64)
  - [x] Test deployment on NorthFlank with Dockerfile
- [x] Publish images on a CDN (Content Delivery Network)
  - [x] Dockerise
- [x] Make it possible to send images along the route
  - [x] Dockerise
- [ ] Make it async ready, callback to client when morph is ready
  - [ ] Dockerise

# Routes:

- POST http://127.0.0.1:8000/morph provided with {image1, image2}
  Morph 2 images and host reulst in cloudinary
  Returns: {result: Boolean, morph_url: "", morph_local_path: ""}
- POST http://127.0.0.1:8000/morph/test
  Morph 2 test images available in the test folder and return the result in tmp folder
  Returns: {result: Boolean, output_path: "app/tmp/test_result.png"}

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

## Docker

Local image (usefull for mac). Takes ~4minutes to build

- Build `docker build --platform linux/arm64 -t facemorpher-api:local .`
- Run `docker run -p 8000:8000 --env-file .env facemorpher-api:local`

Multi platform image (amd64 + arm64). Takes ~5minutes to build and push

- Build and push: `docker buildx build --platform linux/amd64,linux/arm64 -t pfbqt/facemorpher-api:latest --push .`
- Pull: `docker pull pfbqt/facemorpher-api:latest`
- Run: `docker run -p 8000:8000 --env-file .env pfbqt/facemorpher-api:latest`
