# src/provider.py
"""Single place where VERA talks to an LLM. Swap providers here, nowhere else."""

import json
import os
import re
import requests

API_URL = "https://api.anthropic.com/v1/messages"
API_VERSION = "2023-06-01"

# Haiku 4.5 is the cheapest current Claude ($1/$5 per million tokens).
# Bump to "claude-sonnet-5" if explanation quality needs it.
DEFAULT_MODEL = os.environ.get("VERA_MODEL", "claude-haiku-4-5-20251001")


class LLMUnavailable(Exception):
    """No key, LLM disabled, or the API call failed. Callers fall back."""


def llm_mode() -> str:
    return os.environ.get("LLM_MODE", "CLOUD").upper()


def get_api_key() -> str:
    """Session state first (sidebar field, added later), then environment."""
    try:
        import streamlit as st
        k = st.session_state.get("api_key")
        if k:
            return str(k).strip()
    except Exception:
        pass
    return (os.environ.get("ANTHROPIC_API_KEY") or "").strip()


def available() -> bool:
    return llm_mode() != "OFF" and bool(get_api_key())


def complete(system: str, user: str, max_tokens: int = 400,
             temperature: float = 0.1, prefill: str = None,
             model: str = None) -> str:
    """Send one message. Returns the text. Raises LLMUnavailable on any failure."""
    if llm_mode() == "OFF":
        raise LLMUnavailable("LLM_MODE is OFF")

    key = get_api_key()
    if not key:
        raise LLMUnavailable("No ANTHROPIC_API_KEY set")

    messages = [{"role": "user", "content": user}]
    if prefill:
        messages.append({"role": "assistant", "content": prefill})

    try:
        r = requests.post(
            API_URL,
            headers={
                "x-api-key": key,
                "anthropic-version": API_VERSION,
                "content-type": "application/json",
            },
            json={
                "model": model or DEFAULT_MODEL,
                "max_tokens": max_tokens,
                "temperature": temperature,
                "system": system,
                "messages": messages,
            },
            timeout=60,
        )
    except requests.RequestException as e:
        raise LLMUnavailable(f"Network error: {e}")

    if r.status_code == 429:
        raise LLMUnavailable("Rate limited")
    if r.status_code == 401:
        raise LLMUnavailable("Invalid API key")
    if r.status_code != 200:
        raise LLMUnavailable(f"HTTP {r.status_code}: {r.text[:200]}")

    try:
        blocks = r.json()["content"]
        text = "".join(b["text"] for b in blocks if b.get("type") == "text")
    except Exception as e:
        raise LLMUnavailable(f"Unexpected response shape: {e}")

    return (prefill + text) if prefill else text.strip()


def complete_json(system: str, user: str, max_tokens: int = 400,
                  model: str = None) -> dict:
    """Same, but seeds an opening brace so the reply is a bare JSON object."""
    raw = complete(system, user, max_tokens=max_tokens,
                   prefill="{", model=model)
    raw = re.sub(r"^```(?:json)?|```$", "", raw.strip(), flags=re.MULTILINE).strip()
    try:
        return json.loads(raw)
    except json.JSONDecodeError as e:
        raise LLMUnavailable(f"Model did not return valid JSON: {e}")


if __name__ == "__main__":
    print(f"Model: {DEFAULT_MODEL}")
    print(f"Mode:  {llm_mode()}")
    print(f"Key:   {'set (' + get_api_key()[:12] + '...)' if get_api_key() else 'NOT SET'}")
    print("-" * 50)
    try:
        print("Plain call:", complete("Reply in exactly three words.", "Say hello.", max_tokens=20))
    except LLMUnavailable as e:
        print("Plain call FAILED:", e)
    try:
        print("JSON call: ", complete_json(
            "Return JSON only.",
            'Return exactly: {"units": {"tensile_strength": "MPa"}}',
            max_tokens=60))
    except LLMUnavailable as e:
        print("JSON call FAILED:", e)