"""Authentication tests for the Homework 2 endpoints.

Everything here runs offline: no Langfuse, no Docker, and no model provider
key. The tracing side of Homework 2 is checked by reading the recorded spans
in Langfuse (Part E), not from these tests.
"""

from __future__ import annotations

from pathlib import Path

import pytest
from fastapi import HTTPException

from server import app as server_app


def test_create_session_rejects_claimed_role(world: dict[str, Path]) -> None:
    """User 1 is a shopper in the database, so a merchant claim is refused."""
    server_app._SESSIONS.clear()

    with pytest.raises(HTTPException) as exc_info:
        server_app.create_session(
            server_app.SessionCreate(user_id=1, role="merchant")
        )

    assert exc_info.value.status_code == 403
    assert server_app._SESSIONS == {}


def test_token_does_not_authorize_another_session(world: dict[str, Path]) -> None:
    """A token issued for one session cannot authorize a different session."""
    server_app._SESSIONS.clear()
    merchant = server_app.create_session(
        server_app.SessionCreate(user_id=9002, role="merchant")
    )
    shopper = server_app.create_session(
        server_app.SessionCreate(user_id=1, role="shopper")
    )

    with pytest.raises(HTTPException) as exc_info:
        server_app._authorize(
            shopper["session_id"], f"Bearer {merchant['token']}"
        )

    assert exc_info.value.status_code == 403

    # The token still works for the session it was issued for.
    ctx = server_app._authorize(
        merchant["session_id"], f"Bearer {merchant['token']}"
    )
    assert ctx.user_id == 9002
    assert ctx.role == "merchant"
