const task = await taskSpace("ego-xhs-login-check");
const page = task.page("p1");
await page.goto("https://creator.xiaohongshu.com/publish/publish?source=official");
await page.waitForTimeout(4000);

console.log({ spaceId: task.spaceId, url: await page.url(), title: await page.title() });

const shot = await page.screenshot({ path: "E:/project/content-os/output/ego-xhs-check-20261020/creator-landing.png" });
console.log({ screenshot: shot });

console.log(await page.snapshot());
