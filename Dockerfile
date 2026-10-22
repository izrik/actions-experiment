FROM ubuntu:latest

RUN apt-get update \
    && apt-get install -y --no-install-recommends python3 \
    && rm -rf /var/lib/apt/lists/*

ARG COMMIT=unknown
ENV COMMIT_VAR=$COMMIT

WORKDIR /
COPY README.md /
COPY cli.py /
CMD ["sleep", "86400"]
RUN echo $COMMIT > /commit.md
