FROM python:3
ADD *.py user/
ADD requirements.txt user/
WORKDIR /
RUN pip install -r user/requirements.txt

ENTRYPOINT ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "user:create_app()" ]