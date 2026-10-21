const spaces = await listTaskSpaces();
console.log(JSON.stringify(spaces.filter((s) => s.id >= 3), null, 1).slice(0, 1500));

const task = await taskSpace(4);
console.log("pages before:", (await task.pages()).map((p) => p.label));
console.log("tabs before:", (await task.tabs()).map((t) => ({ label: t.label ?? null, active: t.active, url: t.url })));

let page = await task.newPage();
console.log("created page:", page.label, "url:", await page.url());
await page.waitForTimeout(2000);
console.log("pages after:", (await task.pages()).map((p) => p.label));
console.log("tabs after:", (await task.tabs()).map((t) => ({ label: t.label ?? null, active: t.active, url: t.url })));
