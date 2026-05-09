# BYD EV Pro Home Assistant Integration

HACS custom component. Public repo: `ant0nkr/ev-pro-ha-integration`.

**Doc index:** `../byd-ev-pro-doc/INDEX.md`
**Workspace rules:** `../CLAUDE.md`

No build step. Copy `custom_components/byd_ev_pro/` to HA config dir.

---

## Hard rules (HA-specific)

1. **Public repo** — sanitize ALL user-facing copy and release notes.
   NO FIDs, device type numbers, hex values, signal names, DiLink internals,
   MinIO/Cloudflare references, Android package names. User-facing only.

2. **Show last-known values with `last_updated`** — never "unavailable" just because the car is off.
   Queue service calls through relay (24h TTL on relay side).

3. **Webhook payload schema changes touch the head unit too** — coordinate.

4. **HA instance**: `hassio.matrixnetwork.online`.
   Car pushes sensors via webhook. Voice/automation calls HA services via token.

5. **Commits**: `ant0nkr` profile, no `Co-Authored-By`, no work email.

---

## Doc shortcuts

- HA integration architecture (in head-unit-app docs) → `../byd-ev-pro-doc/architecture/02-head-unit-app.md`
- Webhook payload schema → search `architecture/` for HA / webhook
- Release sanitization rules → `../CLAUDE.md` §6
