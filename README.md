# Weather CLI
A simple CLI tool to check the current day's rain forecast and UV index.

## Requirements
You will need to have the following requirements in place:
* Docker daemon
* Access to https://api.ipify.org
* Access to https://api.weatherapi.com
* API_KEY previously created at https://www.weatherapi.com/signup.aspx

## Build
To run the tool using a docker container, build the container using the Makefile:

```
$ make build
docker build --tag weather-cli .
[+] Building 2.2s (10/10) FINISHED                                                                                                                                                                                                                                                                                                                                docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                                                                                                                                                                                                                                                                              0.0s
 => => transferring dockerfile: 212B                                                                                                                                                                                                                                                                                                                                              0.0s
 => [internal] load metadata for docker.io/library/python:3.12.4-alpine3.20                                                                                                                                                                                                                                                                                                       1.0s
 => [internal] load .dockerignore                                                                                                                                                                                                                                                                                                                                                 0.0s
 => => transferring context: 2B                                                                                                                                                                                                                                                                                                                                                   0.0s
 => [1/5] FROM docker.io/library/python:3.12.4-alpine3.20@sha256:7f15e22f496c65cffbbac5e30e7e98d60f3e3b9cc5ee5d51cf3c55ed604787c8                                                                                                                                                                                                                                                 0.0s
 => => resolve docker.io/library/python:3.12.4-alpine3.20@sha256:7f15e22f496c65cffbbac5e30e7e98d60f3e3b9cc5ee5d51cf3c55ed604787c8                                                                                                                                                                                                                                                 0.0s
 => [internal] load build context                                                                                                                                                                                                                                                                                                                                                 0.1s
 => => transferring context: 310.45kB                                                                                                                                                                                                                                                                                                                                             0.1s
 => CACHED [2/5] WORKDIR /app                                                                                                                                                                                                                                                                                                                                                     0.0s
 => CACHED [3/5] COPY requirements.txt ./                                                                                                                                                                                                                                                                                                                                         0.0s
 => CACHED [4/5] RUN pip install --no-cache-dir -r requirements.txt                                                                                                                                                                                                                                                                                                               0.0s
 => [5/5] COPY . .                                                                                                                                                                                                                                                                                                                                                                0.1s
 => exporting to image                                                                                                                                                                                                                                                                                                                                                            1.0s
 => => exporting layers                                                                                                                                                                                                                                                                                                                                                           0.8s
 => => exporting manifest sha256:83d61a06bda7c4bcfcd7f88fb9841246370956434748048729a0c4b274f8a48e                                                                                                                                                                                                                                                                                 0.0s
 => => exporting config sha256:3baa1563bbc85014853d003095baf8290c1b859064462198aa98b4072bfbe218                                                                                                                                                                                                                                                                                   0.0s
 => => exporting attestation manifest sha256:7eae7a50cb304c7839bb32c533c46f7b6893c4bcfb5024e5438be5e962c8c33b                                                                                                                                                                                                                                                                     0.0s
 => => exporting manifest list sha256:ca3a4b6bd98bbf9b68011a3948aa4c4cdd57feda7fd0354192c48b21f952cd4c                                                                                                                                                                                                                                                                            0.0s
 => => naming to docker.io/library/weather-cli:latest                                                                                                                                                                                                                                                                                                                             0.0s
 => => unpacking to docker.io/library/weather-cli:latest                                                                                                                                                                                                                                                                                                                          0.2s

View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/20qpppvm4wj5gvkhw4xkudq7g

What's next:
    View a summary of image vulnerabilities and recommendations → docker scout quickview
```

## Tips

Running help:
```
$ docker run -e API_KEY="YOUR-KEY" weather-cli weather.py --help
Usage: weather.py command [args...]

A simple weather command line to check rain and shine conditions

Required |- set API_KEY environment variable before use it

Optional |- set DEBUG_WEATHER environment variable as True to enable debug
mode

Commands:
  rain    Discovery if today the chance of rain is greater than 5%
  shine   Discovery if today the chance of UV is greater than 3
```

Running a rain argument:
```
$ docker run -e API_KEY="YOUR-KEY" weather-cli weather.py rain
True
```

Running a shine argument:
```
$ docker run -e API_KEY="YOUR-KEY" weather-cli weather.py shine
True
```

Running rain argument using debug mode enabled:
```
docker run -e API_KEY="YOUR-KEY" -e DEBUG_WEATHER=True weather-cli weather.py rain

        ====== DEBUG MODE ENABLED ======
        Your Public IP is x.x.x.x
        The chance of rain is 94%
        Is today will rain? True
```

Running shine argument using debug mode enabled:
```
docker run -e API_KEY="YOUR-KEY" -e DEBUG_WEATHER=True weather-cli weather.py shine

        ====== DEBUG MODE ENABLED ======
        Your Public IP is x.x.x.x
        The uv is 4.0
        Is today will be a shiny day? True
```
