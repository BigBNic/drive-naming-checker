# Setup: Making the Checker Live

Three pieces. Code is done. These are the remaining steps.

## 1. Google Drive API service account

- Create a service account in Google Cloud Console
- Enable the Drive API
- Download the JSON key
- Share the target Drive folders with the service account email (edit access)
- Set up a push notification channel (webhook) on folder create events
  - `files.watch` with `pageToken` polling as fallback
- Point the webhook at the hosted checker endpoint

## 2. Always-on host

- Nicholas's cloud box (already running Grok Bots) or a $5/month VPS
- Run: `python checker.py <filename>` as a pre-save gate
- Or expose an HTTP endpoint: `POST /check {"filename": "..."}`

## 3. Bot-side wiring

- Every bot (DOCU-Bot, Chief of Staff, Steward, etc.) calls the checker
  BEFORE saving any file
- On BLOCK: bot reports one line with the blocker and does not save
- On PASS: save proceeds normally

## Test without any of the above

```bash
python checker.py 2026-11-01_hairflip_deck.pptx   # should PASS
python checker.py t01.png                          # should BLOCK
python test_checker.py                             # full suite
```

## Cost to run

- Free if hosted on Nicholas's existing cloud box
- ~$5/month VPS otherwise
- Zero per-check cost
