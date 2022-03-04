
console.log('connected')


$('#test').click(function(){
    if (document.getElementById('test').value != 'Index')
        $('#test').text('Index');
    else $('#test').text('Well jquery is working')
})