const task = await useOrCreateTaskSpace("ego-xhs-p14-check", { profileId: "Profile 14" });
const page = task.page("p1");
await page.goto("https://creator.xiaohongshu.com/publish/publish?source=official");
await page.waitForTimeout(5000);

console.log({ spaceId: task.spaceId, url: await page.url(), title: await page.title() });
console.log((await page.snapshot()).slice(0, 3000));
