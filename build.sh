#!/bin/bash

declare -r -x SWD="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
declare -r -x SOURCES="${SWD##*/}"

if [[ -z "${GIT_BRANCH}" ]]; then
  if [[ -d "${SWD}/.git" ]]; then
    GIT_BRANCH=$(cd "${SWD}"; git rev-parse --abbrev-ref HEAD)
  else
    GIT_BRANCH="unknown"
  fi
fi

if [[ -z "${GIT_REVNUM}" ]]; then
  if [[ -d "${SWD}/.git" ]]; then
    GIT_REVNUM=$(cd "${SWD}"; git rev-list HEAD|wc -l)
  else
    GIT_REVNUM=0
  fi
fi

tar -cvzf /tmp/aic94xx-3.10.0.tar.gz aic94xx/ && rpmbuild -tb /tmp/aic94xx-3.10.0.tar.gz  --define 'version 3.10.0' --define "release ${GIT_REVNUM}"
