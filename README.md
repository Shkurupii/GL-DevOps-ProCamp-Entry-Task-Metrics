# Installation & Configuration


## Getting Started

GL-DevOps-ProCamp-Entry-Task-Metrics is designed to provide basic stats about:
* cpu
* disk
* memory
* network

GL-DevOps-ProCamp-Entry-Task-Metrics supports Python versions ``>3``.

You can easily test drive GL-DevOps-ProCamp-Entry-Task-Metrics on a modest setup
or simply on your laptop by installing it as pip package directly to your system
or by using docker container (**beta-feature**).

## Install GL-DevOps-ProCamp-Entry-Task-Metrics Locally with Pip

### Requirements
* python3
* pip

To try GL-DevOps-ProCamp-Entry-Task-Metrics locally, the best-supported currently
method is via pip, using ``venv``.

**Step 0 - Install a virtualenv**

*Mac OSX and Linux:*

```commandline
python3 -m pip install virtualenv
python3 -m virtualenv --version
```

**Step 1 - Make a venv and install GL-DevOps-ProCamp-Entry-Task-Metrics package**

*Mac OSX and Linux:*

```commandline
cd GL-DevOps-ProCamp-Entry-Task-Metrics
python3 -m virtualenv venv
python3 -m pip install .
```

## Install GL-DevOps-ProCamp-Entry-Task-Metrics Locally with Docker (BETA)

**Expected Disk and Network metrics outcome may differ at the moment. Work in progress!**

### Requirements
* docker

**Step 0 - Install a Docker**

*Mac OSX:*

    `Install Docker for Mac <https://docs.docker.com/docker-for-mac/install/>`__, which includes the Docker engine and a recent version of `docker-compose` out of the box.

*Linux:*

    `Install Docker on Linux <https://docs.docker.com/engine/install/>`__ by following Docker’s instructions for whichever flavor of Linux suits you.

**Step 1 - Build image**

```commandline
cd GL-DevOps-ProCamp-Entry-Task-Metrics
docker build -t gl-devops-procamp-entry-task-metrics:latest -t gl-devops-procamp-entry-task-metrics:0.0.1 .
```

## Run GL-DevOps-ProCamp-Entry-Task-Metrics installed with Pip

**Commands are executed either from root or with root privileges**

```commandline
GL-DevOps-ProCamp-Entry-Task-Metrics memory
GL-DevOps-ProCamp-Entry-Task-Metrics cpu
GL-DevOps-ProCamp-Entry-Task-Metrics disk
GL-DevOps-ProCamp-Entry-Task-Metrics network
```

## Run GL-DevOps-ProCamp-Entry-Task-Metrics installed with Docker

**Commands are executed either from root or with root privileges**

**Expected Disk and Network metrics outcome may differ at the moment. Work in progress!**

```commandline
docker run --rm -v /:/host:ro gl-devops-procamp-entry-task-metrics disk
docker run --rm --net=host    gl-devops-procamp-entry-task-metrics network
docker run --rm               gl-devops-procamp-entry-task-metrics cpu
docker run --rm               gl-devops-procamp-entry-task-metrics memory
```
