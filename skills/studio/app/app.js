// Video studio: every edit version in one place, with timestamped notes to send back to Runneth.
// Data lives in ../data: projects.json lists projects; projects/<slug>/review.json lists versions,
// and each version's video and poster sit in projects/<slug>/review/v<N>.mp4 and v<N>.jpg.
// Notes and approvals are saved in this browser only, then copied back into the chat.

const url = (p) => new URL(`./data/${p}`, import.meta.url).href;
const getJSON = async (p) => { const r = await fetch(url(p), { cache: "no-store" }); return r.ok ? r.json() : null; };
const el = (tag, cls, text) => { const e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; };
const fmt = (s) => { const m = Math.floor(s / 60); return `${m}:${(s - m * 60).toFixed(1).padStart(4, "0")}`; };
const load = (k) => { try { return JSON.parse(localStorage.getItem(k) || "null"); } catch { return null; } };
const store = (k, v) => localStorage.setItem(k, JSON.stringify(v));
const button = (text, cls = "") => { const b = el("button", `btn ${cls}`.trim(), text); b.type = "button"; return b; };

const appEl = document.getElementById("app");
const projects = (await getJSON("projects.json"))?.projects || [];

async function copy(text, b) {
  try { await navigator.clipboard.writeText(text); const old = b.textContent; b.textContent = "Copied"; setTimeout(() => (b.textContent = old), 1500); }
  catch { window.prompt("Copy this and paste it into the chat:", text); }
}

async function route() {
  const [path, query] = location.hash.replace(/^#\/?/, "").split("?");
  appEl.replaceChildren();
  window.scrollTo(0, 0);
  const p = projects.find((x) => x.slug === path);
  if (!p) return renderHome();
  const data = await getJSON(`projects/${p.slug}/review.json`);
  return renderProject(p, data?.versions || [], Number(new URLSearchParams(query || "").get("v")));
}
window.addEventListener("hashchange", route);

function renderHome() {
  appEl.append(el("h1", "title", "Video studio"));
  if (!projects.length) { appEl.append(el("p", "empty", "No videos yet. Your first edit will show up here.")); return; }
  const grid = el("div", "projects");
  for (const p of [...projects].reverse()) {
    const a = el("a", "project"); a.href = `#/${p.slug}`;
    a.append(el("h2", "", p.title));
    if (p.created) a.append(el("p", "quiet", p.created));
    grid.append(a);
  }
  appEl.append(grid);
}

function renderProject(p, versions, wanted) {
  const back = el("a", "back", "← All videos"); back.href = "#/";
  appEl.append(back, el("h1", "title", p.title));
  if (!versions.length) { appEl.append(el("p", "empty", "No versions yet.")); return; }
  let ver = versions.find((x) => x.v === wanted) || versions[versions.length - 1];

  const picker = el("div", "versions");
  const holder = el("div");
  appEl.append(picker, holder);

  function drawPicker() {
    picker.replaceChildren();
    for (const x of versions) {
      const b = button(`V${x.v}${load(`studio:${p.slug}:approved:v${x.v}`) ? " ✓" : ""}`, x.v === ver.v ? "on" : "");
      b.title = x.label;
      b.onclick = () => { ver = x; drawPicker(); draw(); };
      picker.append(b);
    }
  }

  function draw() {
    const KEY = `studio:${p.slug}:notes:v${ver.v}`;
    let notes = load(KEY) || [];
    const save = () => store(KEY, notes);
    holder.replaceChildren();

    const card = el("section", "card");
    const head = el("div", "card-head");
    const left = el("div");
    left.append(el("p", "quiet", `Version ${ver.v}${ver.date ? " · " + ver.date : ""}`), el("h2", "", ver.label || `Version ${ver.v}`));
    const acts = el("div", "actions");
    const bCopy = button("Copy my notes", "primary");
    const bOk = button(load(`studio:${p.slug}:approved:v${ver.v}`) ? "Approved ✓" : "Approve this version");
    acts.append(bCopy, bOk);
    head.append(left, acts);

    const grid = el("div", "grid");
    const player = el("div", "player");
    const video = document.createElement("video");
    video.controls = true; video.playsInline = true; video.preload = "metadata";
    video.src = url(`projects/${p.slug}/review/${ver.file}.mp4`);
    video.poster = url(`projects/${p.slug}/review/${ver.file}.jpg`);
    const timeline = el("div", "timeline"); const playhead = el("div", "playhead"); timeline.append(playhead);
    const clock = el("p", "quiet clock", `0:00.0 / ${fmt(ver.dur || 0)}`);
    player.append(video, timeline, clock);

    const dur = () => video.duration || ver.dur || 1;
    timeline.addEventListener("click", (e) => {
      if (e.target.classList.contains("dot")) return;
      const r = timeline.getBoundingClientRect();
      video.currentTime = Math.max(0, Math.min(1, (e.clientX - r.left) / r.width)) * dur();
    });
    video.addEventListener("timeupdate", () => {
      clock.textContent = `${fmt(video.currentTime)} / ${fmt(dur())}`;
      playhead.style.left = `${(video.currentTime / dur()) * 100}%`;
    });

    const panel = el("div", "panel");
    let at = null, whole = false;
    const where = el("p", "where", "Pause where you want to leave a note");
    const bWhole = button("Note on the whole video");
    const box = document.createElement("textarea"); box.placeholder = "What should change here?";
    const bSave = button("Save note", "primary");
    const list = el("div", "notes");
    panel.append(el("h3", "", "Leave a note"), where, bWhole, box, bSave, el("h3", "", "Your notes"), list);
    grid.append(player, panel);
    card.append(head, grid);
    holder.append(card);

    const showWhere = () => {
      where.textContent = whole ? "On the whole video" : at == null ? "Pause where you want to leave a note" : `At ${fmt(at)}`;
      bWhole.textContent = whole ? "Note at a moment instead" : "Note on the whole video";
    };
    const grab = () => { if (!whole) { at = +video.currentTime.toFixed(1); showWhere(); } };
    video.addEventListener("pause", grab);
    box.addEventListener("focus", () => { video.pause(); grab(); });
    bWhole.onclick = () => { whole = !whole; if (!whole) grab(); showWhere(); };
    bSave.onclick = () => {
      const text = box.value.trim(); if (!text) { box.focus(); return; }
      notes.push({ t: whole ? null : (at ?? +video.currentTime.toFixed(1)), note: text });
      notes.sort((a, b) => (a.t ?? -1) - (b.t ?? -1));
      box.value = ""; whole = false; save(); drawNotes(); showWhere();
    };

    function drawNotes() {
      timeline.querySelectorAll(".dot").forEach((d) => d.remove());
      list.replaceChildren();
      if (!notes.length) list.append(el("p", "empty", "No notes yet."));
      notes.forEach((n, i) => {
        if (n.t != null) {
          const d = el("div", "dot"); d.style.left = `${(n.t / dur()) * 100}%`; d.title = n.note;
          d.onclick = () => { video.currentTime = n.t; }; timeline.append(d);
        }
        const row = el("div", "note");
        const body = el("div");
        body.append(el("p", "quiet", n.t == null ? "Whole video" : fmt(n.t)), el("p", "", n.note));
        if (n.t != null) body.firstChild.onclick = () => { video.currentTime = Math.max(0, n.t - 1); video.play(); };
        const del = button("Delete", "small"); del.onclick = () => { notes.splice(i, 1); save(); drawNotes(); };
        row.append(body, del);
        list.append(row);
      });
    }
    drawNotes(); showWhere();

    bCopy.onclick = () => {
      const lines = notes.map((n) => `- ${n.t == null ? "Whole video" : fmt(n.t)}: ${n.note}`);
      copy([`Notes on "${p.title}", version ${ver.v}:`, ...(lines.length ? lines : ["- No notes"])].join("\n"), bCopy);
    };
    bOk.onclick = () => {
      store(`studio:${p.slug}:approved:v${ver.v}`, true);
      copy(`Approved "${p.title}", version ${ver.v}.`, bOk);
      drawPicker(); bOk.textContent = "Approved ✓";
    };
  }

  drawPicker();
  draw();
}

route();
