**Acceptance criteria (from Ticket-1)**

- **AC1:** User can log in with a valid email and password
- **AC2:** After 5 failed attempts the account is locked for 15 minutes
- **AC3:** An error message is shown for invalid credentials, without revealing which field is wrong
- **AC4:** The "Remember me" checkbox keeps the user logged in for 30 days
- **AC5:** Password field masks input

**Test cases**

| ID | Title | Preconditions | Steps | Expected result | Type | Covers |
|---|---|---|---|---|---|---|
| TC-01 | Valid email and password log the user in | A registered account exists with a known email and password | 1) Open the login page. 2) Enter the registered email. 3) Enter the correct password. 4) Click "Log in". | User is logged in and redirected to their account page. | positive | AC1 |
| TC-02 | Valid credentials submitted with the Enter key | A registered account exists | 1) Open the login page. 2) Enter the registered email. 3) Enter the correct password. 4) Press Enter in the password field. | User is logged in and redirected to their account page. | positive | AC1 |
| TC-03 | Four failed attempts do not lock the account | A registered account exists and is not locked | 1) Submit a wrong password 4 times for the account. 2) Submit the correct password. | Login succeeds. The account is not locked. | boundary | AC2 |
| TC-04 | Fifth failed attempt locks the account | A registered account exists and is not locked | 1) Submit a wrong password 5 times for the account. 2) Submit the correct password immediately after. | After the 5th failure the account is locked. The correct-password attempt is rejected with a lock message. | boundary | AC2 |
| TC-05 | Account unlocks after 15 minutes | Account was locked by 5 failed attempts less than 15 minutes ago | 1) Wait until 15 minutes after the lock was applied. 2) Submit the correct password. | Login succeeds. The lock has expired. | boundary | AC2 |
| TC-06 | Wrong password shows a generic error | A registered account exists | 1) Enter the registered email. 2) Enter a wrong password. 3) Click "Log in". | An error message such as "Invalid email or password" is shown. The message does not say which field is wrong. | negative | AC3 |
| TC-07 | Unregistered email shows the same generic error | No account exists for the email used | 1) Enter an unregistered email. 2) Enter any password. 3) Click "Log in". | The same generic error message as for a wrong password is shown. It does not say that the email is unknown. | negative | AC3 |
| TC-08 | Error message is identical for wrong email and wrong password | Registered account exists | 1) Submit a registered email with a wrong password and note the message. 2) Submit an unregistered email with any password and note the message. | Both messages are identical in text and placement. | negative | AC3 |
| TC-09 | Remember me keeps the user logged in after browser restart | A registered account exists | 1) Log in with "Remember me" checked. 2) Close and reopen the browser within 30 days. 3) Open the account page. | User is still logged in without re-entering credentials. | positive | AC4 |
| TC-10 | Remember me session expires after 30 days | User logged in with "Remember me" checked, and 30 days have not yet passed | 1) Wait until 30 days after login (or set the clock to 30 days and 1 minute). 2) Open the account page. | User is logged out and asked to log in again. | boundary | AC4 |
| TC-11 | Without Remember me the session does not persist | A registered account exists | 1) Log in with "Remember me" unchecked. 2) Close and reopen the browser. 3) Open the account page. | User is not logged in and must log in again. | negative | AC4 |
| TC-12 | Password characters are masked while typing | Login page is open | 1) Click into the password field. 2) Type "Secret123". | Each typed character is shown as a dot or asterisk. The plain text is not visible. | positive | AC5 |
| TC-13 | Long password is fully masked | Login page is open | 1) Click into the password field. 2) Type a 128-character password. | All 128 characters are masked. No plain text is visible at any point. | boundary | AC5 |
| TC-14 | Empty email and password fields are rejected | Login page is open | 1) Leave email and password empty. 2) Click "Log in". | A validation message is shown for the empty fields. No login attempt is sent and no failed attempt is counted. | negative | extra |
| TC-15 | Leading and trailing spaces in email are trimmed | A registered account exists | 1) Enter the registered email with a space before and after it. 2) Enter the correct password. 3) Click "Log in". | Login succeeds, because the surrounding spaces are removed before the check. | boundary | extra |
| TC-16 | SQL injection string in email is rejected safely | Login page is open | 1) Enter `' OR '1'='1` in the email field. 2) Enter any password. 3) Click "Log in". | Login fails with the generic error. No database error or data leak is shown. | negative | extra |
| TC-17 | Successful login resets the failed attempt counter | A registered account exists with 4 failed attempts recorded | 1) Log in with the correct password. 2) Log out. 3) Submit a wrong password once. 4) Submit a wrong password 4 more times. | The account is locked only after the 5th failure counted since the successful login. Before that the account is not locked. | boundary | extra |