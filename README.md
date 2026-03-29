# API Test Framework

![Tests](https://github.com/VivekanandUsingh/api-test-framework/actions/workflows/api-tests.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![pytest](https://img.shields.io/badge/pytest-8.1-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

A production-grade REST API test automation framework built with Python and pytest. Demonstrates data-driven testing, reusable client architecture, CI/CD integration, and comprehensive assertion patterns — built to the standards expected at QA Architect level.

---

## Framework Architecture

```
api-test-framework/
├── config/
│   └── config.yaml          # Centralized config — URLs, endpoints, test data
├── utils/
│   └── api_client.py        # Reusable requests wrapper with logging
├── tests/
│   ├── test_users.py        # User CRUD test suite (12 tests)
│   └── test_auth.py         # Login & registration test suite (11 tests)
├── reports/                 # Auto-generated HTML test reports
├── .github/
│   └── workflows/
│       └── api-tests.yml    # GitHub Actions CI/CD pipeline
├── conftest.py              # Shared pytest fixtures
├── pytest.ini               # pytest configuration
└── requirements.txt         # Dependencies
```

---

## What This Framework Demonstrates

- **Reusable API client** — single wrapper handling all HTTP methods, headers, timeouts, and response logging
- **Config-driven design** — all URLs, endpoints, and test data in YAML — no hardcoded values in tests
- **Shared fixtures** — pytest conftest pattern for session-scoped client and config reuse
- **Comprehensive assertions** — status codes, response schema, field values, and performance thresholds
- **Negative testing** — invalid credentials, missing fields, nonexistent resources
- **CI/CD integration** — GitHub Actions runs full suite on every push with HTML report artifact
- **Scheduled runs** — daily 8AM automated execution to catch API drift

---

## Test Coverage

| Suite | Tests | Coverage |
|---|---|---|
| GET /users | 7 tests | List, pagination, schema, single user, 404, response time |
| POST /users | 5 tests | Creation, ID assignment, field validation, timestamp |
| POST /login | 6 tests | Valid auth, token return, invalid credentials, missing fields |
| POST /register | 5 tests | Registration, token, ID, missing fields, unknown user |
| **Total** | **23 tests** | |

---

## Setup & Run

**1. Clone the repo**
```bash
git clone https://github.com/VivekanandUsingh/api-test-framework.git
cd api-test-framework
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run all tests**
```bash
pytest
```

**4. Run with HTML report**
```bash
pytest --html=reports/report.html --self-contained-html
```

**5. Run a specific suite**
```bash
pytest tests/test_users.py -v
pytest tests/test_auth.py -v
```

---

## CI/CD Pipeline

This framework runs automatically via GitHub Actions on:
- Every push to `main`
- Every pull request to `main`
- Daily at 8:00 AM UTC (scheduled run)

The pipeline installs dependencies, executes all 23 tests, and uploads an HTML report as a downloadable artifact.

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.11 | Core language |
| pytest | Test runner and assertion framework |
| requests | HTTP client library |
| PyYAML | Config management |
| pytest-html | HTML report generation |
| GitHub Actions | CI/CD automation |

---

## Author

**Vivekanand Singh** — QA Architect with 20 years across Web, Mobile, API, and Platform Migration  
[LinkedIn](https://www.linkedin.com/in/vivekanand09/) · [GitHub](https://github.com/VivekanandUsingh)
