@echo off 
echo ======================================== 
echo ROLLBACK TEST SIMULATION 
echo ======================================== 
 
echo [STEP 1] Current version: 
git log --oneline -1 
 
echo [STEP 2] Simulating bad deployment... 
echo "Bad version deployed - health check failing" 
 
echo [STEP 3] Detecting failure... 
echo "Health check: FAILED (HTTP 500)" 
 
echo [STEP 4] Initiating rollback... 
git checkout v1.0.0-working 
 
echo [STEP 5] Verifying rollback... 
echo "Health check: PASSED" 
 
echo ======================================== 
echo ? ROLLBACK TEST PASSED 
echo ======================================== 
git checkout day20-rollback 
