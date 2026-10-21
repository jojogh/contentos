const s = await newTaskSpace("ego-xhs-p14-verify", "Profile 14");
console.log({ id: s.id, profileId: s.profileId, profileName: s.profileName });

const task = await taskSpace(s.id);
let page;
try {
  page = task.page("p1");
} catch {
  const tabs = await task.tabs();
  const active = tabs.find((t) => t.active) || tabs[0];
  if (!active) throw new Error("no tabs in new space");
  page = active.label ? task.page(active.label) : await task.adopt(active.page);
}
console.log({ page: page.label });

await page.goto("https://creator.xiaohongshu.com/publish/publish?source=official");
await page.waitForTimeout(5000);
console.log({ url: await page.url(), title: await page.title() });
console.log((await page.snapshot()).slice(0, 2500));
