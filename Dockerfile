FROM python:3.9
COPY ./Scores.txt /app/
COPY ./*.py /app/
COPY ./tests/* /app/tests/
RUN pip install -f requirements.txt
EXPOSE 5000
CMD python MainGame.py