"""Tiny application used by the code review POC."""

from sample_agent.greeting import greeting
from sample_agent.webhooks import is_allowed_webhook

__all__ = ["greeting", "is_allowed_webhook"]
