import os

word = "Terminator"
output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(word)
