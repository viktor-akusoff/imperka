FROM python:3.11

WORKDIR /code
 
COPY ./requirements.txt /code/requirements.txt
COPY ./entrypoint.sh /code/entrypoint.sh
 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN --mount=type=secret,id=secret_key,required cp /run/secrets/secret_key /opt/secret_key

RUN --mount=type=secret,id=password,required cp /run/secrets/password /opt/password

RUN --mount=type=secret,id=username,required cp /run/secrets/username /opt/username
 
COPY ./app /code/app

EXPOSE 8000

ENTRYPOINT ["sh", "/code/entrypoint.sh" ]