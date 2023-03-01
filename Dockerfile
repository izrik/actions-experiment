FROM ubuntu:latest

ARG COMMIT=unknown
ENV COMMIT_VAR=$COMMIT

WORKDIR /
COPY README.md /
CMD ["sleep", "86400"]
RUN echo $COMMIT > /commit.md
