FROM ubuntu:latest

RUN apt-get update \
    && apt-get install -y --no-install-recommends python3 \
    && rm -rf /var/lib/apt/lists/*

ARG COMMIT=unknown
ENV COMMIT_VAR=$COMMIT

LABEL org.opencontainers.image.title="actions-experiment" \
    org.opencontainers.image.description="GitHub Actions experiment image with a Python CLI for development and testing." \
    org.opencontainers.image.source="https://github.com/izrik/actions-experiment" \
    org.opencontainers.image.revision=$COMMIT

WORKDIR /
COPY README.md /
COPY cli.py /
CMD ["sleep", "86400"]
RUN echo $COMMIT > /commit.md
