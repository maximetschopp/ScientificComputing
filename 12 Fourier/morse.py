MORSE = {
    "label": "",
    "children": {
    ".": {
        "label": "E",
        "children": {
            "-": {
                "label": "A",
                "children": {
                    "-": {
                        "label": "W",
                        "children": {
                            "-": {
                                "label": "J",
                                "children": {"-": {"label": "1", "children": {}}},
                            },
                            ".": {"label": "P", "children": {}},
                        },
                    },
                    ".": {
                        "label": "R",
                        "children": {".": {"label": "L", "children": {}}},
                    },
                },
            },
            ".": {
                "label": "I",
                "children": {
                    "-": {
                        "label": "U",
                        "children": {
                            ".": {"label": "F", "children": {}},
                            "-": {
                                "label": "",
                                "children": {"-": {"label": "2", "children": {}}},
                            },
                        },
                    },
                    ".": {
                        "label": "S",
                        "children": {
                            ".": {
                                "label": "H",
                                "children": {
                                    "-": {"label": "4", "children": {}},
                                    ".": {"label": "5", "children": {}},
                                },
                            },
                            "-": {
                                "label": "V",
                                "children": {"-": {"label": "3", "children": {}}},
                            },
                        },
                    },
                },
            },
        },
    },
    "-": {
        "label": "T",
        "children": {
            ".": {
                "label": "N",
                "children": {
                    ".": {
                        "label": "D",
                        "children": {
                            ".": {
                                "label": "B",
                                "children": {".": {"label": "6", "children": {}}},
                            },
                            "-": {"label": "X", "children": {}},
                        },
                    },
                    "-": {
                        "label": "K",
                        "children": {
                            ".": {"label": "C", "children": {}},
                            "-": {"label": "Y", "children": {}},
                        },
                    },
                },
            },
            "-": {
                "label": "M",
                "children": {
                    ".": {
                        "label": "G",
                        "children": {
                            "-": {"label": "Q", "children": {}},
                            ".": {
                                "label": "Z",
                                "children": {".": {"label": "7", "children": {}}},
                            },
                        },
                    },
                    "-": {
                        "label": "O",
                        "children": {
                            ".": {
                                "label": "",
                                "children": {".": {"label": "8", "children": {}}},
                            },
                            "-": {
                                "label": "",
                                "children": {
                                    ".": {"label": "9", "children": {}},
                                    "-": {"label": "0", "children": {}},
                                },
                            },
                        },
                    },
                },
            },
        },
    },
    },
}

def morse_decode_recursive(code, tree):
    if not code:
        return tree.get("label", "")
    if "children" in tree and code[0] in tree["children"]:
        return morse_decode_recursive(code[1:], tree["children"][code[0]])
    return ""


def morse_decode(code):
    return ''.join(morse_decode_recursive(letter, MORSE) for letter in code.split())

code = "--.. . .-. ---"

# Split the code into Morse letters and decode each one
decoded = morse_decode(code)
print(f"Decoded Morse code '{code}' to '{decoded}'")