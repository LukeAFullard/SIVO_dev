console.log("The issue: The user types a name in the input inside shape-item list. Nothing updates until blur.");
console.log("If they type and press 'Enter', it does not blur, so the name isn't saved immediately. When they try to export or do something else, maybe the shape ID wasn't updated.");
console.log("If we add `input.addEventListener('keydown', (e) => { if (e.key === 'Enter') e.target.blur(); e.stopPropagation(); });` that solves the Enter issue.");
console.log("Also, if we look at `window.addEventListener('keydown', ...)` it has: `if (e.target.tagName.toLowerCase() === 'input' && e.target.type === 'text') return;`");
console.log("This correctly avoids intercepting keystrokes. But if the user clicks the list item and types a letter, the input captures it naturally.");
console.log("Wait, if I change it to `e.target.blur()` on Enter, that will fire the `change` event, triggering `updateShapeId(index, value)` -> `saveState()`. But wait, does it trigger a re-render of the canvas to reflect the new ID in memory? The ID is purely internal in the canvas until exported, it just changes `shapes[index].id`.");
