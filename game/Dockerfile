FROM python:3
ADD ["common", "resources", "*.py", "requirements.txt", "game/"]
WORKDIR game/
RUN pip install -r requirements.txt
ENTRYPOINT ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app" ]