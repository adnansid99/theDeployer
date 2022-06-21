FROM python:3.9.9

COPY . .

RUN chmod 777 start.sh

RUN pip install -r requirements.txt

CMD ["bash", "start.sh"]
