FROM python:3.11-alpine

RUN mkdir -p /shows
RUN mkdir -p /config
COPY config/ /config

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Enable your CRON task
RUN crontab /app/mycron
# Create empty log (TAIL needs this)
RUN touch /tmp/out.log

# Start TAIL - as your always-on process (otherwise - container exits right after start)
CMD python3 /app/init.py;crond && tail -f /tmp/out.log