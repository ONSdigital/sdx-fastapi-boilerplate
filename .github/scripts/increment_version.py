import toml


def bump_patch(version: str) -> str:
    """Increment the patch version (X.Y.Z -> X.Y.Z+1)."""
    major, minor, patch = map(int, version.split("."))
    patch += 1
    return f"{major}.{minor}.{patch}"


# Load pyproject.toml
with open("pyproject.toml", "r") as f:
    pyproject = toml.load(f)

current_version = pyproject["project"]["version"]
new_version = bump_patch(current_version)

# Update version
pyproject["project"]["version"] = new_version

# Save pyproject.toml back
with open("pyproject.toml", "w") as f:
    toml.dump(pyproject, f)

print(f"Version bumped: {current_version} → {new_version}")
