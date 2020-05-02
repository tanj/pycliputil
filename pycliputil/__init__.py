__version__ = "0.1.0"

import pyperclip as clipboard
import re
from swissarmy import safe_cast


class IncClip(object):
    reCounter = re.compile(r"<(?P<counter>\w+):?(?P<start>\d+)?>", re.MULTILINE)

    def __init__(self, string=None):
        self.counters = {}
        self.string = string if string is not None else clipboard.paste()
        self.find_counters()

    def find_counters(self):
        for c in self.reCounter.finditer(self.string):
            self.counters.update(
                {
                    c.group("counter"): {
                        "inc": safe_cast(int, c.group("start"), 1),
                        "match": c.string[c.start() : c.end()],
                    }
                }
            )

    def inc_clip(self):
        new = self.string
        for c in self.counters:
            new = new.replace(self.counters[c]["match"], str(self.counters[c]["inc"]))
            self.counters[c]["inc"] += 1
        clipboard.copy(new)
