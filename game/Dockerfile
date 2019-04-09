FROM python:3
ADD ["*.py", "requirements.txt", "game/"]
WORKDIR /
RUN pip install -r game/requirements.txt
ENTRYPOINT ["gunicorn", "-w", "4", "-b", "0.0.0.0:5001", "game:create_app()" ]