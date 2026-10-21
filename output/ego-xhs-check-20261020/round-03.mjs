const r = await useOrCreateTaskSpace("ego-xhs-p14-check", { profileId: "Profile 14" });
console.log(typeof r, r && typeof r === "object" ? Object.keys(r).join(",") : String(r));
