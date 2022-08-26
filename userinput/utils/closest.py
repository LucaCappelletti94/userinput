"""Utilities to determine which terms are the closer to a given one."""
from typing import List
import numpy as np
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
    split_word = word.replace("-", " ").replace("_", " ").split(" ")
    return [
        word
        for word, _ in sorted(
            [
                (
                    candidate,
                    np.mean([
                        jaro_winkler_metric(normalize(w), normalize(c))
                        for c in candidate.replace("-", " ").replace("_", " ").split(" ")
                        for w in split_word
                    ])
                )
                for candidate in words
            ],
            key=lambda x: x[1],
            reverse=True
        )[:k]
    ]


def closest(word: str, words: List[str]) -> str:
    """Return word amongst provided words which is closest.

    Parameters
    -----------------------
    word: str
        The needle tpo search for.
    words: List[str]
        The haystack to search the needle in.
    """
    best_score, best_candidate = 0, None
    split_word = word.replace("-", " ").replace("_", " ").split(" ")
    for candidate in words:
        score = np.mean([
            jaro_winkler_metric(normalize(w), normalize(c))
            for c in candidate.replace("-", " ").replace("_", " ").split(" ")
            for w in split_word
        ])
        if score > best_score:
            best_score = score
            best_candidate = candidate
    return best_candidate


def must_be_in_set(
    word: str,
    words: List[str],
    element_name: str,
    allow_lowercase: bool = True
):
    """Must be in a set.
    
    Parameters
    ------------------------
    word: str
        The word to find.
    words: List[str]
        The valid elements in the set.
    element_name: str
        The name of the elements in the set.
    allow_lowercase: bool = True
        Whether to allow for lowercase
    """
    if allow_lowercase:
        lower_word = word.lower()
        for candidate in words:
            if candidate.lower() == lower_word:
                return candidate
        
    if word not in words:
        set_size = min(5, len(words))
        closests = get_k_closest(word, words, k=5)
        raise ValueError(
            (
                "The provided {element_name} `{word}` is not available, "
                "did you mean `{best_match}`? Other similar valid values "
                "are {closests}."
            ).format(
                word=word,
                element_name=element_name,
                best_match=closests[0],
                closests=", ".join([
                    "{}`{}`".format(
                        "and " if i == set_size - 2 else "",
                        c
                    )
                    for i, c in enumerate(closests[1:])
                ])
            )
        )
    
    return word