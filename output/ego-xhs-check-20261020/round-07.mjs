for (const fn of [newTaskSpace, taskSpace, useOrCreateTaskSpace, profiles]) {
  try {
    console.log("=====", fn.name);
    help(fn);
  } catch (e) {
    console.log("help failed:", e.message);
  }
}
