const attempts = [
  ["test-p14-a", { profileId: "Profile 14" }],
  ["test-p14-b", { profile: "Profile 14" }],
  ["test-p14-c", { profileName: "Profile 14" }],
  ["test-p14-d", { profileDir: "Profile 14" }],
];

for (const [name, opts] of attempts) {
  try {
    const s = await newTaskSpace(name, opts);
    console.log(name, JSON.stringify(opts), "=>", JSON.stringify({ id: s.id, profileId: s.profileId, profileName: s.profileName }));
  } catch (e) {
    console.log(name, JSON.stringify(opts), "ERR", e.message);
  }
}
