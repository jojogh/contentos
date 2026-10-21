const task = await taskSpace(4);
const page = task.page("p1");
await page.goto("https://creator.xiaohongshu.com/new/note-manager");
await page.waitForTimeout(6000);
console.log({ url: await page.url(), title: await page.title() });
console.log((await page.snapshot({ scope: "full_page" })).slice(0, 6000));
