"""Compatibility shims for the Gate-3 frozen stack.

videohash 3.0.1 calls PIL.Image.ANTIALIAS, which Pillow removed in v10
(we run Pillow 11.3.0). ANTIALIAS was always an alias of LANCZOS, so
restoring the alias is exact, not approximate. Applied by the dedupe
stage and the smoke tests before videohash is imported. Logged in
docs/INSTALL-LIST.md (Gate 3 results) — not a silent workaround.
"""
import PIL.Image

if not hasattr(PIL.Image, "ANTIALIAS"):
    PIL.Image.ANTIALIAS = PIL.Image.LANCZOS
