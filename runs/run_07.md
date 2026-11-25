**Acceptance criteria (from Ticket-1):**

- **AC1:** User can log in with a valid email and password
- **AC2:** After 5 failed attempts the account is locked for 15 minutes
- **AC3:** An error message is shown for invalid credentials, without revealing which field is wrong
- **AC4:** The "Remember me" checkbox keeps the user logged in for 30 days
- **AC5:** Password field masks input

**Test cases:**

| ID | Title | Preconditions | Steps | Expected result | Type | Covers |
|---|---|---|---|---|---|---|
| TC-01 | Log in with valid email and password | Registered user exists, not locked | 1. Open login page. 2. Enter the registered email and correct password. 3. Click "Log in". | User is logged in and redirected to the account page. | positive | AC1 |
| TC-02 | Password differing only in case is rejected | Registered user exists, not locked | 1. Open login page. 2. Enter the registered email and the correct password with one letter's case changed. 3. Click "Log in". | Login fails; user stays on the login page with an error message. | negative | AC1 |
| TC-03 | Four failed attempts do not lock the account | Registered user exists, not locked | 1. Enter the registered email and a wrong password, and submit, four times. 2. Enter the correct password and submit. | Login succeeds; the account is not locked. | boundary | AC2 |
| TC-04 | Fifth failed attempt locks the account | Registered user exists, not locked | 1. Enter the registered email and a wrong password, and submit, five times. 2. Enter the correct password and submit. | After the fifth failure the account is locked; the correct password is rejected with a lock message. | negative | AC2 |
| TC-05 | Account is still locked at 14 minutes | Account locked by five failed attempts at time T | 1. At T + 14 min, enter the correct password and submit. | Login is rejected; account remains locked. | boundary | AC2 |
| TC-06 | Account unlocks after 15 minutes | Account locked by five failed attempts at time T | 1. At T + 15 min, enter the correct password and submit. | Login succeeds; the lock has expired. | boundary | AC2 |
| TC-07 | Wrong password shows generic error | Registered user exists, not locked | 1. Enter the registered email and a wrong password. 2. Click "Log in". | Error message such as "Invalid email or password" is shown. It does not say which field is wrong. | negative | AC3 |
| TC-08 | Unknown email shows the same generic error | No account exists for the email used | 1. Enter an unregistered email and any password. 2. Click "Log in". | Same generic error message as TC-07 is shown, with no hint that the email is unknown. | negative | AC3 |
| TC-09 | Remember me keeps user logged in for 30 days | Registered user exists, not locked | 1. Log in with valid credentials and check "Remember me". 2. Close and reopen the browser after one day. 3. Open the account page. | User is still logged in. | positive | AC4 |
| TC-10 | Without Remember me the session does not persist | Registered user exists, not locked | 1. Log in with valid credentials, leaving "Remember me" unchecked. 2. Close and reopen the browser. 3. Open the account page. | User is logged out and asked to log in again. | negative | AC4 |
| TC-11 | Remember me session still valid at 30 days | Logged in with "Remember me" checked at time T | 1. At T + 30 days minus 1 hour, open the account page. | User is still logged in. | boundary | AC4 |
| TC-12 | Remember me session expires after 30 days | Logged in with "Remember me" checked at time T | 1. At T + 30 days plus 1 minute, open the account page. | User is logged out and redirected to the login page. | boundary | AC4 |
| TC-13 | Password is masked while typing | Login page open | 1. Click the password field. 2. Type a password. | Characters appear as masked dots or asterisks, not plain text. | positive | AC5 |
| TC-14 | Password is not shown in plain text after a failed login | Login page open | 1. Enter a password and submit with a wrong value. 2. Inspect the password field after the error appears. | The password field still masks the value and the password is not displayed as plain text. | negative | AC5 |
| TC-15 | Submitting empty email and password | Login page open | 1. Leave email and password empty. 2. Click "Log in". | Validation messages are shown; no login request succeeds. | negative | extra |
| TC-16 | Email at maximum allowed length (254 characters) | Registered user with a 254-character email exists | 1. Enter the 254-character email and correct password. 2. Click "Log in". | Login succeeds. | boundary | extra |
| TC-17 | SQL injection string in email field is rejected | Login page open | 1. Enter `' OR '1'='1` as email and any password. 2. Click "Log in". | Login fails with the generic error; no data is exposed and no server error is shown. | negative | extra |
| TC-18 | Failed-attempt counter resets after successful login | Registered user exists, not locked | 1. Submit four wrong passwords. 2. Log in with the correct password. 3. Log out. 4. Submit four more wrong passwords. | Account is not locked after the second set of four failures. | boundary | extra |