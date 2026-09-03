# fleet census

`census.json` is regenerated on every ledger run from the live agent registry.
Each agent carries two separate status fields, and they are separate on
purpose — conflating "registered" with "running" is how a fleet gets oversold.

- **registered** — the agent exists in the registry. Every listed agent is
  registered.
- **running** — true only when all three hold: the fleet is not paused, the
  agent is not parked, and something actually schedules its cadence
  (an `on_demand` agent has no scheduler, so it is registered but not running).

**Fleet pause state is read from the pause marker the fleet itself honours.**
When the fleet is paused, every agent reports `running: false`, because the
cadence entry points are gated closed. `census.json` records `fleet_paused` so
the reason a fully-registered fleet shows nothing running is visible, not
mysterious.

No descriptions, prompts or file paths are published here — only the six
fields above.
