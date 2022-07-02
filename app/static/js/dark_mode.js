
$(document).ready(function () {   

    console.log('dark_mode JS - document ready , javascript connected')


    //setting  initial state.
    $('.dynamic-content').hide()
    $('#profile_row').show()

    $('.nav-link').on("click", function(e){

        // console.log("one of the buttons was clicked")

        e.preventDefault()


        if(e.target.id == "profile_button"){

            console.log("clicked profile button")

            //modify 'active' class from all buttons 
            $('.nav-link').removeClass('active')
            $('#profile_button').addClass('active')

            //make that content visible
            $('.dynamic-content').hide()
            $('#profile_row').show()

        }else if(e.target.id == "programming_tools_button"){
            console.log("clicked programming tools button")

            $('.nav-link').removeClass('active')
            $('#programming_tools_button').addClass('active')

            $('.dynamic-content').hide()
            $('#programming_tools_row').show()

        }else if(e.target.id == "awards_button"){
            console.log("clicked awards button")

            // fetch_awards_ajax()

            $('.nav-link').removeClass('active')
            $('#awards_button').addClass('active')

            $('.dynamic-content').hide()
            $('#awards_row').show()

        }else if(e.target.id == "certifications_button"){
            console.log("clicked certifications button")

            $('.nav-link').removeClass('active')
            $('#certifications_button').addClass('active')

            $('.dynamic-content').hide()
            $('#certifications_row').show()

        }else if(e.target.id == "work_experiences_button"){
            console.log("clicked work experiences button")
            
            $('.nav-link').removeClass('active')
            $('#work_experiences_button').addClass('active')

            $('.dynamic-content').hide()
            $('#work_experiences_row').show()

        }else if(e.target.id == "education_button"){
            console.log("clicked education button")

            $('.nav-link').removeClass('active')
            $('#education_button').addClass('active')

            $('.dynamic-content').hide()
            $('#education_row').show()
        } else{
            console.log("That is not a valid target.id")
        }

    });

    function fetch_awards_ajax(){
        $.ajax({
            type: 'GET',
            url: "/fetch_awards_ajax",
            success: function(response) {
                console.log("function fetch_awards_ajax success")

                parsedResponse = JSON.parse(response)
                //attempt to input the text in the response 
                //into the html elements 🤔
                console.log('parsedResponse: ',parsedResponse)

                //location.reload();
                return
            },
            error: function(error){
                console.log("function fetch_awards_ajax error")
                return 
            }
        });
    }

});

    