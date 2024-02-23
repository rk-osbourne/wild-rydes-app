FROM python:3.8
WORKDIR /aws-pipeline
ADD . /aws-pipeline
RUN pip install --no-cache-dir flask
EXPOSE 3000
CMD ["python", "landing_page.py"]
