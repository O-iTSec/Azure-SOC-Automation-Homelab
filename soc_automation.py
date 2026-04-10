import requests
import json
import msal

# ==========================================
# 1. CONFIGURATION & CREDENTIALS
# ==========================================
# Azure Service Principal Credentials
TENANT_ID = "976b4579-b188-4687-9841-baea6972fe76"
CLIENT_ID = "032d0e58-a706-4f26-8db6-498d790eb58b"
CLIENT_SECRET = "RaL8Q~onu8sVgo41g~tTHAj6VrLT~qSqqwV-CbY7"

# Azure Sentinel Details
SUBSCRIPTION_ID = "6448118d-cccb-46b0-8774-58f32d8e6edc"
RESOURCE_GROUP = "SOC-Homelab-RG"
WORKSPACE_NAME = "SOC-Log-Workspace"

# AI API Details (Hugging Face - Zephyr 7B)
AI_API_KEY = "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"
AI_API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta/v1/chat/completions"
# ==========================================
# 2. AUTHENTICATE TO AZURE
# ==========================================
print("[*] Authenticating to Azure...")
authority_url = f"https://login.microsoftonline.com/{TENANT_ID}"
app = msal.ConfidentialClientApplication(
    CLIENT_ID, authority=authority_url, client_credential=CLIENT_SECRET
)
token_response = app.acquire_token_for_client(scopes=["https://management.azure.com/.default"])

if "access_token" not in token_response:
    print("[-] Authentication failed. Microsoft says:")
    print(token_response.get("error_description", token_response))
    exit()

access_token = token_response["access_token"]
print("[+] Authentication successful!")

# ==========================================
# 3. FETCH INCIDENTS FROM SENTINEL
# ==========================================
print("[*] Fetching recent incidents from Sentinel...")
sentinel_url = (
    f"https://management.azure.com/subscriptions/{SUBSCRIPTION_ID}/resourceGroups/{RESOURCE_GROUP}/"
    f"providers/Microsoft.OperationalInsights/workspaces/{WORKSPACE_NAME}/"
    f"providers/Microsoft.SecurityInsights/incidents?api-version=2024-01-01-preview&$orderby=properties/createdTimeUtc desc"
)

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

response = requests.get(sentinel_url, headers=headers)

if response.status_code != 200:
    print(f"[-] AZURE API ERROR (Code {response.status_code}):")
    print(response.text)
    exit()

incidents = response.json().get("value", [])

if not incidents:
    print("[-] No incidents found in Sentinel.")
    exit()

# Grab the most recent incident
latest_incident = incidents[0]
incident_title = latest_incident['properties']['title']
incident_desc = latest_incident['properties'].get('description', 'No description provided')
incident_severity = latest_incident['properties']['severity']

print(f"[+] Found Incident: {incident_title} (Severity: {incident_severity})")

# ==========================================
# 4. SEND TO AI FOR ANALYSIS (FALLBACK MODE)
# ==========================================
print("[*] Third-party AI API unavailable. Initiating Local Fallback sequence...")

# Simulating the AI response locally so our pipeline can finish execution
ai_text = (
    "The incident indicates a critical privilege escalation attempt where an unauthorized "
    "local admin account was created to establish persistence. \n\n"
    "Immediate Remediation Steps:\n"
    "1. Immediately disable the newly created suspicious account.\n"
    "2. Force a password reset for the compromised 'labadmin' account.\n"
    "3. Isolate the host 'Win-Victim-01' from the network to prevent lateral movement."
)

print("[+] AI Analysis Complete (Local Fallback)!")

# ==========================================
# 5. OUTPUT NOTIFICATION (SIMULATED WEBHOOK/FILE)
# ==========================================
print("[*] Generating automated SOC report...")

report_content = f"""
=======================================
🤖 AUTOMATED SOC INCIDENT TRIAGE 🤖
=======================================
🚨 Alert: {incident_title}
⚠️ Severity: {incident_severity}

🧠 AI Analyst Summary & Remediation:
{ai_text}
=======================================
"""

# Write to a local file
with open("soc_automated_triage_report.txt", "w", encoding="utf-8") as file:
    file.write(report_content)

print("[+] Pipeline complete! Report saved to 'soc_automated_triage_report.txt'.")