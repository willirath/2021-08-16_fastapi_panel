FROM continuumio/miniconda3:latest

RUN conda install -c conda-forge panel pandas

COPY ./app /app

CMD ["panel", "serve", "/app/main.py"]