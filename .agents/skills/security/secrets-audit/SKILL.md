---
name: secrets-audit
description: Scans source code, configuration files, and git commits to detect hardcoded secrets, database credentials, API keys, and sensitive data leaking into application logs.
---

# Secrets & Sensitive Data Audit Skill

## 1. When to Use
- Before completing any task that modifies configuration files, database connections, or authentication providers.
- When performing a security review or audit of a newly onboarded repository.
- When writing logging statements around user requests or third-party API calls.

## 2. When NOT to Use
- When reviewing non-credential configuration values (e.g. logging levels, pagination limits).

## 3. Core Audit Rules

### A. Zero Hardcoded Credentials
- Scan source files and `appsettings.json` / `web.config` for:
  - Raw passwords (`Password=...;`, `pwd=...;`)
  - API keys (`AIzaSy...`, `sk_live_...`, `AKIA...`)
  - Private certificates / PEM keys
  - Plaintext symmetric JWT keys in source (`"super-secret-key-12345"`)
- Ensure secrets are loaded via:
  - User Secrets in development (`dotnet user-secrets`)
  - Environment variables (`ASPNETCORE_*`)
  - Azure Key Vault, AWS Secrets Manager, or HashiCorp Vault in production.

### B. Sensitive Logging Prevention
- Never log passwords, tokens, full credit card numbers, or personally identifiable information (PII).
- For HTTP request logging, mask the `Authorization` header and request bodies for login endpoints.

## 4. Anti-Patterns
- **Committing Secrets to Git**: Storing real production connection strings inside `appsettings.Production.json` checked into source control.
- **Logging Exceptions with Credentials**: Logging raw exception messages that include the complete connection string with password.

## 5. Verification Checklist
- [ ] No hardcoded passwords or API keys in source code.
- [ ] Configuration uses placeholders (`<SET_IN_ENVIRONMENT>`) in tracked files.
- [ ] Logs do not record credentials, auth headers, or PII.
