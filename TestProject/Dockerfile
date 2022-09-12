FROM python:3

EXPOSE 8000


WORKDIR /TestProject

COPY . ./TestProject
RUN pip install -r ./TestProject/requirements.txt
#CMD ["uvicorn", "TestProject.api.main:app", "--host", "0.0.0.0", "--port", "80"]