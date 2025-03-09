ARG MODEL_NAME=deepseek-r1:7b

FROM nvidia/cuda:12.0.1-runtime-ubuntu20.04

ENV MODEL_NAME=deepseek-r1:7b
ENV DEBIAN_FRONTEND=noninteractive

# Установка всех зависимостей в одном RUN-блоке
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    software-properties-common \
    bash \
    curl && \
    add-apt-repository -y ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.11 python3.11-distutils python3.11-venv && \
    python3.11 -m ensurepip && \
    python3.11 -m pip install --upgrade pip && \
    rm -rf /var/lib/apt/lists/*

# Создание рабочей директории и копирование файлов
RUN mkdir -p /app
WORKDIR /app
COPY ./src/* ./
COPY requirements.txt ./

# Установка Ollama и зависимостей
RUN curl -fsSL https://ollama.com/install.sh | sh
#RUN ollama pull $MODEL_NAME

# Installing dependenses
RUN python3.11 -m pip install -r requirements.txt

EXPOSE 5000

# Явный сброс entrypoint и указание полного пути к Python
ENTRYPOINT []
CMD ["/usr/bin/python3.11", "main.py"]
#CMD ["bin/bash"]
