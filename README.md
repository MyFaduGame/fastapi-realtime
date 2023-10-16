
# FastAPI Web Socket

This repository has code of FastAPI WebSocket and it contains the connection cofigration in order to create a deployment on EC2 or any other type of it..




## API Reference

#### Ping API

```http
  GET /test
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `None   ` | `None  ` |                            |

| Returns     |
| :-----------|
| `Hello World` |

#### Without WebSocket

```http
  GET /test/{number}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `number`      | `Integer` | **Required**. Number |

| Returns     |
| :-----------|
| `number+1` |

```ws
  WS /websocket
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `number`      | `Integer` | **Required**. Number |

| Returns     |
| :-----------|
| `number+1` |



## Features

- Python
- FastAPI
- Docker Deployemnt
- nginx Conf
- Easy to Install
- Plug and Play



## Authors

- [@MyFaduGame](https://www.github.com/MyFaduGame)


## 🛠 Skills Used
Python, Docker, Docker-Compose, Nginx, WebSocket, GitHub, Github Actions


## Support

For support, email navinsharma9376319931@gmail.com.

