# GitHub Activity Fetcher

A simple command-line tool to fetch and display GitHub activity from the command line.

## Usage

### Fetch user activity

```bash
python github_fetcher.py --user turing
```

### Fetch repository activity

```bash
python github_fetcher.py --repo turing/hello-world
```

### Use authentication token

```bash
python github_fetcher.py --user turing --token YOUR_TOKEN
```

## Requirements

- Python 3.6+
- requests
