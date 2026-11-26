#!/usr/bin/env python3
"""Sum 25 Round 7 entrypoint (news-image-20261125).

Copies the pre-rendered entry.png next to this file into the output
directory. Standard library only: the make.fun server sandbox has no
PIL, so this entrypoint must never import anything beyond the stdlib.
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        print("entry.png not found next to main.py", file=sys.stderr)
        return 1
    # The PNG is rendered ahead of time by render.py (PIL, local only);
    # this file only moves bytes, so it runs identically in the sandbox.
    if len(sys.argv) > 1:
        outdir = sys.argv[1]
    else:
        outdir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(outdir, exist_ok=True)
    dst = os.path.join(outdir, "entry.png")
    shutil.copyfile(src, dst)
    print("wrote", dst, os.path.getsize(dst), "bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
