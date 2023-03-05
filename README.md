# Streaming Analytics for CMCD

This work is inspired by [NUStreaming/CMCD-DASH](https://github.com/NUStreaming/CMCD-DASH).

In the repository we provide an end-to-end proof of concept of a video streaming infrastructure which monitors the Quality of Experience (QoE) of the clients watching the stream. The QoE is presented in Grafana dashboard.


## Quick start

You will need zsh, [docker](https://docs.docker.com/get-docker/), and [docker-compose](https://docs.docker.com/compose/install/) for this to work.

### 1️⃣ Clone this repo
```
git clone git@github.com:stepski011/Streaming-Analytics-CMCD-CMSD.git
```

### 2️⃣ Source toolbox
In the project root folder run
```bash
source ./toolbox.zsh
```

Alternatively, you can add toolbox.zsh into your PATH so that you can call the scripts to anywhere and don't have to source toolbox in every new terminal session.

This file contains helpful scripts to start/stop the containers and other control tasks.

### 🐇 Download media files (Big Buck Bunny)
In the root of the project run
```bash
cmcd-pull-media
```

### 🚀 Launch containers
In the root of the project run
```bash
cmcd-up
```

This will spin up the docker-compose configuration in a project called `cmcd`. You can test by running `docker ps`.

You can send GET request `http://localhost:8080/cmcd-njs/testProcessQuery?CMCD=bl%3D21300` to check that the cmcd server is up and running. See `cmcd-server/tests.http` for more examples.

### 🎉 Stream
Open the `stream-client/index.html` file in you browser, the streaming should start automatically.

Even though you are streaming the file from your localhost, you will need to be connected to the internet, so that the [dash.js](https://github.com/Dash-Industry-Forum/dash.js) source code can be downloaded.

### 📊 View dashboard
To open the [CMCD Grafana Dashboard](http://0.0.0.0:3000/d/rivvtDJVz/cmcd). Grafana runs on port 3000, you can access it on http://0.0.0.0:3000.

## Components
![Architecture Diagram](./docs/assets/architecture.png)

### CMCD-server

- NGINX JS (NJS) webserver and middleware (NGINX v1.18)
- See `nginx/cmcd_njs.js` for more details on the NJS application logic and implementation
    - Note that request URLs that are prefixed with `/cmcd-njs/bufferBasedRateControl` refer to CMCD requests and will trigger the NJS rate control mechanism
    - Example request with CMCD: `http://localhost:8080/cmcd-njs/bufferBasedRateControl/media/vod/bbb_30fps_akamai/bbb_30fps.mpd` 
    - Example request with NO CMCD: `http://localhost:8080/media/vod/bbb_30fps_akamai/bbb_30fps.mpd`

Other useful commands:
- Check if NGINX is running:
  - `curl http://127.0.0.1:8080`
  - Or `ps -ef | grep nginx`
  - Or `systemctl status nginx` for webserver status
- Log files location: `/var/log/nginx/`
  - To inspect logs: `tail -f error.log` and `tail -f access.log`
  - To capture the custom logs in `cmcd_njs.js`:
    - Create the log file: `sudo touch /var/log/nginx/cmcd.log`
    - Update write permission for the log file: `sudo chmod 666 /var/log/nginx/cmcd.log`
    - To inspect logs: `tail -f cmcd.log`

### CMCD-bridge
TODO

### Database
TODO

### Grafana Dashboard
![CMCD Dashboard in Grafana](./docs/assets/grafana-dashboard.png)

TODO:
- More details on grafana setup
- link to AWS project
- explanation of panels (copy from Grafana setup)


## More on CMCD
TODO: Link to our report

## Contributing
TODO

### Contributors
- **Antonín Vlček** [🐦 @TonyVlcek](https://twitter.com/TonyVlcek), [🐙 TonyVlcek](https://github.com/TonyVlcek)
- **Alicx Kamoun**
- **Vuk Stojkovic** [🐙 stepski011](https://github.com/stepski011)
