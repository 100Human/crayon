FROM python:3.10.4

WORKDIR /opt/program

COPY app/requirements.txt .
RUN pip install -r requirements.txt

COPY app .

EXPOSE 8080
ENV SM_MODEL_DIR /opt/ml/model
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8080", "app:app", "-n"]
