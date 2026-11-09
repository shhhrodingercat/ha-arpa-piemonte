"""ARPA Piemonte Home Assistant integration."""

from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import PLATFORMS


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up an ARPA Piemonte config entry."""
    if PLATFORMS:
        await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload an ARPA Piemonte config entry."""
    if not PLATFORMS:
        return True
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
