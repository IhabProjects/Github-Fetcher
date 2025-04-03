import argparse

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description= "Fetch Github Activity")

    parser.add_argument('--user', '-u', help = "Github username to fetch activity for", type = str, required = False)
    parser.add_argument('--repo', '-r', help = "Github repository in format owner/repo", type = str, required = False)
    parser.add_argument('--token', '-t', help = "Github personal access token", type = str, required = False)

    parser.add_argument('--page', '-p', help = "Page number for pagination", type = int, default = 1)
    parser.add_argument('--count', '-c', help = "Number of events per page", type = int, default = 30)


    parser.add_argument('--json', '-j', action='store_true', help='Output raw JSON instead of formatted text')
    
    parser.add_argument('--detailed', '-d', action='store_true', help='Show detailed event information')

    return parser.parse_args()
