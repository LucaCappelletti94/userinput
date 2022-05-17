"""Utilities to determine which terms are the closer to a given one."""
from typing import List
from jaro import jaro_winkler_metric

def normalize(word: str) -> str:
    """Return provided string normalized to increase likelyhood of matches."""
    word = word.lower()
    return word

def get_k_closest(word: str, words: List[str], k: int) -> List[str]:
    """Return the top k words from given list that are closest to provided word.

    Parameters
    -----------------------
    word: str,
        The needle tpo search for.
    words: List[str],
        The haystack to search the needle in.
    k: int,
        The number of elements to retrieve.
    """
    top_k = []
    sorted_list = sorted(
        [
            (
                w,
                jaro_winkler_metric(normalize(w), normalize(word))
            )
            for w in words
        ],
        key=lambda x: x[1],
        reverse=True
    )

    for i, (word, _) in enumerate(sorted_list):
        if i < k:
            top_k.append(word)
        else:
            break
        
    return top_k


def closest(word: str, words: List[str]) -> str:
    """Return word amongst provided words which is closest.

    Parameters
    -----------------------
    word: str,
        The needle tpo search for.
    words: List[str],
        The haystack to search the needle in.
    """
    best_score, best_candidate = 0, None
    for candidate in words:
        score = jaro_winkler_metric(normalize(word), normalize(candidate))
        if score > best_score:
            best_score = score
            best_candidate = candidate
    return best_candidate
