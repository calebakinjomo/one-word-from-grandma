"""One Word From Grandma — entry word "Terminator".

Grandma's word for the moment something unstoppable walks in: she doesn't
run, she just names it — "Terminator" — and keeps stirring the pot.
"""

import os

word = "Terminator"
output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(word)
