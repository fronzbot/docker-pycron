set -ex

USERNAME=fronzbot
IMAGE=python

git pull origin master

version=`cat VERSION`
echo "version: $version"

git add -A
git commit -m "version $version"
git tag -a "$version" -m "version $version"
git push
git push --tags
