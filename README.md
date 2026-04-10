# Azure SOC Automation & Red/Blue Team Homelab

## 📌 Project Overview
This repository contains the code, scripts, and governance documentation for a comprehensive, end-to-end Security Operations Center (SOC) homelab. The project simulates a real-world corporate environment in Microsoft Azure, encompassing offensive Red Team attack simulations and defensive Blue Team automated triage pipelines.

## 🛠️ Technologies & Tools
* **Cloud Infrastructure:** Microsoft Azure (Virtual Machines, NSGs, Virtual Networks)
* **SIEM & Logging:** Azure Sentinel, Microsoft Defender for Cloud, KQL (Kusto Query Language)
* **Automation & Scripting:** Python, REST APIs, PowerShell
* **Artificial Intelligence:** Hugging Face LLM Integration (Mistral-7B) for automated alert triage
* **Offensive Tools:** GoPhish, MailHog (Credential Harvesting Simulation)

## 🔄 Engineering Lifecycle
This project was executed using a strict Software Development Life Cycle (SDLC) framework to ensure the security tools were built, tested, and documented to industry standards.

* **Requirements & R&D Discovery:** Conducted initial research and development to map out threat paths for local privilege escalation and credential harvesting, designing an Azure cloud architecture to capture these specific attack vectors.
* **Development:** Engineered a custom Python automation pipeline integrating Azure Sentinel APIs and Hugging Face LLMs to rapidly pull, analyze, and triage high-severity security alerts. 
* **Testing:** Executed live Red Team simulations (creating rogue backdoors, launching GoPhish campaigns) to rigorously test the detection logic and SIEM ingestion pipelines.
* **Deployment:** Deployed persistent PowerShell security scripts via Windows Task Scheduler for automated Data Loss Prevention (DLP) scanning, continuous threat hunting, and log retention.
* **Maintenance & Governance:** Formalized the operational lifecycle by drafting an Incident Response Playbook, an automated Daily Triage SOP, and a Corporate Identity Policy, ensuring the SDLC feedback loop continuously improves detection engineering.

## 📂 Repository Contents

### 1. Automation Pipeline (`/Automation_Pipeline`)
Contains `soc_automation.py`, a custom script that fetches recent incidents from Azure Sentinel via the Microsoft Authentication Library (MSAL). It utilizes a fallback-capable API connection to an LLM to generate instant threat summaries and remediation steps for Level 1 Analysts, outputting to `soc_automated_triage_report.txt`.

### 2. PowerShell Security Tools (`/PowerShell_Security_Tools`)
Custom operational scripts designed for proactive defense:
* **User Access Review:** Audits local endpoints to identify dormant accounts or unauthorized privilege escalations.
* **Threat Hunting:** Scans active processes for invalid cryptographic signatures to isolate potential malware.
* **Log Backup:** Automates the extraction and secure storage of Windows Security Event Logs.

### 3. Governance & Documentation (`/Governance_and_Documentation`)
Standardized business documentation formatted for SOC operations:
* **Incident Response Playbook:** NIST-aligned containment and eradication steps for Privilege Escalation (MITRE ATT&CK TA0004).
* **Daily Triage SOP:** Step-by-step workflow for analysts utilizing the AI-automation pipeline.
* **Corporate Security Policy:** Identity and Access Management (IAM) governance detailing password complexity and access reviews.

## 🚀 Key Achievements
* Successfully reduced theoretical Mean Time to Triage (MTTT) by automating alert context generation.
* Bridged the gap between offensive infrastructure build-outs and defensive detection engineering.
* Translated complex technical engineering into actionable corporate security documentation.
