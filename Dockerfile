FROM --platform=linux/amd64 ghcr.io/owl-corp/python-poetry-base:3.12-slim

# Install project dependencies
WORKDIR /bot
COPY pyproject.toml poetry.lock ./
RUN poetry install --without dev

# Copy the source code in last to optimize rebuilding the image
COPY . .

ENTRYPOINT ["poetry"]
CMD ["run", "python", "-m", "bot"]
