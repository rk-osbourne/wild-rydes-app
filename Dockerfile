FROM python:3
# Set application working directory
WORKDIR /usr/src/app
# Install requirements
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
# Install application
COPY wild_rydes_app.py ./
# Run application
EXPOSE 5000
CMD ["python", "wild_rydes_app.py"]
