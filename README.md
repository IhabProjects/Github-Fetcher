# GitHub Activity Fetcher

A simple command-line tool to fetch and display GitHub activity from the command line.

## Installation

Clone the repository:

```bash
git clone https://github.com/IhabProjects/Github-Fetcher.git

cd Github-Fetcher
```

### Install dependencies:

pip install -r requirements.txt

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

### Pagination

```bash
python github_fetcher.py --user turing --page 2 --count 50
```

### JSON output

```bash
python github_fetcher.py --user turing --json > activity.json
```

### Detailed event information

```bash
python github_fetcher.py --user turing --detailed
```

## Requirements

- Python 3.6+
- requests
