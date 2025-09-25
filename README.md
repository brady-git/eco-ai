# eco-ai

RAG + one-tool FastAPI service.

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # fill in keys

# start API
uvicorn app.main:app --reload --port 8000

# Salesforce (read-only)
SF_INSTANCE_URL=eco-battery.my.salesforce.com
SF_USERNAME=warranty@ecobattery.com
SF_PASSWORD=Thunderst1!
SF_SECURITY_TOKEN=

# Vector DB
CHROMA_DIR=./data/vectorstore
