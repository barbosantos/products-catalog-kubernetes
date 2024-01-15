FROM python:3.11

# Install Chrome and dependencies
RUN apt-get update -y && \
    apt-get install -y \
    wget \
    unzip \
    libglib2.0 \
    libnss3 \
    libgconf-2-4 \
    libfontconfig1 \
    chromium-driver

# Download and install ChromeDriver
RUN wget -O /tmp/chromedriver.zip https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/120.0.6099.109/linux64/chromedriver-linux64.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    rm /tmp/chromedriver.zip

RUN ls -l /usr/local/bin/

# Set up your Python app

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app.py /code/app.py

#CMD ["python", "./products_app/main.py"]

ENTRYPOINT ["python3", "/code/app.py"]

#RUN python3 /code/app.py