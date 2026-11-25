**Acceptance criteria (from Ticket-1)**

- **AC1:** User can log in with a valid email and password
- **AC2:** After 5 failed attempts the account is locked for 15 minutes
- **AC3:** An error message is shown for invalid credentials, without revealing which field is wrong
- **AC4:** The "Remember me" checkbox keeps the user logged in for 30 days
- **AC5:** Password field masks input

**Test cases**

| ID | Title | Preconditions | Steps | Expected result | Type | Covers |
|---|---|---|---|---|---|---|
| TC-01 | Valid email and password log the user in | Registered account exists; user is logged out | 1. Open login page. 2. Enter valid email and correct password. 3. Click Log in. | User is logged in and redirected to the account page | positive | AC1 |
| TC-02 | Shortest valid email address logs in | Account registered with email a@b.co and a known password | 1. Open login page. 2. Enter a@b.co and correct password. 3. Click Log in. | Login succeeds | boundary | AC1 |
| TC-03 | Four failed attempts do not lock the account | Registered account is not locked | 1. Enter correct email with wrong password four times. 2. Enter correct password. | Login succeeds; no lock message is shown | boundary | AC2 |
| TC-04 | Fifth failed attempt locks the account for 15 minutes | Registered account is not locked | 1. Enter correct email with wrong password five times. 2. Immediately enter correct password. | Login is rejected with a lock message; account stays locked for 15 minutes | negative | AC2 |
| TC-05 | Login succeeds once the 15-minute lock expires | Account locked by five failed attempts at time T | 1. Wait until T+15 minutes (or advance the test clock). 2. Enter correct credentials. | Login succeeds | boundary | AC2 |
| TC-06 | Account is still locked at 14 minutes 59 seconds | Account locked by five failed attempts at time T | 1. At T+14:59, enter correct credentials. | Login is rejected; account remains locked | boundary | AC2 |
| TC-07 | Wrong password shows generic error | Registered account exists | 1. Enter valid email with wrong password. 2. Submit. | Message "Invalid email or password" is shown; no field is singled out | negative | AC3 |
| TC-08 | Unregistered email shows the same generic error | No account exists for the email | 1. Enter unregistered email with any password. 2. Submit. | Same generic message as TC-07 is shown; no field is singled out | negative | AC3 |
| TC-09 | Remember me keeps the user logged in after browser restart | Registered account exists; user is logged out | 1. Check "Remember me". 2. Log in. 3. Close and reopen the browser. 4. Open the account page. | User is still logged in | positive | AC4 |
| TC-10 | Remember me session is still valid at 29 days 23 hours | Logged in with "Remember me" checked at time T | 1. At T+29d 23h, open the account page. | User is still logged in | boundary | AC4 |
| TC-11 | Remember me session expires after 30 days | Logged in with "Remember me" checked at time T | 1. At T+30d 1min, open the account page. | User is logged out and redirected to the login page | boundary | AC4 |
| TC-12 | Session does not persist after restart without Remember me | Registered account exists; user is logged out | 1. Leave "Remember me" unchecked. 2. Log in. 3. Close and reopen the browser. | User is logged out | negative | AC4 |
| TC-13 | Typed password characters are masked | User is on the login page | 1. Click the password field. 2. Type "Secret123". | Each character is shown as a mask symbol, not as plain text | positive | AC5 |
| TC-14 | Very long password is masked | User is on the login page | 1. Type a 128-character password into the password field. | All characters are masked | boundary | AC5 |
| TC-15 | Empty email and password are rejected | User is on the login page | 1. Leave both fields empty. 2. Click Log in. | Validation error is shown; no login attempt is made | negative | extra |
| TC-16 | Email with leading and trailing spaces | Registered account with email user@example.com | 1. Enter " user@example.com " (with spaces) and correct password. 2. Click Log in. | Login succeeds with the email trimmed | boundary | extra |
| TC-17 | SQL injection string in email field | User is on the login page | 1. Enter `' OR '1'='1` as email and any password. 2. Submit. | Login is rejected with the generic error; no data is exposed | negative | extra |
| TC-18 | Failed-attempt counter resets after a successful login | Registered account exists; not locked | 1. Enter wrong password four times. 2. Log in with correct password. 3. Enter wrong password four more times. | Account is not locked after the second set of failures | boundary | extra |

**Notes**
- TC-05, TC-06, and TC-10 to TC-11 depend on time. Use a controllable clock rather than waiting in real time.
- The ticket does not define behavior for TC-15 to TC-18, so their expected results are proposed defaults. Confirm them with the product owner.