FROM python:3

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /usr/src/pi_alarm_clock

COPY . .

EXPOSE 8000

CMD [ "python", "main.py" ]
