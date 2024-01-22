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

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

RUN ls -l /usr/local/bin/

# Set up your Python app

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app.py /code/app.py

#CMD ["python", "./products_app/main.py"]

ENTRYPOINT ["python3", "/code/app.py"]

#RUN python3 /code/app.py