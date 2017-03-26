#!/bin/bash
# fail fast after any error in commands
set -e

git checkout master

# docker build -t ferumflex/edoctor . && docker push ferumflex/edoctor
docker build -t registry.gitlab.com/ferumflex/edoctor . && docker push registry.gitlab.com/ferumflex/edoctor

now=$(date +"%Y/%m/%d")
base="Prod/$now"
tag="$base"
count=1

while true
do
  if git show-ref -q --verify "refs/tags/$tag" 2>/dev/null; then
    count=$((count+1))
    tag="${base}_${count}"
  else
    break
  fi
done

git tag -a "$tag" -m "Production $now"

git push origin master
git push origin "$tag"

git push gitlab master
git push gitlab "$tag"

docker-cloud service redeploy edoctor-web
