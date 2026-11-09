#!/bin/sh
set -eu

EXPECTED_USER="minds_user"
SUDOERS_FILE="/etc/sudoers.d/leavitt-experiment-restarts"
SYSTEMCTL="/usr/bin/systemctl"

if [ "$(id -un)" != "$EXPECTED_USER" ]; then
    printf 'Run this script while logged in as %s.\n' "$EXPECTED_USER" >&2
    exit 1
fi

if [ ! -x "$SYSTEMCTL" ]; then
    printf '%s was not found or is not executable.\n' "$SYSTEMCTL" >&2
    exit 1
fi

temporary_file="$(mktemp)"
trap 'rm -f "$temporary_file"' EXIT HUP INT TERM

printf '%s ALL=(root) NOPASSWD: %s restart ollama.service, %s restart leavitt-client.service\n' \
    "$EXPECTED_USER" "$SYSTEMCTL" "$SYSTEMCTL" > "$temporary_file"

printf 'A one-time sudo password may be requested to install the narrow sudoers rule.\n'
sudo /usr/sbin/visudo -cf "$temporary_file"
sudo /usr/bin/install -o root -g root -m 0440 "$temporary_file" "$SUDOERS_FILE"
sudo /usr/sbin/visudo -cf "$SUDOERS_FILE"

printf 'Installed %s. Verifying non-interactive permissions...\n' "$SUDOERS_FILE"
sudo -n -l "$SYSTEMCTL" restart ollama.service >/dev/null
sudo -n -l "$SYSTEMCTL" restart leavitt-client.service >/dev/null
printf 'Passwordless Ollama and Leavitt client restarts are ready.\n'
