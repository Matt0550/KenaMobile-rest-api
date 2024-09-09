[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![Discord][discord-shield]][discord-url]
[![Docker Pulls][docker-shield]][docker-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Matt0550/KenaMobile-rest-api">
    <img src="https://raw.githubusercontent.com/Matt0550/public-gaac/main/uploads/kena_mobile_unofficial_rest_api.png" alt="Logo" height="120" style="border-radius: 10px">
  </a>

  <h3 align="center">Kena Mobile Unofficial REST API</h3>

  <p align="center">
    An unofficial REST API for Kena Mobile website.
    <br />
    <br />
    <a href="https://github.com/Matt0550/KenaMobile-rest-api/issues">Report Bug</a>
    ·
    <a href="https://github.com/Matt0550/KenaMobile-rest-api/issues">Request Feature</a>
  </p>
</div>

This project is for educational purposes only. Please use this project responsibly. 

Copyright and all rights belong to the respective owners.

## Features

- Get customer information
- Get user offers information
- Get user credit information
 
## API Endpoints
> [!TIP]
> The API is self-documented. You can access the Swagger UI at `/docs` and the ReDoc UI at `/redoc`.

- `/getCreditInfo?phoneNumber={phone}`: Get the credit information of a user. Phone is a string and is required.
- `/getCustomerDTO?phoneNumber={phone}`: Get the customer information of a user. Phone is a string and is required.
- `/getPromo?phoneNumber={phone}`: Get the offers information of a user. Phone is a string and is required.
  
> [!WARNING]
> For all the endpoints you need to pass the `PHPSESSID` in the body of the request. You can get it by logging in to the Kena Mobile website and copying the `PHPSESSID` cookie. 


## TO-DO
- [X] Add Dockerfile
- [X] Add Docker Compose
- [ ] Add more endpoints


## Public instance of the API
You can use the public instance of the API at `https://kena-api.cloud.matteosillitti.it/` (click [here](https://kena-api.cloud.matteosillitti.it/)).
Limitations: 2 requests per minute, 20 requests per day. If you need more requests, [contact me](#help---feedback).

## Environment Variables (docker)
| Variable | Description | Default |
| :--- | :--- | :--- |
| `PUID` | User ID | `1000` |
| `PGID` | Group ID | `1000` |

## Installation - Using Docker Compose (recommended)
Clone the project

```yml
version: '3'

services:
  kenamobile_restapi:
    image: matt0550/kenamobile_restapi
    environment:
      - PUID=1000     # UID of the user inside the container
      - PGID=1000     # GID of the user inside the container
    ports:
      - 5000:5000
    restart: unless-stopped
```

Run the container with `docker-compose up -d`

## Installation - Using Docker Run
Pull the image

```bash
  docker run -d -p 5000:5000 -e PUID=1000 -e PGID=1000 matt0550/kenamobile_restapi
```

## Installation - Self-Host or docker build

Clone the project

```bash
  git clone https://github.com/Matt0550/KenaMobile-rest-api
```

Go to the project directory

```bash
  cd KenaMobile-rest-api-master
```

OPTIONAL: use docker to build the image

```bash
  docker build -t KenaMobile-rest-api .
```

If you don't want to use docker, skip this step.
Else, change the `image` in `docker-compose.yml` with the image name you used.
Run the container with `docker-compose up -d`

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the REST API (after setting the environment variables)

```bash
  cd api
  uvicorn api:app
```

## Help - feedback
You can contact me on:

Discord: https://go.matteosillitti.it/discord

Telegram: https://go.matteosillitti.it/telegram

Mail: <a href="mailto:mail@matteosillitti.it">me@matteosillitti.it</a>

## License

[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)

## Support me

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/matt05)

[![buy-me-a-coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/Matt0550)

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://paypal.me/sillittimatteo)

[contributors-shield]: https://img.shields.io/github/contributors/Matt0550/KenaMobile-rest-api.svg?style=for-the-badge
[contributors-url]: https://github.com/Matt0550/KenaMobile-rest-api/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Matt0550/KenaMobile-rest-api.svg?style=for-the-badge
[forks-url]: https://github.com/Matt0550/KenaMobile-rest-api/network/members
[stars-shield]: https://img.shields.io/github/stars/Matt0550/KenaMobile-rest-api.svg?style=for-the-badge
[stars-url]: https://github.com/Matt0550/KenaMobile-rest-api/stargazers
[issues-shield]: https://img.shields.io/github/issues/Matt0550/KenaMobile-rest-api.svg?style=for-the-badge
[issues-url]: https://github.com/Matt0550/KenaMobile-rest-api/issues
[license-shield]: https://img.shields.io/github/license/Matt0550/KenaMobile-rest-api.svg?style=for-the-badge
[license-url]: https://github.com/Matt0550/KenaMobile-rest-api/blob/master/LICENSE
[discord-shield]: https://img.shields.io/discord/828990499507404820?style=for-the-badge
[discord-url]: https://go.matteosillitti.it/discord
[docker-shield]: https://img.shields.io/docker/pulls/matt0550/kenamobile_restapi?style=for-the-badge
[docker-url]: https://hub.docker.com/r/matt0550/kenamobile_restapi
