function cmcd-up() {
  docker-compose -f ./.docker/docker-compose.yaml --project-name=cmcd up -d
}

function cmcd-down() {
  docker-compose -f ./.docker/docker-compose.yaml --project-name=cmcd down --volumes
}

function cmcd-pull-media() {
  # Download and unzip
  MEDIA_ZIP_URL='https://gitlab.com/stepski011/streaming-analytics-cmcd-cmsd/-/archive/master/streaming-analytics-cmcd-cmsd-master.zip?path=cmcd-server/nginx/media'
  cd ./cmcd-server/nginx
  wget -O file.zip "$MEDIA_ZIP_URL" && unzip file.zip

  # Fish out media files (GitLab returns zip with whole repo structure, not just media url)
  mv ./streaming-analytics-cmcd-cmsd-master-cmcd-server-nginx-media/cmcd-server/nginx/media ./media

  # Clean up
  rm -rf ./file.zip ./streaming-analytics-cmcd-cmsd-master-cmcd-server-nginx-media
  cd ../../
}
