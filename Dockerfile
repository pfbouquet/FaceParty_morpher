# syntax=docker/dockerfile:1
FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

# Installer TOUTES les dépendances système en une seule passe
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libgtk2.0-dev \
    libglib2.0-dev \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libboost-all-dev \
    libopencv-dev \
    python3.11-dev \
    git \
    curl \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  \
  # Création du lien opencv2 -> opencv4/opencv2 pour que stasm trouve ses headers
  && ln -s /usr/include/opencv4/opencv2 /usr/include/opencv2

WORKDIR /app

COPY requirements.txt .
#COPY requirements.txt ./

# Installer OpenCV Python en premier (évite certains conflits ABI)
RUN pip install --no-cache-dir opencv-python-headless

# Puis le reste des dépendances, y compris stasm
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
#COPY app/ ./app

# Exposer le port
EXPOSE 8000

# Lancer Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]