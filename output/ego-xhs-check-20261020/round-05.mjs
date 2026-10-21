const summary = await useOrCreateTaskSpace("ego-xhs-p14-check-b", { profileId: "Profile 14" });
console.log({ id: summary.id, profileId: summary.profileId, profileName: summary.profileName });

const task = await taskSpace(summary.id);
let page = null;
try {
  page = task.page("p1");
} catch {
  page = await task.newPage();
}
console.log({ page: page.label });
await page.goto("https://creator.xiaohongshu.com/publish/publish?source=official");
await page.waitForTimeout(5000);
console.log({ url: await page.url(), title: await page.title() });
console.log((await page.snapshot()).slice(0, 2000));
