const removed = await deleteSpaces([1, 2, 3]);
console.log("removed:", JSON.stringify(removed));
console.log("remaining:", JSON.stringify((await listTaskSpaces()).map((s) => ({ id: s.id, name: s.name, profile: s.profileId }))));
