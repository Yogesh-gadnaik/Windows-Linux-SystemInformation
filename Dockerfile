FROM python

WORKDIR /python-docker

COPY requirements.txt requirements.txt

# RUN pip install pypiwin32==223

RUN pip install -r requirements.txt

COPY . .

# EXPOSE 5000:5000
CMD [ "python3" , "app.py"]
# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]



