import argparse

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help='the path to the export file')
    parser.add_argument('--format', default='json', choices=['json', 'csv'], type=str.lower)
    return parser


def main():
    import sys
    from hr import export, users
    from hr import users as u

    # Creationg the parser and immediately have it start parsing the args
    args = create_parser().parse_args()

    users = u.fetch_users()

    # If the path is passed, we are going to determine the file we are using and the passed format
    if args.path:
        file = open(args.path, 'w', newline='')
    else:
        file = sys.stdout

    if args.format == 'json':
        export.to_json_file(file, users)
    else:
        export.to_csv_file(file, users)
