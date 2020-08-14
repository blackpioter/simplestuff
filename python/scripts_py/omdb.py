import json
import re

def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    movies = []
    for file in files:
        with open(file, 'r') as f:
            movies.append(json.loads(f.read()))
    return movies


def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    for movie in movies:
        if "Comedy" in movie['Genre']:
            return movie['Title']


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    key = lambda x: int(re.sub(r'.*\s(\d+)\snominat.*.',r'\1',x['Awards']))
    return max(movies, key=key)['Title']


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    return max(movies, key=lambda x:int(x['Runtime'].split()[0]))['Title']
