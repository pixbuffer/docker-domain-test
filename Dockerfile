FROM python:3.6.1-onbuild
COPY stuff /usr/src/app
CMD ["python", "server.py"]
