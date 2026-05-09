console.log("Wait, if clicking the input triggers a parent element's click listener... What parent element? `li`? No.");
console.log("`ul#shape-list`? No.");
console.log("`#sidebar`? No.");
console.log("Wait... is `updateShapeList` being called inside `annotator.js` randomly?");
console.log("Look at `canvas.addEventListener('mousedown'` -> `updateShapeList`?");
console.log("Wait! Does the input click bubble up to the `canvas`? No, they are siblings.");
console.log("What if `e.stopPropagation()` on `mousedown` and `click` on the input prevents it from bubbling to something we missed?");
