"""Display your Homework 1 mark: uv run python show_grade.py."""

from hashlib import sha256

SALT = "60b7c6ad2b3fa703a5e6b675dca07726"
GRADE_HASH = "a3269252ca6f64d8b95f4a6f41c0ae4a3fd595985207c2136837dabeec5f3db0"

# Match the stored hash against each possible whole-number mark.
for mark in range(101):
    candidate = sha256(f"{SALT}:{mark}".encode("utf-8")).hexdigest()
    if candidate == GRADE_HASH:
        print(f"Homework 1: {mark}/100")
        break
else:
    raise RuntimeError("The mark could not be verified. Please contact the instructor.")
