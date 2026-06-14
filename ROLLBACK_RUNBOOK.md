# Rollback Runbook 
 
## When to Rollback 
- [ ] Health check failing ( errors) 
- [ ] Critical user journey broken 
- [ ] Security vulnerability detected 
- [ ] Database corruption or data loss 
 
## Rollback Procedure 
 
### 1. Identify Target Version 
```bash 
git tag -l "v*"  # List all versions 
``` 
 
### 2. Execute Rollback 
- Go to GitHub Actions  Rollback workflow 
- Enter target version (e.g., v1.0.0-working) 
- Enter reason for rollback 
- Click "Run workflow" 
 
### 3. Verify Recovery 
```bash 
curl https://your-app.com/health 
``` 
 
### 4. Post-Rollback Actions 
- Investigate root cause 
- Write post-mortem 
- Add test to prevent recurrence 
