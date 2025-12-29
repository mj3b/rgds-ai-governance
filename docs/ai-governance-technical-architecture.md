```mermaid
flowchart LR
  H[Humans\n(Approver/Reviewer/Lead)] -->|only actors who change state| R[RGDS System of Record\nDecision Log + Evidence + State]
  R -->|optional request\n(read-only inputs)| A[Non-Agentic AI Assist\n(stateless, bounded)]
  A -->|advisory output only\n(no outcome/state writes)| R
  R --> X[Delivery Tooling\n(Jira/Docs/BI)\n(read models)]
  H -->|human-mediated publish/update| X

  A -.->|blocked| X
  A -.->|blocked| R
```

```mermaid
flowchart TB
  LA[Layer A\nGovernance & Authority] --> LB[Layer B\nRGDS Core (Deterministic)]
  LB --> LC[Layer C\nAI Assist (Bounded, Stateless)]
  LB --> LD[Layer D\nDelivery Integrations]
  LB --> LE[Layer E\nAudit & Controls]
  LC --> LE
```

```mermaid
flowchart LR
  EP1[EP1: Human signature required\nfor state transitions] --> RGDS[RGDS State Machine]
  EP2[EP2: AI write boundary\nadvisory fields only] --> OUT[AI Output Handler]
  EP3[EP3: External writes require\nhuman-mediated commit] --> INT[Integrations (Jira/Docs/BI)]

  AI[AI Assist] -.->|cannot close/approve| RGDS
  AI -.->|cannot publish/update| INT
```
