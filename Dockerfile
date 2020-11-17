FROM pytorch/pytorch:1.7.0-cuda11.0-cudnn8-runtime

COPY ./requirements.txt requirements.txt 
RUN pip install -r requirements.txt

RUN python -m nltk.downloader punkt 

COPY . .

CMD ["python", "server.py"]