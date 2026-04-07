---
title: 'Narrative Reporting REST APIs for Automated Report Generation'
description: 'Leverage NR REST APIs to automate report generation, download outputs, and integrate Narrative Reporting with downstream systems and scheduling tools.'
product: 'narrative-reporting'
subcategory: 'tips'
pubDate: '2026-04-01'
---

# Narrative Reporting REST APIs for Automated Report Generation

Oracle Narrative Reporting exposes a comprehensive REST API that enables programmatic control over report generation, job monitoring, output delivery, and package management. This guide covers practical API usage patterns, authentication, endpoint reference, and real-world integration examples for EPM administrators and architects.

## API Overview

The NR REST API enables automation of:

- **Report Generation**: Trigger Books and Report Packages to generate on-demand
- **Job Management**: Monitor generation status, retrieve logs, and handle failures
- **Output Download**: Fetch PDF/Excel outputs programmatically for integration
- **Scheduling**: Configure and manage automated report generation schedules
- **Package Administration**: Manage report packages, content, and metadata via API
- **Bursting Management**: Control bursting definitions and trigger bulk distributions
- **Audit and Logging**: Retrieve execution history and audit trails

## Authentication

NR APIs use OAuth 2.0 for secure authentication. You have two options:

**Option 1: OAuth Token (Recommended)**
- Enterprise applications with OAuth support
- Service accounts with API credentials
- Token-based authentication is more secure than basic auth

**Option 2: Basic Authentication** (Legacy)
- Simple scripts and ad-hoc integrations
- Username and password encoded in Base64
- Less secure; requires HTTPS

### Setting Up OAuth Authentication

1. **Create Service Account in EPM Cloud**:
   - Log in as EPM Cloud administrator
   - Navigate to **Administration** → **User Provisioning**
   - Create new user: "nr_api_service" (or similar)
   - Assign role: NR Administrator or NR Architect (depending on use case)
   - Generate API credentials (client ID and secret)

2. **Store Credentials Securely**:
   - Do not hardcode credentials in scripts
   - Use environment variables, secure vaults (HashiCorp Vault), or CI/CD secrets manager
   - Rotate credentials quarterly

3. **Obtain OAuth Token**:
   ```bash
   curl -X POST https://your-instance.oracle.com/rest/v2/oauth2/token \
     -d "grant_type=client_credentials" \
     -d "client_id=YOUR_CLIENT_ID" \
     -d "client_secret=YOUR_CLIENT_SECRET" \
     -H "Content-Type: application/x-www-form-urlencoded"
   ```
   Response:
   ```json
   {
     "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
     "token_type": "Bearer",
     "expires_in": 3600
   }
   ```

4. **Use Token in API Requests**:
   ```bash
   curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     https://your-instance.oracle.com/rest/v2/narrativeReporting/books
   ```

**Token Expiration**: Tokens expire after 1 hour. Refresh tokens automatically or request a new token for long-running scripts.

## Core API Endpoints

### Books Endpoints

**List All Books**
```
GET /rest/v2/narrativeReporting/books
```
Query Parameters:
- `limit`: Number of results (default 50, max 500)
- `offset`: Pagination offset
- `search`: Filter by book name (substring match)

Response:
```json
{
  "total": 125,
  "limit": 50,
  "offset": 0,
  "items": [
    {
      "id": "BOOK_Q4_2026_BOARD_PACK",
      "name": "Q4 2026 Board Financial Pack",
      "description": "Quarterly board reporting package",
      "owner": "john.doe@company.com",
      "created": "2026-01-15T10:30:00Z",
      "modified": "2026-03-28T14:45:00Z",
      "status": "Published"
    }
  ]
}
```

**Get Book Details**
```
GET /rest/v2/narrativeReporting/books/{bookId}
```
Returns: Full book metadata, structure, chapters, topics, content items

**Create Book Generation Job**
```
POST /rest/v2/narrativeReporting/books/{bookId}/jobs
Content-Type: application/json
```
Request Body:
```json
{
  "outputFormat": "PDF",
  "pov": {
    "entity": "ENTITY_001",
    "period": "2026.Q4",
    "scenario": "ACTUAL"
  },
  "metadata": {
    "requestedBy": "john.doe@company.com",
    "businessReason": "Monthly board pack distribution"
  }
}
```

Response:
```json
{
  "jobId": "JOB_20260401_001234",
  "bookId": "BOOK_Q4_2026_BOARD_PACK",
  "status": "SUBMITTED",
  "createdAt": "2026-04-01T08:00:00Z",
  "estimatedCompletionTime": "2026-04-01T08:02:30Z"
}
```

### Job Management Endpoints

**Get Job Status**
```
GET /rest/v2/narrativeReporting/jobs/{jobId}
```
Response:
```json
{
  "jobId": "JOB_20260401_001234",
  "bookId": "BOOK_Q4_2026_BOARD_PACK",
  "status": "IN_PROGRESS",
  "progress": {
    "percentComplete": 65,
    "currentStep": "Rendering graphics",
    "elapsedSeconds": 45
  },
  "outputDetails": {
    "format": "PDF",
    "filename": "Q4_2026_Board_Pack_ENTITY_001.pdf",
    "fileSize": null
  }
}
```

Status Values: SUBMITTED, IN_PROGRESS, COMPLETED, FAILED, CANCELLED

**Wait for Job Completion** (Polling Pattern):
```bash
#!/bin/bash

JOB_ID="JOB_20260401_001234"
MAX_WAIT=300  # 5 minutes
POLL_INTERVAL=5  # Check every 5 seconds

for ((i=0; i<$MAX_WAIT; i+=POLL_INTERVAL)); do
  STATUS=$(curl -s -H "Authorization: Bearer $TOKEN" \
    "https://your-instance.oracle.com/rest/v2/narrativeReporting/jobs/$JOB_ID" \
    | jq -r '.status')

  if [ "$STATUS" == "COMPLETED" ]; then
    echo "Job completed successfully"
    break
  elif [ "$STATUS" == "FAILED" ]; then
    echo "Job failed"
    exit 1
  fi

  echo "Status: $STATUS, waiting..."
  sleep $POLL_INTERVAL
done

if [ $i -ge $MAX_WAIT ]; then
  echo "Timeout waiting for job completion"
  exit 1
fi
```

**Download Generated Report**
```
GET /rest/v2/narrativeReporting/jobs/{jobId}/output
```
Query Parameters:
- `format`: PDF, EXCEL, HTML (must match original request)

Response: Binary file stream (PDF/Excel attachment)

Example cURL:
```bash
curl -H "Authorization: Bearer $TOKEN" \
  "https://your-instance.oracle.com/rest/v2/narrativeReporting/jobs/$JOB_ID/output?format=PDF" \
  -o "Q4_2026_Board_Pack.pdf"
```

**Get Job Logs**
```
GET /rest/v2/narrativeReporting/jobs/{jobId}/logs
```
Returns: Detailed log entries for debugging failed jobs
```json
{
  "jobId": "JOB_20260401_001234",
  "logs": [
    {
      "timestamp": "2026-04-01T08:00:01Z",
      "level": "INFO",
      "message": "Job submitted for BOOK_Q4_2026_BOARD_PACK"
    },
    {
      "timestamp": "2026-04-01T08:00:15Z",
      "level": "INFO",
      "message": "Loading book definition and POV"
    },
    {
      "timestamp": "2026-04-01T08:00:45Z",
      "level": "WARNING",
      "message": "Grid 'Division C P&L' took 3.2 seconds to render"
    }
  ]
}
```

### Report Packages Endpoints

**List All Report Packages**
```
GET /rest/v2/narrativeReporting/reportPackages
```

**Trigger Report Package Generation**
```
POST /rest/v2/narrativeReporting/reportPackages/{packageId}/jobs
```
Request Body:
```json
{
  "includeAllDoclets": true,
  "outputFormat": "PDF",
  "pov": {
    "entity": "ENTITY_001"
  }
}
```

**Get Package Job Status**
```
GET /rest/v2/narrativeReporting/reportPackages/{packageId}/jobs/{jobId}
```

## Real-World Integration Examples

### Example 1: Nightly Board Pack Generation and SharePoint Upload

**Scenario**: Generate monthly board financial pack at 8 PM daily and upload to SharePoint.

**Implementation** (Python):
```python
#!/usr/bin/env python3

import os
import time
import requests
import json
from datetime import datetime
from azure.identity import ClientSecretCredential
from azure.storage.sharepoint import SharePointClient

# Configuration
NR_INSTANCE = "https://your-instance.oracle.com"
NR_CLIENT_ID = os.getenv("NR_CLIENT_ID")
NR_CLIENT_SECRET = os.getenv("NR_CLIENT_SECRET")
BOOK_ID = "BOOK_Q4_2026_BOARD_PACK"
SHAREPOINT_SITE = "https://yourcompany.sharepoint.com/sites/Finance"
SHAREPOINT_LIBRARY = "Shared Documents"

def get_oauth_token():
    """Obtain OAuth token for NR API"""
    url = f"{NR_INSTANCE}/rest/v2/oauth2/token"
    payload = {
        "grant_type": "client_credentials",
        "client_id": NR_CLIENT_ID,
        "client_secret": NR_CLIENT_SECRET
    }
    response = requests.post(url, data=payload)
    response.raise_for_status()
    return response.json()["access_token"]

def trigger_book_generation(token, book_id):
    """Trigger book generation via NR API"""
    url = f"{NR_INSTANCE}/rest/v2/narrativeReporting/books/{book_id}/jobs"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "outputFormat": "PDF",
        "pov": {
            "entity": "ALL_ENTITIES",
            "period": "LATEST",
            "scenario": "ACTUAL"
        }
    }
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()["jobId"]

def wait_for_job_completion(token, job_id, max_wait=300):
    """Poll job status until completion"""
    url = f"{NR_INSTANCE}/rest/v2/narrativeReporting/jobs/{job_id}"
    headers = {"Authorization": f"Bearer {token}"}

    elapsed = 0
    while elapsed < max_wait:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        job = response.json()

        if job["status"] == "COMPLETED":
            return True
        elif job["status"] == "FAILED":
            raise Exception(f"Job failed: {job.get('errorMessage', 'Unknown error')}")

        print(f"Job {job_id} status: {job['status']}, progress: {job['progress']['percentComplete']}%")
        time.sleep(10)
        elapsed += 10

    raise TimeoutError(f"Job did not complete within {max_wait} seconds")

def download_report(token, job_id):
    """Download generated report PDF"""
    url = f"{NR_INSTANCE}/rest/v2/narrativeReporting/jobs/{job_id}/output"
    headers = {"Authorization": f"Bearer {token}"}
    params = {"format": "PDF"}

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"BoardPack_{timestamp}.pdf"

    with open(filename, "wb") as f:
        f.write(response.content)

    return filename

def upload_to_sharepoint(filename, sharepoint_site, library):
    """Upload PDF to SharePoint"""
    credential = ClientSecretCredential(
        tenant_id=os.getenv("AZURE_TENANT_ID"),
        client_id=os.getenv("AZURE_CLIENT_ID"),
        client_secret=os.getenv("AZURE_CLIENT_SECRET")
    )

    # Implementation depends on SharePoint SDK
    # This is pseudocode; actual implementation uses microsoft.graph or SharePoint SDK
    print(f"Uploading {filename} to {sharepoint_site}/{library}")
    # ... SharePoint upload logic ...

def main():
    try:
        print("Starting nightly board pack generation...")

        # Step 1: Get OAuth token
        token = get_oauth_token()
        print("OAuth token obtained")

        # Step 2: Trigger book generation
        job_id = trigger_book_generation(token, BOOK_ID)
        print(f"Book generation triggered. Job ID: {job_id}")

        # Step 3: Wait for completion
        wait_for_job_completion(token, job_id)
        print(f"Job {job_id} completed successfully")

        # Step 4: Download report
        filename = download_report(token, job_id)
        print(f"Report downloaded: {filename}")

        # Step 5: Upload to SharePoint
        upload_to_sharepoint(filename, SHAREPOINT_SITE, SHAREPOINT_LIBRARY)
        print(f"Report uploaded to SharePoint")

        print("Nightly board pack generation completed successfully")

    except Exception as e:
        print(f"Error: {e}")
        # Send alert to Slack/email
        exit(1)

if __name__ == "__main__":
    main()
```

**Scheduling**: Use Linux cron or Windows Task Scheduler to run at 8 PM:
```bash
# Cron: Run at 8 PM daily
0 20 * * * /usr/local/bin/generate_board_pack.py
```

### Example 2: Trigger Report from Task Manager Close Event

**Scenario**: Automatically generate P&L report when month-end close completes in Task Manager.

**Implementation** (Oracle Automate Integration):
```bash
# EPM Automate script triggered by Task Manager close event

# Get OAuth token
TOKEN=$(curl -s -X POST https://your-instance.oracle.com/rest/v2/oauth2/token \
  -d "grant_type=client_credentials" \
  -d "client_id=$NR_CLIENT_ID" \
  -d "client_secret=$NR_CLIENT_SECRET" | grep -o '"access_token":"[^"]*' | cut -d'"' -f4)

# Trigger book generation
JOB_RESPONSE=$(curl -s -X POST https://your-instance.oracle.com/rest/v2/narrativeReporting/books/BOOK_MONTHLY_PL/jobs \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "outputFormat": "PDF",
    "pov": {
      "entity": "ALL",
      "period": "LATEST"
    }
  }')

JOB_ID=$(echo $JOB_RESPONSE | grep -o '"jobId":"[^"]*' | cut -d'"' -f4)

echo "P&L report generation triggered. Job ID: $JOB_ID"

# Poll for completion
while true; do
  JOB_STATUS=$(curl -s https://your-instance.oracle.com/rest/v2/narrativeReporting/jobs/$JOB_ID \
    -H "Authorization: Bearer $TOKEN" | grep -o '"status":"[^"]*' | cut -d'"' -f4)

  if [ "$JOB_STATUS" == "COMPLETED" ]; then
    echo "P&L report generation completed"

    # Download report
    curl -s -H "Authorization: Bearer $TOKEN" \
      "https://your-instance.oracle.com/rest/v2/narrativeReporting/jobs/$JOB_ID/output?format=PDF" \
      -o "Monthly_PL_Report.pdf"

    # Email to CFO
    mail -s "Monthly P&L Report Generated" cfo@company.com < /dev/null
    break
  elif [ "$JOB_STATUS" == "FAILED" ]; then
    echo "P&L report generation failed"
    exit 1
  fi

  echo "Waiting for job completion... Status: $JOB_STATUS"
  sleep 10
done
```

### Example 3: Bulk Excel Export for Data Warehouse

**Scenario**: Export monthly actuals from multiple Books to Excel format for data warehouse ingestion.

**Implementation** (Bash):
```bash
#!/bin/bash

# Configuration
TOKEN=$1  # Pass OAuth token as parameter
OUTPUT_DIR="/data/exports/$(date +%Y%m%d)"
mkdir -p $OUTPUT_DIR

# Books to export
declare -a BOOKS=(
  "BOOK_MONTHLY_PL"
  "BOOK_MONTHLY_BS"
  "BOOK_MONTHLY_CF"
)

# Entity list
declare -a ENTITIES=(
  "ENTITY_001"
  "ENTITY_002"
  "ENTITY_003"
)

echo "Starting bulk export at $(date)"

JOB_IDS=()

# Trigger all jobs (don't wait for each one)
for BOOK in "${BOOKS[@]}"; do
  for ENTITY in "${ENTITIES[@]}"; do
    # Trigger generation
    RESPONSE=$(curl -s -X POST https://your-instance.oracle.com/rest/v2/narrativeReporting/books/$BOOK/jobs \
      -H "Authorization: Bearer $TOKEN" \
      -H "Content-Type: application/json" \
      -d "{
        \"outputFormat\": \"EXCEL\",
        \"pov\": {
          \"entity\": \"$ENTITY\",
          \"period\": \"LATEST\"
        }
      }")

    JOB_ID=$(echo $RESPONSE | grep -o '"jobId":"[^"]*' | cut -d'"' -f4)
    JOB_IDS+=($JOB_ID)

    echo "Triggered $BOOK for $ENTITY. Job ID: $JOB_ID"
  done
done

echo "All jobs triggered. Waiting for completion..."

# Wait for all jobs to complete
for JOB_ID in "${JOB_IDS[@]}"; do
  while true; do
    STATUS=$(curl -s https://your-instance.oracle.com/rest/v2/narrativeReporting/jobs/$JOB_ID \
      -H "Authorization: Bearer $TOKEN" | grep -o '"status":"[^"]*' | cut -d'"' -f4)

    if [ "$STATUS" == "COMPLETED" ]; then
      # Download file
      FILENAME=$(curl -s https://your-instance.oracle.com/rest/v2/narrativeReporting/jobs/$JOB_ID \
        -H "Authorization: Bearer $TOKEN" | grep -o '"filename":"[^"]*' | cut -d'"' -f4)

      curl -s -H "Authorization: Bearer $TOKEN" \
        "https://your-instance.oracle.com/rest/v2/narrativeReporting/jobs/$JOB_ID/output?format=EXCEL" \
        -o "$OUTPUT_DIR/$FILENAME"

      echo "Downloaded $FILENAME"
      break
    elif [ "$STATUS" == "FAILED" ]; then
      echo "Job $JOB_ID failed"
      break
    fi

    sleep 5
  done
done

echo "Bulk export completed at $(date)"

# Load exported files into data warehouse
# ... ETL process ...
```

## Error Handling and Retry Patterns

**Handling Transient Failures**:
```python
import time
import requests

def trigger_with_retry(token, book_id, max_retries=3):
    """Trigger book generation with exponential backoff retry"""
    for attempt in range(max_retries):
        try:
            url = f"{NR_INSTANCE}/rest/v2/narrativeReporting/books/{book_id}/jobs"
            headers = {"Authorization": f"Bearer {token}"}
            payload = {"outputFormat": "PDF"}

            response = requests.post(url, json=payload, headers=headers, timeout=30)

            if response.status_code == 429:  # Rate limited
                wait_time = 2 ** attempt  # Exponential backoff
                print(f"Rate limited. Waiting {wait_time} seconds...")
                time.sleep(wait_time)
                continue

            response.raise_for_status()
            return response.json()["jobId"]

        except requests.exceptions.Timeout:
            print(f"Timeout on attempt {attempt + 1}")
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
        except requests.exceptions.ConnectionError as e:
            print(f"Connection error: {e}")
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)

    raise Exception(f"Failed to trigger book after {max_retries} retries")
```

## API Best Practices

1. **Authentication**: Use OAuth tokens; rotate credentials quarterly; never hardcode secrets
2. **Error Handling**: Implement retry logic with exponential backoff for transient failures
3. **Polling Strategy**: For long-running jobs, use polling interval of 10-30 seconds
4. **Rate Limiting**: NR API has rate limits (contact Oracle for specifics); implement throttling
5. **Logging**: Log all API calls (job triggers, status checks, downloads) for troubleshooting
6. **Monitoring**: Set up alerts for failed jobs; track performance metrics
7. **Documentation**: Document API usage patterns for your organization; provide examples
8. **Testing**: Test API integrations in non-production first; validate error scenarios

## Integration with EPM Automate

In addition to REST APIs, Oracle provides EPM Automate commands for NR:

**Generate Book**:
```bash
RUNBOOK BOOK_MONTHLY_PL PDF ENTITY_001
```

**Download Output**:
```bash
DOWNLOADFILE /narrativeReporting/jobs/JOB_20260401_001234/output monthly_pl.pdf
```

**List Books**:
```bash
LISTBOOKS
```

## Conclusion

The Narrative Reporting REST API enables powerful automation of report generation and distribution. Whether integrating with Task Manager, SharePoint, data warehouses, or custom applications, the API provides the flexibility and control needed to build sophisticated reporting automation. Start with simple use cases (nightly generation, PDF download), then expand to complex orchestration patterns (bursting, conditional triggering, multi-step workflows).

For detailed API documentation, visit Oracle EPM Cloud REST API Reference or contact your Oracle support representative.
