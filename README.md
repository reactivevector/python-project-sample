# Python Project Sample

## Overview
This is a sample Python project structure which using latest technologies for CICD

## Installation

### Prerequisites
- Docker
- Docker Compose

### Docker Setup
Please follow the official Docker installation guide for your operating system:
[Docker Installation Guide](https://docs.docker.com/get-docker/)

### Running with different Profiles

#### Development profile
```bash
docker-compose --profile dev up -d
```

#### Production profile
```bash
docker-compose --profile prod up -d
```

### Stopping the Services
```bash
docker-compose down
```

### Project Structure
```
.
├── bin/                    # Scripts for starting the application
├── docs/                   # Project documentation
│   ├── ba/                # Business analysis docs
│   └── sa/                # System architecture docs
├── pps/                   # Main application code
│   ├── endpoints/         # API endpoints
│   ├── app.py            # Application entry point
│   └── app_factory.py    # Application factory pattern
├── tasks/                 # Project tasks and TODOs
├── Dockerfile            # Docker image definition
├── docker-compose.yaml   # Docker compose services
├── pyproject.toml        # Python project configuration
└── README.md            # Project documentation
```

