FROM python:3.11



COPY poerty.lock /app/
COPY  pyproject.toml /app/
WORKDIR /app
RUN pip install poetry==1.5.1
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-interaction --no-ansi


COPY . /app/

EXPOSE 8000
ENTRYPOINT ["python", "manage.py", "runserver"]

