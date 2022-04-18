import argparse
import hashlib
import json
import os

import requests as requests


def cached_json_get(url, cache_path):
    """
    Get cached or real JSON.

    :param url: URL to get.
    :param cache_path: Path to cache JSON.
    :return:
    """

    h = hashlib.sha256(url.encode())
    file_name = f'{h.hexdigest()}.json'
    file_path = os.path.join(cache_path, file_name)
    # check if cached
    if os.path.exists(file_path):
        # get from cache
        with open(file_path, 'r') as f:
            json_data = json.load(f)
        return json_data
    # not cached
    else:
        response = requests.get(url)
        json_data = response.json()
        # put in cache
        with open(file_path, 'w') as f:
            json.dump(json_data, f, indent=2)
        return json_data


def main():
    args_parser = argparse.ArgumentParser(
        description='Download all chess.com games into one file. '
                    'File are stored in output directory in PGN format.',
        epilog='Copyright 2022 by Cezary K. Wagner is licensed under '
               'Attribution-NonCommercial-NoDerivatives 4.0 International')
    args_parser.add_argument('-u', '--user_name', required=True, type=str, help='User name who was played games.')
    args_parser.print_help()

    args = args_parser.parse_args()

    user_name = args.user_name
    url_games = f'https://api.chess.com/pub/player/{user_name}/games/archives'

    # create output
    output_path = os.path.join(os.path.dirname(__file__), 'output')
    os.makedirs(output_path, exist_ok=True)

    # create cache
    cache_path = os.path.join(output_path, 'cache')
    os.makedirs(cache_path, exist_ok=True)

    json_data = cached_json_get(url_games, cache_path)
    archives = json_data['archives']
    pgns = []
    for archive in archives:
        print(archive)
        json_data = cached_json_get(archive, cache_path)

        for game in json_data['games']:
            pgns.append(game['pgn'])

    with open('all_pgn.pgn', 'w') as f:
        for pgn in pgns:
            f.write(pgn)
            f.write('\n' * 2)




if __name__ == '__main__':
    main()
