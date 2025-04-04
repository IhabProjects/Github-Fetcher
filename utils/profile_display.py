from colorama import Fore, Style
import shutil

def get_terminal_width():
    """Get the terminal width or default to 80"""
    width, _ = shutil.get_terminal_size()
    return width

def create_progress_bar(value, max_value, width=20):
    """Create a colorful progress bar"""
    percentage = (value / max_value) if max_value > 0 else 0
    filled_length = int(width * percentage)
    bar = '█' * filled_length + '░' * (width - filled_length)
    return f"{Fore.CYAN}{bar}{Style.RESET_ALL}"

def display_user_profile(user_data):
    """Display user profile in a beautiful card format"""
    if not user_data:
        return

    profile = user_data['profile']
    stats = user_data['stats']
    width = min(get_terminal_width(), 80)

    # Top border
    print(f"\n{Fore.CYAN}{'═' * width}{Style.RESET_ALL}")

    # Profile header
    print(f"{Fore.CYAN}║{Style.RESET_ALL} {Fore.WHITE}📊 GitHub Profile: {Fore.YELLOW}{profile['login']}{Style.RESET_ALL}")
    if profile['name']:
        print(f"{Fore.CYAN}║{Style.RESET_ALL} {Fore.WHITE}👤 Name: {Fore.GREEN}{profile['name']}{Style.RESET_ALL}")
    if profile['bio']:
        print(f"{Fore.CYAN}║{Style.RESET_ALL} {Fore.WHITE}📝 Bio: {profile['bio']}{Style.RESET_ALL}")

    # Location and company
    if profile['location']:
        print(f"{Fore.CYAN}║{Style.RESET_ALL} {Fore.WHITE}📍 Location: {profile['location']}{Style.RESET_ALL}")
    if profile['company']:
        print(f"{Fore.CYAN}║{Style.RESET_ALL} {Fore.WHITE}🏢 Company: {profile['company']}{Style.RESET_ALL}")

    # Separator
    print(f"{Fore.CYAN}╠{'═' * (width-2)}╣{Style.RESET_ALL}")

    # Statistics
    print(f"{Fore.CYAN}║{Style.RESET_ALL} {Fore.WHITE}📊 Statistics{Style.RESET_ALL}")
    print(f"{Fore.CYAN}║{Style.RESET_ALL}   • Repositories: {Fore.GREEN}{stats['public_repos']}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}║{Style.RESET_ALL}   • Followers: {Fore.GREEN}{stats['followers']}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}║{Style.RESET_ALL}   • Following: {Fore.GREEN}{stats['following']}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}║{Style.RESET_ALL}   • Total Stars: {Fore.YELLOW}⭐ {stats['total_stars']}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}║{Style.RESET_ALL}   • Total Forks: {Fore.MAGENTA}🍴 {stats['total_forks']}{Style.RESET_ALL}")

    # Top Languages
    if stats['top_languages']:
        print(f"{Fore.CYAN}╠{'═' * (width-2)}╣{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║{Style.RESET_ALL} {Fore.WHITE}📚 Top Languages{Style.RESET_ALL}")

        max_lang_count = max(count for _, count in stats['top_languages'])
        for lang, count in stats['top_languages']:
            bar = create_progress_bar(count, max_lang_count, width=20)
            print(f"{Fore.CYAN}║{Style.RESET_ALL}   {lang:<15} {bar} {count}")

    # Profile URLs
    print(f"{Fore.CYAN}╠{'═' * (width-2)}╣{Style.RESET_ALL}")
    print(f"{Fore.CYAN}║{Style.RESET_ALL} {Fore.WHITE}🔗 Profile: {Fore.BLUE}{profile['html_url']}{Style.RESET_ALL}")
    if profile['blog']:
        print(f"{Fore.CYAN}║{Style.RESET_ALL} {Fore.WHITE}🌐 Blog: {Fore.BLUE}{profile['blog']}{Style.RESET_ALL}")

    # Bottom border
    print(f"{Fore.CYAN}{'═' * width}{Style.RESET_ALL}\n")
