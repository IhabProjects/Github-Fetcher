
<div align="center">

  <img src="public/logo.png" alt="GitHub Activity Fetcher Logo" width="200"/>

  # GitHub Activity Fetcher

  🚀 A powerful CLI tool for fetching and displaying GitHub activity with style!

  [Features](#features) • [Installation](#installation) • [Usage](#usage) • [Examples](#examples) • [Contributing](#contributing)

</div>

## 🌟 Features

- 📊 **Beautiful Profile Statistics** - View comprehensive user statistics
- 🎨 **Colorful Interface** - Easy-to-read, color-coded activity feed
- 📈 **Language Analytics** - Visual representation of language usage
- 🔍 **Detailed Events** - In-depth information about each activity
- 🔑 **API Token Support** - Higher rate limits with authentication
- 📝 **JSON Export** - Export data in JSON format

## 🖼️ Screenshots

### Default View
![Default View](/public/default.png)

### Detailed Information
![Detailed Information](/public/detailed_info.png)

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/IhabProjects/Github-Fetcher.git
   cd Github-Fetcher
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 📖 Usage

### Basic Commands

Fetch user activity:
```bash
python github_fetcher.py --user <username>
```

Fetch repository activity:
```bash
python github_fetcher.py --repo <owner/repo>
```

Use with GitHub token:
```bash
python github_fetcher.py --user <username> --token YOUR_TOKEN
```

Get detailed information:
```bash
python github_fetcher.py --user <username> --detailed
```

Export as JSON:
```bash
python github_fetcher.py --user <username> --json > output.json
```

### Command Options

| Option       | Short | Description                                  |
|--------------|-------|----------------------------------------------|
| `--user`     | `-u`  | Fetch Github User Activity                   |
| `--repo`     | `-r`  | Repository in owner/repo format              |
| `--token`    | `-t`  | GitHub API token for authentication          |
| `--page`     | `-p`  | Page number (default: 1)                     |
| `--count`    | `-c`  | Number of events per page (default: 30)      |
| `--json`     | `-j`  | Output in JSON format                        |
| `--detailed` | `-d`  | Show detailed event information              |

## 💡 Examples

### View User Profile and Activity
```bash
python github_fetcher.py --user turing
```

### Get Detailed Repository Activity
```bash
python github_fetcher.py --repo turing/Hello-World --detailed
```

### Export User Activity to JSON
```bash
python github_fetcher.py --user turing --json > activity.json
```

## ⚙️ Configuration

### GitHub Token

To avoid rate limits, you can use a GitHub token:

1. Generate a token at: [https://github.com/settings/tokens](https://github.com/settings/tokens)

2. Use the token with the `--token` option:
   ```bash
   python github_fetcher.py --user turing --token YOUR_TOKEN
   ```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch:
   ```bash
   git checkout -b feature/noice-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add noice lil feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/noice-feature
   ```
5. Open a Pull Request

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

## 🙏 Acknowledgments

- GitHub API
- Colorama
- roadmap.sh for idea (Had it before but they made me do it: https://roadmap.sh/projects/github-user-activity)
- All our contributors (None For now)

## 📬 Contact

**Ihab:Eurekios** - [@linkedin](https://twitter.com/yourtwitter)
**Project Link**: [https://github.com/IhabProjects/Github-Fetcher](https://github.com/IhabProjects/Github-Fetcher)

---

Made with ❤️ by Ihab Elbani
