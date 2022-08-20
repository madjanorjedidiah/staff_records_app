FROM python:3.8-slim as python_base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN addgroup --system appuser \
    && adduser --system --ingroup appuser appuser

USER appuser

RUN mkdir /home/appuser/staff_app

WORKDIR /home/appuser/staff_app

COPY requirements.txt /home/appuser/staff_app

USER root
RUN pip install -r /home/appuser/staff_app/requirements.txt

COPY --chown=appuser:appuser start-dev-server.sh /usr/local/bin

RUN chmod +x /usr/local/bin/start-dev-server.sh

USER appuser

COPY --chown=appuser:appuser . /home/appuser/staff_app

#CMD ["/usr/local/bin/start-dev-server.sh"]