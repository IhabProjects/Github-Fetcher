from colorama import init, Fore, Style
init()

def print_banner():
    """Print the ASCII art banner and basic usage"""
    banner = f"""{Fore.CYAN}
    ███████╗██╗   ██╗██████╗ ███████╗██╗  ██╗██╗ ██████╗ ███████╗
    ██╔════╝██║   ██║██╔══██╗██╔════╝██║ ██╔╝██║██╔═══██╗██╔════╝
    █████╗  ██║   ██║██████╔╝█████╗  █████╔╝ ██║██║   ██║███████╗
    ██╔══╝  ██║   ██║██╔══██╗██╔══╝  ██╔═██╗ ██║██║   ██║╚════██║
    ███████╗╚██████╔╝██║  ██║███████╗██║  ██╗██║╚██████╔╝███████║
    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝ ╚══════╝

    ██████╗ ██╗████████╗    ███████╗███████╗████████╗ ██████╗██╗  ██╗███████╗██████╗
    ██╔════╝ ██║╚══██╔══╝    ██╔════╝██╔════╝╚══██╔══╝██╔════╝██║  ██║██╔════╝██╔══██╗
    ██║  ███╗██║   ██║       █████╗  █████╗     ██║   ██║     ███████║█████╗  ██████╔╝
    ██║   ██║██║   ██║       ██╔══╝  ██╔══╝     ██║   ██║     ██╔══██║██╔══╝  ██╔══██╗
    ╚██████╔╝██║   ██║       ██║     ███████╗   ██║   ╚██████╗██║  ██║███████╗██║  ██║
     ╚═════╝ ╚═╝   ╚═╝       ╚═╝     ╚══════╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝{Style.RESET_ALL}

    {Fore.GREEN}[ GitHub Activity Fetcher v1.0 ]{Style.RESET_ALL}
    {Fore.YELLOW}[ Created by Eurekios: Ihab ]{Style.RESET_ALL}
    """
    print(banner)

def print_usage():
    """Print colorful usage instructions"""
    usage = f"""
    {Fore.CYAN}USAGE:{Style.RESET_ALL}

    {Fore.GREEN}Fetch user activity:{Style.RESET_ALL}
    python github_fetcher.py --user <username>

    {Fore.GREEN}Fetch repository activity:{Style.RESET_ALL}
    python github_fetcher.py --repo <owner/repo>

    {Fore.CYAN}OPTIONS:{Style.RESET_ALL}

    {Fore.YELLOW}-u, --user{Style.RESET_ALL}     GitHub username to fetch activity for
    {Fore.YELLOW}-r, --repo{Style.RESET_ALL}     GitHub repository (format: owner/repo)
    {Fore.YELLOW}-t, --token{Style.RESET_ALL}    GitHub API token for authentication
    {Fore.YELLOW}-p, --page{Style.RESET_ALL}     Page number (default: 1)
    {Fore.YELLOW}-c, --count{Style.RESET_ALL}    Number of events per page (default: 30)
    {Fore.YELLOW}-j, --json{Style.RESET_ALL}     Output raw JSON instead of formatted text
    {Fore.YELLOW}-d, --detailed{Style.RESET_ALL} Show detailed event information

    {Fore.CYAN}EXAMPLES:{Style.RESET_ALL}

    {Fore.GREEN}# Fetch user activity with token{Style.RESET_ALL}
    python github_fetcher.py --user turing --token YOUR_TOKEN

    {Fore.GREEN}# Fetch repository activity with pagination{Style.RESET_ALL}
    python github_fetcher.py --repo turing/hello-world --page 2 --count 50

    {Fore.GREEN}# Get detailed JSON output{Style.RESET_ALL}
    python github_fetcher.py --user turing --json --detailed > activity.json
    """
    print(usage)

def print_error(message):
    """Print error message in red"""
    print(f"\n{Fore.RED}Error: {message}{Style.RESET_ALL}\n")

def print_success(message):
    """Print success message in green"""
    print(f"\n{Fore.GREEN}{message}{Style.RESET_ALL}\n")

def print_info(message):
    """Print info message in cyan"""
    print(f"{Fore.CYAN}{message}{Style.RESET_ALL}")

def print_warning(message):
    """Print warning message in yellow"""
    print(f"{Fore.YELLOW}Warning: {message}{Style.RESET_ALL}")
