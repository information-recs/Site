# Information

Static site for Information. Plain HTML, CSS and JavaScript with no build step.

## Put it online with GitHub Pages (free)

1. Create a new **public** repository on GitHub.
2. Upload everything in this folder to the repository's root (drag and drop works in the browser). Keep the folder structure.
3. In the repository go to **Settings, Pages**. Under "Build and deployment" choose **Deploy from a branch**, pick `main` and `/ (root)`, and save.
4. After a minute the site is live at `https://YOUR-USERNAME.github.io/REPO-NAME/` (or `https://YOUR-USERNAME.github.io/` if the repo is named `YOUR-USERNAME.github.io`).

Optional: add a custom domain under Settings, Pages. HTTPS is free.

After you know the final address, open `index.html` and change `content="og-image.jpg"` to the full URL of that image so link previews (iMessage, Instagram, Slack) show it.

## Update the site

- **Text, email, Instagram, SoundCloud link:** edit the `CONFIG` block near the bottom of `index.html`.
- **Events:** edit `events.json` (one entry per event, dates as `YYYY-MM-DD`). Events dated today or later appear under Upcoming, the rest move to Archive on their own.
- **Flyers:** run `python3 tools/download-flyers.py` on your computer. It saves each flyer into `flyers/` as a small image and updates `events.json`. Commit the result. Until you do, flyers load straight from Resident Advisor.
- Changes can take a few minutes to appear after you commit.

## Files

| File | What it is |
| --- | --- |
| `index.html` | the whole site |
| `events.json` | event list |
| `logo-spin.webp` | the animated logo |
| `about-clip.gif` | the clip in the About section |
| `flyers/` | event flyers (filled by the script) |
| `favicon.png`, `apple-touch-icon.png`, `og-image.jpg` | browser tab icon, home-screen icon, link preview image |
| `.nojekyll` | tells GitHub Pages to serve the files as they are |
