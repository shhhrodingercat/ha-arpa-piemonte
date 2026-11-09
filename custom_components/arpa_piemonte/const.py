"""Constants for the ARPA Piemonte integration."""

from __future__ import annotations

from homeassistant.const import Platform

DOMAIN = "arpa_piemonte"

# Platform modules live at the integration root (sensor.py, ...), not in a
# sub-package. Empty until the first service adapter lands (Phase 4).
PLATFORMS: list[Platform] = []
