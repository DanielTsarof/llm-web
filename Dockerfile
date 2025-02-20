ARG MODEL_NAME=deepseek-r1:7b

# Using image with cuda and cudnn
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu20.04

# Model name
ENV MODEL_NAME=deepseek-r1:7b

# Installing python
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.11 python3.11-distutils python3.11-dev python3.11-venv

# Installing pip
RUN python3.10 -m ensurepip

# Updating pip
RUN python3.10 -m pip install --upgrade pip

RUN mkdir /app
WORKDIR /app
COPY ./src/* .

# Installing ollama
RUN curl -fsSL https://ollama.com/install.sh | sh
RUN ollama pull $MODEL_NAME

# Installing dependenses
RUN python3.10 -m pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "main.py"]
