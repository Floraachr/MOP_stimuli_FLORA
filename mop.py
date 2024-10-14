import numpy as np
import pandas as pd


def get_sonority_dict():
    return {
        "low vowels": 17,
        "mid peripheral vowels": 16,
        "high peripheral vowels": 15,
        "mid interior vowels": 14,
        "high interior vowels": 13,
        "glides": 12,
        "rhotic approximants": 11,
        "flaps": 10,
        "laterals": 9,
        "trills": 8,
        "nasals": 7,
        "voiced fricatives": 6,
        "voiced affricates": 5,
        "voiced stops": 4,
        "voiceless fricatives": 3,
        "voiceless affricates": 2,
        "voiceless stops": 1,
    }


def get_ipa_dict():
    return {
        "low vowels": ["a", "ɑ", "æ"],
        "mid peripheral vowels": ["e", "o", "ɛ", "ɔ"],
        "high peripheral vowels": ["i", "u", "ɪ", "ʊ"],
        "mid interior vowels": ["ə", "ɘ"],
        "high interior vowels": ["ɨ", "ʉ"],
        "glides": ["j", "w"],
        "rhotic approximants": ["ɹ"],
        "flaps": ["ɾ", "ɽ"],
        "laterals": ["l", "ɭ", "ʎ"],
        "trills": ["r", "ʀ"],
        "nasals": ["m", "n", "ɳ", "ŋ", "ɲ", "ɴ"],
        "voiced fricatives": ["v", "ð", "z", "ʒ", "ʐ", "ʝ", "ɣ", "ʁ", "ʕ", "ɦ"],
        "voiced affricates": ["dʒ", "ɖʐ", "ɟʝ"],
        "voiced stops": ["b", "d", "g", "ɖ", "ɢ"],
        "voiceless fricatives": ["f", "θ", "s", "ʃ", "ʂ", "ç", "x", "χ", "ħ", "h"],
        "voiceless affricates": ["tʃ", "ts", "tɕ", "ʈʂ"],
        "voiceless stops": ["p", "t", "k", "ʈ", "q", "ʡ", "ʔ"],
    }


def get_phonotacticon(
    lect: str = None,
    position: str = "Onset",
    path: str = r"C:\Users\flora\OneDrive\Documents\stimuli_MOP\Syllable-Generator-main\Syllable-Generator-main",

):
    if not np.isin(position, ["Onset", "Nucleus", "Coda"]):
        raise TypeError("position must be one of 'Onset', 'Nucleus', 'Coda'")
    ph = pd.read_csv(path)[["Lect", position]]
    ph_dict = dict(zip(ph["Lect"], ph[position]))
    if lect is None:
        return ph_dict
    return ph_dict[lect].split()


def get_ipa_class(phoneme: str, ipa_dict=get_ipa_dict()):
    for cat, pho in ipa_dict.items():
        if np.isin(phoneme, pho):
            return cat


def get_sonority(phoneme: str, sonority_dict=get_sonority_dict()):
    ipa_class = get_ipa_class(phoneme)
    return sonority_dict[ipa_class]


def get_ssp_clusters(consonants: list[str], ssp_diff: int = 5):
    clusters = []
    for a in consonants:
        for b in consonants:
            if (get_sonority(a) - get_sonority(b)) > ssp_diff:
                clusters.append(a + b)
    return clusters


def make_words(consonants: list[str], vowels: list[str], **kwargs):
    clusters = get_ssp_clusters(consonants, **kwargs)
    words = [
        c + v1 + cl + v2
        for c in consonants
        for v1 in vowels
        for cl in clusters
        for v2 in vowels
    ]
    return words