FROM python:3.8
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install -U pip setuptools wheel
RUN python3 -m spacy download en_core_web_sm
COPY . /code/app 
EXPOSE 5000/tcp
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]
