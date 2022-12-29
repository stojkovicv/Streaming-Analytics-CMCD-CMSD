function cmcd-up() {
  docker-compose -f ./.docker/docker-compose.yaml --project-name=cmcd up -d
}

function cmcd-down() {
  docker-compose -f ./.docker/docker-compose.yaml --project-name=cmcd down --volumes
}

function cmcd-get-logs() {
   docker cp cmcd-server:/var/log/nginx/access_cmcd.log ./cmcd-server/access_cmcd.log
}
