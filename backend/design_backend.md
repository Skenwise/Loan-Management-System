backend/
 ├── core/                  # Shared primitives & infrastructure
 │    ├── time.py            # ValueDate, PostingDateTime
 │    ├── money.py           # Money primitive
 │    ├── ids.py             # AccountID, LoanID, TransactionID, CustomerID
 │    ├── errors.py          # Domain exceptions
 │    ├── database.py        # DB connection & session
 │    └── config.py          # App configuration
 │
 ├── loans/                 # Loan product logic
 │    ├── loan.py            # Loan entity, lifecycle
 │    ├── schedule.py        # Amortization & repayment schedules
 │    ├── interest.py        # Interest calculations
 │    ├── disbursement.py    # Loan funding
 │    └── repayment.py       # Payment handling
 │
 ├── accounts/              # Ledger accounts
 │    ├── account.py         # Account entity
 │    ├── chart_of_accounts.py
 │    ├── journal.py
 │    └── posting.py
 │
 ├── payments/              # Money movement
 │    ├── inbound.py
 │    ├── outbound.py
 │    ├── providers/         # Integrations
 │    └── settlement.py
 │
 ├── currency/              # Multi-currency support
 │    ├── currency.py
 │    ├── exchange_rate.py
 │    └── fx_revaluation.py
 │
 ├── tenants/               # Multi-tenant isolation
 │    ├── tenant.py
 │    └── context.py
 │
 ├── identity/              # Security & users
 │    ├── user.py
 │    ├── role.py
 │    ├── permission.py
 │    └── auth.py
 │
 ├── audit/                 # Logging & reconciliation
 │    ├── audit_log.py
 │    ├── reconciliation.py
 │    └── controls.py
 │
 ├── reporting/             # Read-only projections
 │    ├── loan_reports.py
 │    ├── ledger_views.py
 │    └── compliance.py
 │
 └── app/                   # FastAPI application entry
      ├── __init__.py
      ├── main.py            # FastAPI app instance
      ├── routes/            # API endpoints
      │    ├── loans.py
      │    ├── accounts.py
      │    └── payments.py
      └── dependencies.py    # DI & common dependencies (DB, Auth, Config)
