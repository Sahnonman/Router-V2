# Router-V2

This app displays a map of Saudi Arabia with optional data points loaded from a Google Sheet. 

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Provide your Google service account credentials in `.streamlit/secrets.toml`:
   ```toml
   [gcp_service_account]
   type = "service_account"
   project_id = "your-project"
   private_key_id = "..."
   private_key = "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
   client_email = "...@your-project.iam.gserviceaccount.com"
   client_id = "..."
   auth_uri = "https://accounts.google.com/o/oauth2/auth"
   token_uri = "https://oauth2.googleapis.com/token"
   auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
   client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509/..."
   ```
   An example file is provided at `.streamlit/secrets.toml.example`.
3. Run the Streamlit app:
   ```bash
   streamlit run streamlit_app_app.py
   ```
