const task = await taskSpace(4);
const page = task.page("p1");

const rows = await page.evaluate(() => {
  const out = [];
  const nodes = [...document.querySelectorAll("div,span,p")];
  for (const el of nodes) {
    const t = (el.textContent || "").trim();
    if (/^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$/.test(t) && el.children.length === 0) {
      let card = el;
      for (let i = 0; i < 5 && card.parentElement; i++) card = card.parentElement;
      const lines = (card.innerText || "").split("\n").map((s) => s.trim()).filter(Boolean);
      out.push({ date: t, text: lines.slice(0, 6) });
    }
  }
  return out.slice(0, 15);
});
console.log(JSON.stringify(rows, null, 1).slice(0, 5000));
