function cmcd-up() {
  docker-compose -f ./.docker/docker-compose.yaml --project-name=cmcd up -d
}

function cmcd-down() {
  docker-compose -f ./.docker/docker-compose.yaml --project-name=cmcd down --volumes
}
