FROM python:3.7-alpine
ADD . /code/
RUN pip install -r /code/requirements.txt
CMD ["python", "/code/server_api.py"]
