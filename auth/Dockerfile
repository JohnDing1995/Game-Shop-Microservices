FROM python:3
ADD ["*.py", "requirements.txt", "auth/"]
WORKDIR auth/
RUN pip install -r requirements.txt
ENTRYPOINT ["gunicorn", "-w", "4", "-b", "0.0.0.0:6000", "app:app" ]