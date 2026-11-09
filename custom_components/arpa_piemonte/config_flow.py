"""Config flow for ARPA Piemonte."""

from __future__ import annotations

from typing import Any

from homeassistant.config_entries import ConfigFlow, ConfigFlowResult

from .const import DOMAIN


class ArpaPiemonteConfigFlow(ConfigFlow, domain=DOMAIN):
    """Set up the integration.

    Single config entry (``single_config_entry`` in the manifest). Service and
    station selection will be added here and in the options flow in Phase 4.
    """

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Confirm and create the entry."""
        if user_input is not None:
            return self.async_create_entry(title="ARPA Piemonte", data={})

        return self.async_show_form(step_id="user")
