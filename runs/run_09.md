**Acceptance criteria (from Ticket-1):**

- **AC1:** User can log in with a valid email and password
- **AC2:** After 5 failed attempts the account is locked for 15 minutes
- **AC3:** An error message is shown for invalid credentials, without revealing which field is wrong
- **AC4:** The "Remember me" checkbox keeps the user logged in for 30 days
- **AC5:** Password field masks input

**Test cases:**

| ID | Title | Preconditions | Steps | Expected result | Type | Covers |
|---|---|---|---|---|---|---|
| TC-01 | Log in with valid email and password | A registered user account exists and is not locked | 1. Open the login page. 2. Enter the registered email. 3. Enter the correct password. 4. Click "Log in". | User is logged in and redirected to their account page. | positive | AC1 |
| TC-02 | Password with wrong letter case is rejected | A registered user account exists and is not locked | 1. Open the login page. 2. Enter the registered email. 3. Enter the correct password with one letter's case changed. 4. Click "Log in". | Login fails and the invalid-credentials error is shown. User is not logged in. | negative | AC1 |
| TC-03 | Account locks on the 5th consecutive failed attempt | A registered user account exists and is not locked | 1. Enter the registered email and a wrong password, then submit. 2. Repeat step 1 four more times (5 total). 3. Attempt to log in with the correct password. | After the 5th failure the account is locked. The login with the correct password is rejected. | boundary | AC2 |
| TC-04 | Four failed attempts do not lock the account | A registered user account exists and is not locked | 1. Enter the registered email and a wrong password, then submit. 2. Repeat step 1 three more times (4 total). 3. Log in with the correct password. | Login succeeds. The account is not locked. | boundary | AC2 |
| TC-05 | Locked account stays locked for 15 minutes | Account was locked by 5 failed attempts less than 15 minutes ago | 1. Attempt to log in with the correct password at 14 minutes after the lock. | Login is rejected and a lock message is shown. | negative | AC2 |
| TC-06 | Account unlocks after 15 minutes | Account was locked by 5 failed attempts exactly 15 minutes ago | 1. Attempt to log in with the correct password at 15 minutes after the lock. | Login succeeds. | positive | AC2 |
| TC-07 | Wrong password shows generic error | A registered user account exists and is not locked | 1. Enter the registered email and a wrong password. 2. Click "Log in". | Error message is shown, for example "Invalid email or password". The message does not say which field is wrong. | negative | AC3 |
| TC-08 | Unregistered email shows the same generic error | No account exists for the email used | 1. Enter an unregistered email and any password. 2. Click "Log in". | The same generic error as TC-07 is shown. The message does not reveal whether the email exists. | negative | AC3 |
| TC-09 | Remember me keeps user logged in for 30 days | A registered user account exists and is not locked | 1. Log in with valid credentials and check "Remember me". 2. Close the browser. 3. Reopen the browser and go to the app after 29 days. | User is still logged in without re-entering credentials. | positive | AC4 |
| TC-10 | Remember me session expires after 30 days | Login was made with "Remember me" checked | 1. Go to the app at 30 days after login, with no new login. | User is logged out and must log in again. | boundary | AC4 |
| TC-11 | Without "Remember me" the session is not kept | A registered user account exists and is not locked | 1. Log in with valid credentials and leave "Remember me" unchecked. 2. Close the browser. 3. Reopen the browser and go to the app. | User is logged out and must log in again. | negative | AC4 |
| TC-12 | Password is masked while typing | Login page is open | 1. Click in the password field. 2. Type "Secret123". | Each typed character is shown as a mask symbol (for example dots), not as plain text. | positive | AC5 |
| TC-13 | Pasted password is masked | Login page is open and a password is copied to the clipboard | 1. Click in the password field. 2. Paste the password. | The pasted text is shown as mask symbols, not as plain text. | boundary | AC5 |
| TC-14 | Leading and trailing spaces in email are trimmed | A registered user account exists and is not locked | 1. Enter the registered email with a space before and after it. 2. Enter the correct password. 3. Click "Log in". | Login succeeds, because spaces are trimmed from the email. | boundary | extra |
| TC-15 | Empty email and password are rejected before submit | Login page is open | 1. Leave both fields empty. 2. Click "Log in". | Validation messages are shown for both fields. No login request is sent. | negative | extra |
| TC-16 | Password of maximum allowed length is accepted | A registered user account exists with a password at the maximum length the system allows (for example 128 characters) | 1. Enter the email. 2. Enter the full-length correct password. 3. Click "Log in". | Login succeeds. | boundary | extra |
| TC-17 | Failed-attempt counter resets after a successful login | A registered user account exists and is not locked | 1. Enter a wrong password 4 times. 2. Log in with the correct password. 3. Enter a wrong password 4 more times. 4. Log in with the correct password. | Account is not locked at any point. Both successful logins succeed. | extra |
| TC-18 | SQL injection text in email is rejected safely | Login page is open | 1. Enter `' OR '1'='1` in the email field. 2. Enter any password. 3. Click "Log in". | Login fails with the generic error. No login is granted and no server error is shown. | negative | extra |