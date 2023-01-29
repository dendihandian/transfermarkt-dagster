# NOTE: refer to the dagster docker deployment to docker: https://docs.dagster.io/deployment/guides/docker#deploying-dagster-to-docker

FROM python:3.8-slim

RUN mkdir -p /opt/dagster/dagster_home /opt/dagster/app

COPY transfermarkt-pipeline /opt/dagster/app/

RUN pip install dagster dagit

ENV DAGSTER_HOME=/opt/dagster/dagster_home/

WORKDIR /opt/dagster/app

EXPOSE 3000

ENTRYPOINT ["dagit", "-h", "0.0.0.0", "-p", "3000"]
