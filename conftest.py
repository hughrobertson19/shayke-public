"""Make the MIT-licensed quotable_span package importable during tests.

The package lives under ``lib/quotable_span/`` (kept out of the repo root so the
one runnable library reads as a self-contained folder). Adding that directory to
``sys.path`` lets ``import quotable_span`` resolve from a plain
``pytest`` at the repo root, with no install step and no dependency.
"""

import sys
from pathlib import Path

_QS = Path(__file__).resolve().parent / "lib" / "quotable_span"
if str(_QS) not in sys.path:
    sys.path.insert(0, str(_QS))
