# key.py
# 🔐 Final Key Assembler for 7SDS

def assemble(parts):
    """Combine string fragments from all .md files to reveal the true name."""
    return "-".join(parts).lower()

# Example usage:
# key = assemble(["Principle", "Mind", "Soul", "Spirit", "Life", "Truth", "Love"])
