#!/usr/bin/env bash
# Prints the id of the newest artifact NAME from a trusted run of WORKFLOW, or
# nothing when no run qualifies. Used by pages.yml for every artifact it
# publishes.
#
#   bash scripts/pick_artifact.sh <name> <workflow file>   # network refresh.yml
#
# A trusted run is one of .github/workflows/<workflow file>, on main of this
# repo, triggered by schedule or workflow_dispatch, and not already failed. The
# artifact search is repo-wide, and a pull_request from a fork can upload an
# artifact with the same name: hence the filter. conclusion == success is not
# required, because the run that uploads the artifact is still running when it
# triggers the deploy; a run that has already failed is refused.
#
# Needs GH_TOKEN (actions: read), GITHUB_REPOSITORY and REPO_ID
# (github.repository_id) in the environment. NAME and WORKFLOW come from the
# workflow file, never from data.
set -euo pipefail

name="$1"
wf=".github/workflows/$2"
[[ "$name" =~ ^[a-z0-9-]+$ && "$2" =~ ^[a-z0-9-]+\.yml$ ]] || { echo "pick_artifact: bad arguments" >&2; exit 2; }

cands=$(gh api "repos/$GITHUB_REPOSITORY/actions/artifacts?name=$name&per_page=50" \
  --jq "[.artifacts[] | select((.expired | not)
          and .workflow_run.head_branch == \"main\"
          and (.workflow_run.head_repository_id | tostring) == \"$REPO_ID\")]
        | sort_by(.created_at) | reverse | .[] | \"\(.id) \(.workflow_run.id)\"")
while read -r aid rid; do
  [ -n "$aid" ] || continue
  ok=$(gh api "repos/$GITHUB_REPOSITORY/actions/runs/$rid" --jq \
    "(.path == \"$wf\")
     and (.event == \"schedule\" or .event == \"workflow_dispatch\")
     and .head_branch == \"main\"
     and (.head_repository.id | tostring) == \"$REPO_ID\"
     and (.conclusion == null or .conclusion == \"success\")")
  if [ "$ok" = "true" ]; then
    echo "$name: artifact $aid of run $rid" >&2
    echo "$aid"
    exit 0
  fi
done <<< "$cands"
echo "$name: no artifact from a trusted $wf run" >&2
