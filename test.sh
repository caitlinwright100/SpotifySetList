ENV_VARIABLES=$(aws ssm get-parameter --name "/spotify_setlist_envs" --with-decryption --query "Parameter.Value" --output text)
TEMP_FILE=$(mktemp)
# Parse JSON and export variables
while IFS='=' read -r key value; do
    echo "$key=$value" >> "$TEMP_FILE"

# Move variables to /etc/environment
# sudo mv "$TEMP_FILE" /etc/environment

# Optional: Reload environment variables for current session
# source /etc/environment

# Verification: Print contents of /etc/environment to verify
echo "Environment variables moved to /etc/environment:"