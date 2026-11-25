**Acceptance criteria (Ticket-1: Login with email and password)**

- **AC1:** User can log in with a valid email and password
- **AC2:** After 5 failed attempts the account is locked for 15 minutes
- **AC3:** An error message is shown for invalid credentials, without revealing which field is wrong
- **AC4:** The "Remember me" checkbox keeps the user logged in for 30 days
- **AC5:** Password field masks input

**Test cases**

| ID | Title | Preconditions | Steps | Expected result | Type | Covers |
|----|-------|---------------|-------|-----------------|------|--------|
| TC-01 | Valid credentials log the user in | A registered account exists with a known email and password; user is logged out | 1. Open the login page. 2. Enter the registered email. 3. Enter the correct password. 4. Click "Log in". | User is logged in and redirected to their account page. | positive | AC1 |
| TC-02 | Login succeeds with a valid email at maximum allowed length | An account exists whose email is at the maximum length the system accepts (254 characters) | 1. Open the login page. 2. Enter the long registered email. 3. Enter the correct password. 4. Click "Log in". | User is logged in successfully. | boundary | AC1 |
| TC-03 | Four failed attempts do not lock the account | A registered account exists; user is logged out; no prior failed attempts | 1. Enter the registered email with a wrong password and submit. 2. Repeat 3 more times (4 failures in total). 3. Enter the correct password and submit. | Login succeeds; the account is not locked. | boundary | AC2 |
| TC-04 | Fifth failed attempt locks the account | A registered account exists; user is logged out; no prior failed attempts | 1. Enter the registered email with a wrong password and submit 5 times. 2. Enter the correct password and submit. | After the 5th failure the account is locked; the correct-password attempt is rejected and a lock message is shown. | negative | AC2 |
| TC-05 | Account unlocks after 15 minutes | Account was locked by 5 failed attempts at time T | 1. Wait until T + 15 minutes. 2. Enter the correct password and submit. | Login succeeds and the lock has expired. | boundary | AC2 |
| TC-06 | Wrong password shows a generic error | A registered account exists; user is logged out | 1. Enter the registered email. 2. Enter a wrong password. 3. Click "Log in". | An error such as "Invalid email or password" is shown; the message does not say which field is wrong. | negative | AC3 |
| TC-07 | Unknown email shows the same generic error | No account exists for the email used | 1. Enter an unregistered email. 2. Enter any password. 3. Click "Log in". | The same generic error as TC-06 is shown; the message does not reveal whether the email exists. | negative | AC3 |
| TC-08 | Remember me keeps the user logged in after closing the browser | A registered account exists; user is logged out | 1. Log in with valid credentials and tick "Remember me". 2. Close the browser. 3. Reopen the application after 1 day. | User is still logged in without re-entering credentials. | positive | AC4 |
| TC-09 | Remember me session expires after 30 days | User logged in with "Remember me" ticked, at time T | 1. Reopen the application at T + 29 days. 2. Reopen at T + 31 days. | At T + 29 days the user is still logged in; at T + 31 days the user is logged out and must log in again. | boundary | AC4 |
| TC-10 | Without "Remember me" the session does not persist | A registered account exists; user is logged out | 1. Log in with valid credentials, leaving "Remember me" unticked. 2. Close the browser. 3. Reopen the application. | User is logged out and must log in again. | negative | AC4 |
| TC-11 | Password characters are masked while typing | User is on the login page | 1. Click into the password field. 2. Type "Secret123". | Each character is displayed as a mask (dots or asterisks), not as plain text. The input element is of type password. | positive | AC5 |
| TC-12 | Pasted password is masked too | User is on the login page; a password string is in the clipboard | 1. Click into the password field. 2. Paste a password of 128 characters. | The entire pasted value is shown as masked characters, with no plain-text characters visible. | boundary | AC5 |

**Extra test cases (not covered by the ticket)**

| ID | Title | Preconditions | Steps | Expected result | Type | Covers |
|----|-------|---------------|-------|-----------------|------|--------|
| TC-13 | Submitting the form with empty fields shows validation | User is on the login page | 1. Leave email and password empty. 2. Click "Log in". | Validation messages are shown for the empty fields; no login request succeeds. | negative | extra |
| TC-14 | SQL injection string in email field is rejected safely | User is on the login page | 1. Enter `' OR '1'='1` as the email. 2. Enter any password. 3. Click "Log in". | Login is rejected with the generic error; no account is accessed and no server error is shown. | negative | extra |
| TC-15 | Successful login resets the failed-attempt counter | A registered account exists; user is logged out | 1. Submit 4 wrong passwords. 2. Submit the correct password (login succeeds). 3. Log out. 4. Submit 4 wrong passwords. 5. Submit the correct password. | Login succeeds at step 5; the account is not locked, because the counter was reset at step 2. | boundary | extra |
| TC-16 | Email is matched case-insensitively | A registered account exists with email in lowercase | 1. Enter the email in mixed case (e.g., "User@Example.com"). 2. Enter the correct password. 3. Click "Log in". | User is logged in to the same account. | positive | extra |