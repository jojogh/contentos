const surface = Object.getOwnPropertyNames(globalThis).filter((k) => /profil|task|space|help/i.test(k));
console.log("globals:", surface.join(", "));

for (const k of ["profiles", "listProfiles", "newTaskSpace", "useOrCreateTaskSpace", "taskSpace"]) {
  const v = globalThis[k];
  console.log(k, "=>", typeof v, v && typeof v === "object" ? Object.keys(v).join(",") : "");
}

console.log("spaces:", JSON.stringify(await listTaskSpaces()).slice(0, 1500));
