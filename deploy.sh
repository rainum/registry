#!/bin/bash
# fail fast after any error in commands
set -e

git checkout master

# docker build -t ferumflex/edoctor . && docker push ferumflex/edoctor
export DOCKER_HOST=tcp://ferumflex.hopto.org:2376 DOCKER_TLS_VERIFY=1
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

export DOCKER_HOST=tcp://127.0.0.1:32768 DOCKER_TLS_VERIFY=
docker stack deploy -c docker-swarm.yml edoctor --with-registry-auth --prune
