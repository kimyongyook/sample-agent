def is_allowed_webhook(url: str) -> bool:
    return url.startswith("https://hooks.example.com")
