FROM python:3.8-alpine
WORKDIR /echoservice
EXPOSE 8080

COPY install_requirements.txt ./echoservice.py ./wsgi.py ./run_service.sh ./
RUN pip install --no-cache-dir -r install_requirements.txt

ENTRYPOINT [ "./run_service.sh" ]
