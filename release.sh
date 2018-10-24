set -ex

USERNAME=fronzbot
IMAGE=python

git pull

docker run --rm -v "$PWD":/app $USERNAME/$IMAGE
version=`cat VERSION`
echo "version: $version"

git add -A
git commit -m "version $version"
git tag -a "$version" -m "version $version"
git push
git push --tags
