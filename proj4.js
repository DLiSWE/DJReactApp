document.addEventListener('click', async function(){
    
 const response = await fetch(`https://api.spoonacular.com/recipes/findByIngredients?ingredients=apple,+flour,+sugar&number=2&apiKey=979511531ff842c2bc17cbdef4754f97`, {
	"method": "GET",
	"headers": {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
	},
})
const data = await response.json();
let recipes = [];

for (let i=0;i<data.length;i++){
    recipes.push(data[i]);
}
console.log(recipes);
to_html(data);
return [data];
})
    // to_html(data[0])
    
function to_html(data){
    for (let i=0;i<data.length;i++){
        let food = document.createElement("div",{"id":`p${i}`});
        food.innerHTML =`<p>${data[i].title}</p>`;
        let food_id = document.createElement("div",{"id":`p${i}`});
        document.body.appendChild(food);
        document.body.appendChild(food_id);
        let misslen = data[i].missedIngredients.length;
        for (let x=0;x<misslen;x++){
            console.log(x);
        let missedIngred = document.createElement("div",{"id":`p${i}`});
        missedIngred.innerHTML =`<p>${data[i].missedIngredients[x].original}</p>`;
        document.body.appendChild(missedIngred);
    }
        // let missed = document.createElement("div",{"id":`p${i}`})
        // food.innerHTML = `<p>${data[i].missedIngredients.name}</p>`

        // document.body.appendChild(missedIngred)
    }
}