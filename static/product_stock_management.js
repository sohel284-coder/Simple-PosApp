var app = new Vue({
    el: "#app",
    delimiters: ['[[', ']]'],
    data:{
        msg:'hello',
        filters: [
            {
                label: 'drinks',
                options:{
                    water: '200mL',
                    juice: '300ml',
                }
              
            },
           
        ]
    },
    methods:{
        onChange: function(){
            alert('water is clicked');
        }
    }
})

$(document).ready(function(){
    
    $("#choice").click(function(){

    })
})
