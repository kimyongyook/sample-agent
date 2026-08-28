def greeting(name: str) -> str:
    """Return a small, deterministic greeting."""
    cleaned = name.strip()
    if not cleaned:
        raise ValueError("name must not be empty")
    return f"Hello, {cleaned}!"

