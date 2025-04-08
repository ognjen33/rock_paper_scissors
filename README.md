# rock_paper_scissors
RockPaperScissorsLizardSpock game
# Rock Paper Scissors Game

A simple Rock Paper Scissors game API built with FastAPI.

## Quick Start

### Run with Docker

```bash
# Build and start container from the root directory containing DockerFile
docker build -t <container-name> .
docker run -p 8000:8000 <container-name>

# Access the API at http://localhost:8000
```

### API Endpoints

- `POST /play` - Play a game versus a computer
- `GET /games` - View game last 10 games and results
- `GET /games/stats` - View games statistics such as win count, win rate
- `GET /choices` - View all choices
- `GET /choice` - View random choice


## Testing

```bash
# Run tests
docker exec <container_id> pytest app/tests
```

## Technologies

- FastAPI
- SQLAlchemy
- Docker


## Note
1. Test coverage is not 100%, most interesting parts are covered
2. Database url is left hardcoded and left to its name test.db due to simplicity
3. Dependencies are left non-locked due to simplicity, although best practice is to lock them to a specific version or subversion(i.e fastapi==0.95.1)
