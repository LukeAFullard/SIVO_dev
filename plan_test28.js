console.log("Ah!! The reviewer says: 'This is likely due to event bubbling (e.g., clicking the input triggers a parent element's click listener that completely re-renders the list and destroys the newly focused input).'");
console.log("Wait, is there a click listener on the parent element?");
console.log("Let's look at `index_template.html` and `builder.js` for `.shape-list` or `.shape-item` or anything that triggers a re-render.");
