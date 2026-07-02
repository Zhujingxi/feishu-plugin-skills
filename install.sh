#!/usr/bin/env bash
set -euo pipefail

REPO_OWNER="${REPO_OWNER:-Zhujingxi}"
REPO_NAME="${REPO_NAME:-feishu-plugin-skills}"
BRANCH="${BRANCH:-main}"
SKILL_NAME="feishu-plugin-development"
CATEGORY="productivity"

if [ -n "${HERMES_PROFILE:-}" ]; then
  HERMES_HOME_DIR="${HERMES_HOME:-$HOME/.hermes/profiles/$HERMES_PROFILE}"
else
  HERMES_HOME_DIR="${HERMES_HOME:-$HOME/.hermes}"
fi

DEST_DIR="$HERMES_HOME_DIR/skills/$CATEGORY/$SKILL_NAME"
TMP_DIR="$(mktemp -d 2>/dev/null || mktemp -d -t feishu-plugin-skill)"
ARCHIVE="$TMP_DIR/source.tar.gz"
EXTRACT_DIR="$TMP_DIR/extract"

cleanup() {
  rm -rf "$TMP_DIR"
}
trap cleanup EXIT

command_exists() {
  command -v "$1" >/dev/null 2>&1
}

if ! command_exists curl; then
  echo "Error: curl is required to install this skill." >&2
  exit 1
fi

mkdir -p "$EXTRACT_DIR"
URL="https://codeload.github.com/$REPO_OWNER/$REPO_NAME/tar.gz/refs/heads/$BRANCH"

echo "Downloading $REPO_OWNER/$REPO_NAME@$BRANCH..."
curl -fsSL "$URL" -o "$ARCHIVE"

tar -xzf "$ARCHIVE" -C "$EXTRACT_DIR" --strip-components=1

if [ ! -f "$EXTRACT_DIR/SKILL.md" ]; then
  echo "Error: downloaded archive does not contain SKILL.md at repository root." >&2
  exit 1
fi

mkdir -p "$(dirname "$DEST_DIR")"
rm -rf "$DEST_DIR.tmp"
mkdir -p "$DEST_DIR.tmp"

# Copy only the skill payload and installer/docs, not .git metadata.
cp "$EXTRACT_DIR/SKILL.md" "$DEST_DIR.tmp/"
cp "$EXTRACT_DIR/README.md" "$DEST_DIR.tmp/" 2>/dev/null || true
cp "$EXTRACT_DIR/install.sh" "$DEST_DIR.tmp/" 2>/dev/null || true
if [ -d "$EXTRACT_DIR/references" ]; then
  cp -R "$EXTRACT_DIR/references" "$DEST_DIR.tmp/"
fi

rm -rf "$DEST_DIR"
mv "$DEST_DIR.tmp" "$DEST_DIR"

chmod +x "$DEST_DIR/install.sh" 2>/dev/null || true

echo "Installed $SKILL_NAME to: $DEST_DIR"
echo "Restart Hermes or run /reload-skills, then load it with: /skill $SKILL_NAME"
