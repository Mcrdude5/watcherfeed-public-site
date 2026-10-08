# The Watcher Feed Public Site

Public marketing/legal site for TikTok developer review, hosted at:
https://mcrdude5.github.io/watcherfeed-public-site/

## Brand consistency for TikTok review

- The official WatcherFeed app logo is used on the home page, in every page header, and as the browser favicon.
- Home/header: `assets/watcherfeed-crest.webp` (optimized from the original official WatcherFeed crest).
- Browser favicon: `assets/watcherfeed-favicon.png` (rendered from the same original crest).
- The TikTok Developer Portal app icon must continue to use the same original crest.
- Do not reinstate the old generic "WF" home-page placeholder.
- GitHub Pages publication must complete **before** requesting TikTok re-review.
- After publication, check with an incognito window and refresh the browser favicon cache; compare the homepage and favicon against TikTok Basic Info.
- The approved icon's original 1024+px source is kept outside the public repository; do not upload TikTok client secrets, OAuth tokens, or production data here.

## Review process

For the rejection dated October 7, 2026, TikTok's reviewer specifically requested that the **App icon** in Basic Info match the app icon used on the website and browser tab (favicon). The public-site update addresses the site's side. The application owner must confirm the production **App icon** still matches and then select **Return to Draft**, resubmit the updated production review, and await TikTok's decision. Merely changing GitHub Pages cannot change a rejected TikTok review.

The public site describes a draft-first creator-controlled workflow. This repository does not enable TikTok Direct Post or WatcherFeed public autopublishing.

## Preflight

Run `python scripts/verify_brand_consistency.py` from the repo root to check all five pages, brand asset links, and the absence of the old placeholder.

Support contact: watcher@godschoice.net

This repository contains only public website content. WatcherFeed production source, credentials, tokens, media, and private runtime telemetry do not belong here.
