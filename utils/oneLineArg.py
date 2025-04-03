import argparse

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description= "Fetch Github Activity")

    parser.add_argument('--user', '-u', help = "Github username to fetch activity for", type = str, required = True)
    parser.add_argument('--repo', '-r', help = "Github repository in format owner/repo", type = str, required = False)
    parser.add_argument('--token', '-t', help = "Github personal access token", type = str, required = False)

    return parser.parse_args()
