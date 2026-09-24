"""
Stack-based page navigation history ("Back" button).
Owner: Member 3
"""


class Navigator:
    def __init__(self):
        self._history = []  # acts as a Stack (list used as stack: append/pop)

    def push(self, page_name):
        """Call this BEFORE navigating to a new page, to remember where we came from."""
        self._history.append(page_name)

    def go_back(self):
        """Pop the last page from history and return it, or None if empty."""
        if not self._history:
            return None
        return self._history.pop()

    def is_empty(self):
        return len(self._history) == 0

    def clear(self):
        """Reset history — e.g. on logout."""
        self._history = []
