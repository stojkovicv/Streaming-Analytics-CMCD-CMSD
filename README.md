# Streaming Analytics for CMCD

Inspired by [NUStreaming/CMCD-DASH](https://github.com/NUStreaming/CMCD-DASH).

## Quick start

You will need zsh, [docker](https://docs.docker.com/get-docker/), and [docker-compose](https://docs.docker.com/compose/install/) for this to work.

### 1️⃣ Clone this repo
```
git clone git@github.com:stepski011/Streaming-Analytics-CMCD-CMSD.git
```

### 2️⃣ Source toolbox
In the project root folder run `source ./toolbox.zsh`.

Alternatively, you can add toolbox.zsh into your PATH so that you can call the scripts to anywhere and don't have to source toolbox in every new terminal session.

This file contains helpful scripts to start/stop the containers and other control tasks.

### 🚀 Launch containers
In the root of the project run
```
cmcd-up
```

This will spin up the docker-compose configuration in a project called `cmcd`. You can test by running `docker ps`.

You can send GET request `http://localhost:8080/cmcd-njs/testProcessQuery?CMCD=bl%3D21300` to check that the cmcd server is up and running. See `cmcd-server/tests.http` for more examples.

### 🎉 Stream
Open the `stream-client/index.html` file in you browser, the streaming should start automatically.

Even though you are streaming the file from your localhost, you will need internet, so that the [dash.js](https://github.com/Dash-Industry-Forum/dash.js) source code can be downloaded.

## Components

---
TBD

---

- CMCD Server
- Stream Client
- Database
- Grafana


### CMCD Server Setup and Testing

Run the NGINX server:
- Navigate to the `cmcd-server/` folder
- Install the NJS module in NGINX using `sudo apt install nginx-module-njs`
- Open `nginx/config/nginx.conf` and edit `<PATH_TO_CMCD-DASH>` (under "`location /media/vod`") to indicate the absolute path to this repository
- Launch NGINX using `sudo nginx -c <PATH_TO_CMCD-DASH>/cmcd-server/nginx/config/nginx.conf` (note that the absolute path must be used)
- Reload NGINX using `sudo nginx -c <PATH_TO_CMCD-DASH>/cmcd-server/nginx/config/nginx.conf -s reload`, if the configuration has changed
- Test the NJS application `cmcd_njs.js` with CMCD using `http://⟨MachineIP_ADDRESS⟩:8080/cmcd-njs/testProcessQuery?CMCD=bl%3D21300` and verify that it returns a value of 21300 for buffer length (bl)

Run the dash.js client:
- Navigate to the `dash.js/` folder
- Install the dependencies using `npm install`
- Build, watch file changes and launch samples page using `grunt dev`
- Test the dash.js application by navigating to `http://⟨MachineIP_ADDRESS⟩:3000/samples/cmcd-dash/index.html` to view the CMCD-enabled player

### NGINX Server

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
