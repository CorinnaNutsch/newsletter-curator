# Setup: IMAP access to the newsletter mailbox

The app reads newsletters from a dedicated Gmail account over IMAP with an app password (decision in [design.md](design.md) section 12). The ingest code sits behind an adapter, so the Gmail API can replace it later.

Credentials live in environment variables, never in code or in git. `.env` is gitignored, `.env.example` is committed with empty values.

## Steps

1. **Sign in from a trusted browser or device.** Use the browser (or the phone with the Gmail app) where this account was signed in before, on your usual network, without a VPN. A private window or a new browser profile can trigger Google's identity check (see Troubleshooting).
2. **Turn on 2-Step Verification.** myaccount.google.com → Security → 2-Step Verification. Google asks for a phone number.
3. **Create an app password.** Open myaccount.google.com/apppasswords (it only appears once 2-Step Verification is on). Name it `newsletter-curator`. Google shows a 16-character password once; copy it straight into step 5.
4. **Check that IMAP is enabled.** Gmail → gear icon → See all settings → Forwarding and POP/IMAP. If there is an "IMAP access" switch, enable it and save. If there is none, IMAP is already on.
5. **Put the credentials in `.env`** (from the repo root):
   ```
   cp .env.example .env
   ```
   Fill in `IMAP_USER` (the Gmail address) and `IMAP_PASSWORD` (the 16 characters, no spaces). Never commit `.env`.
6. **Test the connection.** This is a throwaway check, not the adapter. It opens the inbox read-only, so nothing is marked as read:
   ```
   set -a; source .env; set +a
   python3 -c "import imaplib,os; m=imaplib.IMAP4_SSL(os.environ['IMAP_HOST']); m.login(os.environ['IMAP_USER'], os.environ['IMAP_PASSWORD']); print(m.select('INBOX', readonly=True)); m.logout()"
   ```
   Success prints `('OK', [b'<number of messages>'])`. Do not paste the password anywhere when asking for help.

## Troubleshooting

| Symptom | Likely cause and fix |
|---|---|
| Google asks to verify your identity ("Wir möchten Ihre Identität überprüfen") | The browser or device looks new, or the network is unknown. Retry once from the browser or phone where you were signed in before, on a known network, no VPN. Do not retry many times in a row, repeated attempts can extend the block. If it persists, wait a day. |
| `AUTHENTICATIONFAILED` | Typo, or the account password was used instead of the app password. Revoke the app password on the same page and create a new one. |
| "Application-specific password required" | 2-Step Verification is not on yet. |
| No app password page | 2-Step Verification is off, or the account is under a Workspace or Advanced Protection policy. |

## Notes
- An app password gives access to the whole mailbox. This is acceptable because the account holds only newsletters. Revoke it any time on the app passwords page.
- The adapter should open mailboxes with `readonly=True`, so ingesting does not change read or starred flags (those flags are implicit feedback, see design.md section 8).
- The `newsletters` label appears in IMAP as a folder named `newsletters`; the adapter can read just that folder.
- The parser and the gold sets do not need IMAP. Only the ingest adapter does.
