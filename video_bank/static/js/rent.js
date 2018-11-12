$(document).ready(function(){
console.log("plop");
    $(".rent").submit(function(event){
        console.log("je suis dans la fonction");
        var url = $(this).attr('action');
        var rented =  "True";
        console.log(url);
        $.ajax({
            url : url,
            data : {'rented': rented},
            method : "post",
            success : function(response){
                $(".rent").css('display', 'none');
                $(".btn_rent").css('display', 'none');
                $(".rented").html("<span style='color:red'>Le film est déjà loué</span>")
            }
        })

        event.preventDefault();
    });

});
