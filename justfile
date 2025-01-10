run-dis *args="":
  uv run disearch {{args}}

run-repl level="10":
  uv run repl --log-level={{level}} 

run-execute level="10":
  uv run execute --log-level={{level}} tests/test_file.py

build:
  uv build

build-docker: build
  docker build -t takimoysha:python .
