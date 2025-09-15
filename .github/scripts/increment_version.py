from tomlkit import parse, dumps, array


def bump_patch(version: str) -> str:
    """Increment the patch version (X.Y.Z -> X.Y.Z+1)."""
    major, minor, patch = map(int, version.split("."))
    patch += 1
    return f"{major}.{minor}.{patch}"


def to_multiline(arr):
    """Force TOML arrays to be multiline."""
    new_arr = array().multiline(True)
    for v in arr:
        new_arr.append(v)
    return new_arr


with open("pyproject.toml", "r") as f:
    pyproject = parse(f.read())

# --- bump version ---
current_version = pyproject["project"]["version"]
new_version = bump_patch(current_version)
pyproject["project"]["version"] = new_version


# --- force all arrays to be multiline ---
def walk(node):
    if isinstance(node, list):
        return to_multiline(node)
    if isinstance(node, dict):
        for k, v in node.items():
            node[k] = walk(v)
    return node


pyproject = walk(pyproject)

# --- write back ---
with open("pyproject.toml", "w") as f:
    f.write(dumps(pyproject))

print(f"Version bumped: {current_version} → {new_version}")
