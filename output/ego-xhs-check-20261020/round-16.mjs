const task = await taskSpace(4);
const page = task.page("p1");

const rows = await page.evaluate(() => {
  const out = [];
  const nodes = [...document.querySelectorAll("div,span,p")];
  for (const el of nodes) {
    const t = (el.textContent || "").trim();
    if (!/^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$/.test(t) || el.children.length > 0) continue;
    let card = el.parentElement;
    let best = null;
    for (let i = 0; i < 6 && card; i++) {
      const lines = (card.innerText || "").split("\n").map((s) => s.trim()).filter(Boolean);
      if (lines.length >= 2 && lines.length <= 8) {
        best = { date: t, lines };
        break;
      }
      card = card.parentElement;
    }
    if (best) out.push(best);
  }
  return out.slice(0, 12);
});
console.log(JSON.stringify(rows, null, 1).slice(0, 5000));
