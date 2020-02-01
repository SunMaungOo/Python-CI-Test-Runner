FROM python:3
CMD mkdir /opt/source
COPY . /opt/source
WORKDIR /opt/source
CMD sudo apt update
CMD sudo apt install git
#Use -git to point to repo location
#Use -file to point to location to run
ENTRYPOINT ["python","./main.py"]
