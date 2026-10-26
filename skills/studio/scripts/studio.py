#!/usr/bin/env python3
"""Video studio helper. Two commands:

  python3 studio.py install
      Copies the studio page into the app made by `app create video-studio`
      and starts an empty project list. Run once, right after creating the app.

  python3 studio.py add --project "Video title" --video /path/to/edit.mp4 --label "First cut"
      Adds the video as the next version of that project (making the project
      if it's new), with a poster frame, and prints the version number.

The app lives at /agent/apps/video-studio unless --app-dir says otherwise.
"""
import argparse
import datetime
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEMPLATE = HERE.parent / "app"
DEFAULT_APP = Path("/agent/apps/video-studio")


def read_json(path, empty):
    return json.loads(path.read_text()) if path.exists() else empty


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n")


def slugify(title):
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return slug[:60] or "video"


def duration(video):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(video)],
        capture_output=True, text=True,
    )
    try:
        return round(float(out.stdout.strip()), 2)
    except ValueError:
        return None


def install(app):
    if not (app / "buildeth.app.json").exists():
        sys.exit(f"No app at {app}. Run: app create video-studio --icon film-slate --colors \"#111827,#9CA3AF\"")
    site = app / "site"
    for name in ("index.html", "app.js", "styles.css"):
        shutil.copyfile(TEMPLATE / name, site / name)
    projects = app / "data" / "projects.json"
    if not projects.exists():
        write_json(projects, {"projects": []})
    print(f"Installed the studio page in {site}")


def add(app, title, video, label):
    video = Path(video)
    if not video.exists():
        sys.exit(f"Video not found: {video}")
    data = app / "data"
    if not (data / "projects.json").exists():
        sys.exit("The studio isn't installed yet. Run: python3 studio.py install")

    index = read_json(data / "projects.json", {"projects": []})
    project = next((p for p in index["projects"] if p["title"] == title), None)
    if project is None:
        slug, n = slugify(title), 2
        taken = {p["slug"] for p in index["projects"]}
        while slug in taken:
            slug, n = f"{slugify(title)}-{n}", n + 1
        project = {"slug": slug, "title": title, "created": datetime.date.today().isoformat()}
        index["projects"].append(project)
        write_json(data / "projects.json", index)

    folder = data / "projects" / project["slug"]
    review = read_json(folder / "review.json", {"versions": []})
    v = max((x["v"] for x in review["versions"]), default=0) + 1
    out = folder / "review" / f"v{v}.mp4"
    out.parent.mkdir(parents=True, exist_ok=True)

    # Move the playback info to the front so the video starts playing before it fully loads.
    fast = subprocess.run(
        ["ffmpeg", "-y", "-v", "error", "-i", str(video), "-c", "copy", "-movflags", "+faststart", str(out)],
        capture_output=True,
    )
    if fast.returncode != 0:
        subprocess.run(
            ["ffmpeg", "-y", "-v", "error", "-i", str(video), "-c:v", "libx264", "-crf", "20",
             "-preset", "veryfast", "-c:a", "aac", "-movflags", "+faststart", str(out)],
            check=True,
        )

    dur = duration(out)
    at = min(1.0, (dur or 2) / 2)
    subprocess.run(
        ["ffmpeg", "-y", "-v", "error", "-ss", str(at), "-i", str(out), "-frames:v", "1",
         "-vf", "scale=540:-2", str(folder / "review" / f"v{v}.jpg")],
        check=True,
    )

    review["versions"].append({
        "v": v,
        "label": label or f"Version {v}",
        "date": datetime.date.today().isoformat(),
        "file": f"v{v}",
        "dur": dur,
    })
    write_json(folder / "review.json", review)
    print(json.dumps({"project": project["slug"], "version": v, "link": f"#/{project['slug']}?v={v}"}))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--app-dir", default=str(DEFAULT_APP))
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("install")
    a = sub.add_parser("add")
    a.add_argument("--project", required=True, help="The video's title, the same every time for the same video")
    a.add_argument("--video", required=True)
    a.add_argument("--label", default="", help="Short name for this version, like 'First cut'")
    args = ap.parse_args()
    app = Path(args.app_dir)
    if args.cmd == "install":
        install(app)
    else:
        add(app, args.project, args.video, args.label)


if __name__ == "__main__":
    main()
