import re

with open("/Users/ziway/Downloads/CNS/inhn_exams_dump.txt", "r") as f:
    text = f.read()

keywords = {
    "CSMA/BEB": ["csma", "backoff", "beb", "hidden station", "rts", "cts"],
    "BDP/Delay": ["bandwidth", "delay product", "bdp", "propagation", "serialization"],
    "Switching": ["circuit switching", "packet switching", "message switching"],
    "Routing": ["distance vector", "link state", "dijkstra", "bellman"],
    "Token Passing": ["token", "ring"],
    "Framing/4B5B": ["4b5b", "stuffing", "manchester", "code rule violation", "preamble"]
}

for category, words in keywords.items():
    print(f"\n======== {category} ========")
    for word in words:
        matches = re.finditer(r".{0,100}" + word + r".{0,100}", text, re.IGNORECASE | re.DOTALL)
        count = 0
        for m in matches:
            count += 1
            if count <= 3: # print first 3 matches for context
                print(f"[{word}] {m.group(0).replace(chr(10), ' ')}")
        print(f"Total '{word}': {count}")
