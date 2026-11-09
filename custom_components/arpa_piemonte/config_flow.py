"""Config flow for ARPA Piemonte."""

from __future__ import annotations

import voluptuous as vol
from homeassistant.config_entries import ConfigFlow, ConfigFlowResult

from .const import DOMAIN


class ArpaPiemonteConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle the initial setup of the integration."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, object] | None = None
    ) -> ConfigFlowResult:
        """Create the single provider config entry.

        This intentionally minimal flow only establishes the integration entry.
        Service and station selection will be added after source reconnaissance
        and the configuration model have been agreed.
        """
        if user_input is not None:
            return self.async_create_entry(title="ARPA Piemonte", data={})

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({}),
        )
