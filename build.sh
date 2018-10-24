set -ex

USERNAME=fronzbot
IMAGE=python

docker build -t $USERNAME/$IMAGE:latest .
