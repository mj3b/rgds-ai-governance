```mermaid
flowchart LR
  H[Humans] -->|Only actors who change state| R[RGDS System of Record]
  R -->|Optional request: read-only inputs| A[AI Assist Non-Agentic]
  A -->|Advisory output only| R
  R --> D[Delivery Tooling]
  H -->|Human-mediated publish/update| D

  A -.->|Blocked| D
  A -.->|Blocked| R

```

