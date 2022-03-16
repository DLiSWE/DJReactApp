$('#test').click(function(){
    $('#test').text('Well jquery is working')
})

let $ingreds = $(".toprow");
$ingreds.hide();

$(document).ready(function(){
    $(".pantrylistname").click(function(){
        $(".toprow").slideToggle("slow");
    });
});

function showHide(ingredients){
    $(`#recipe_for_${ingredients}`).click(function(){
        $(`#recipe_for_${ingredients}`).slideToggle("slow");
    });
};


async function getRecipe(Ingredients){
    const response = await fetch(`https://api.spoonacular.com/recipes/findByIngredients?ingredients=${Ingredients}&number=2&apiKey=4f67686c0fa74823907de359dd10cdfc`, {
       "method": "GET",
       "headers": {
           'Content-Type': 'application/json',
           'Accept': 'application/json',
       }}
   )
   const data = await response.json();
   $(document).ready(function(){ 
    $(".pantrylistitem").hide();
   })

   to_html(data,Ingredients);
   return;
    } 

// title recipe/missing ing

function to_html(data,ingredient){
        let main = document.getElementById("recipe_for_ingredient");
        main.innerHTML = ' '
        main.innerHTML += `<h3 class='ings'>${ingredient} Recipes:</h3>`       
        for (let i=0;i<data.length;i++){
        main.innerHTML += `<img class="rimg" src="${data[i].image}">`;
        main.innerHTML +=`<h5 class='ings'>${data[i].title}: Missing Ingredients: </h5>`;
        let misslen = data[i].missedIngredients.length;
        for (let x=0;x<misslen;x++){
            main.innerHTML += `<li class='ings'>${data[i].missedIngredients[x].originalName}</li>`;
        }
    }
}