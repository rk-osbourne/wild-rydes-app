FROM python:3.8
WORKDIR /aws-pipeline
ADD . /aws-pipeline
RUN pip install --no-cache-dir flask -r requirements.txt
COPY landing_page.py ./
CMD ["python", "landing_page.py"]
